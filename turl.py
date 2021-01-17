#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import re
import json
import random

# str(...) -> UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding("utf8")

domain = os.getenv('TURL_DOMAIN')
args = []
if os.getenv('TURL_ARGS'):
    argk = None
    for argv in re.split(" +", os.getenv('TURL_ARGS').replace(": ", ":").replace("; ", ";")):
        if argk is None:
            if argv.startswith("-"):
                argk = argv
            else:
                domain = argv
        else:
            args.append({ "k": argk, "v": argv.replace("'", "").replace(":", ": ") })
            argk = None

turlFile = sys.argv[1]

vars = {}

failed = False

def runModule(module, index, indexPrefix, namePrefix):
    indexPath = indexPrefix + str(index + 1) + "."
    namePath = namePrefix + module["name"] + "/"
    if module["highlighted"]:
        runCase(indexPath, namePath, module["lines"])
    for i, child in enumerate(module["children"]):
        if module["highlighted"]:
            child["highlighted"] = True
        runModule(child, i, indexPath, namePath)

def runCase(indexPath, namePath, lines):
    if len(lines) < 1:
        return
    lastCurl = None
    lastRes = None
    for line in lines:
        if line.startswith("curl "):
            line = line.replace("curl ", "curl -s ")
            line = re.sub(' +', ' ', line)
            if domain is not None:
                line = re.sub('([^\-]+://)[^/]+(.+)', "\\1" + domain + "\\2", line)
            for arg in args:
                target = arg["k"] + " +[^']+"
                if arg["v"].find(":") > -1:
                    target = arg["k"] + " +'" + arg["v"][0:arg["v"].find(":")] + ": [^']+"
                line = re.sub(target, arg["k"] + " '" + arg["v"], line)
            line = applyVars(line)
            lastCurl = line
            lastResLines = os.popen(line).readlines()
            if len(lastResLines) < 1:
                lastRes = None
            else:
                lastRes = lastResLines[0]
        else:
            validateRes(indexPath, namePath, lastCurl, line, lastRes)

def applyVars(curl):
    curl = curl.replace("$lastRandom", lastRandom)
    curl = curl.replace("$random", nextRandom())
    for k, v in vars.items():
        curl = curl.replace(k, v)
    return curl

def nextRandom():
    lastRandom = str(random.randint(0,9999999999))
    return lastRandom

def validateRes(indexPath, namePath, curl, expJson, actJson):
    if actJson is None:
        sys.stderr.write(indexPath[2:-1] + "\t" + namePath[1:-1] + "\t" + curl + "\t(Empty)\t" + expJson + "\tBad response\n")
        failed = True
        return
    exp = None
    try:
        exp = json.loads(expJson)
    except Exception as e:
        sys.stderr.write('Bad expected JSON: ' + expJson)
        exit(1)
    act = None
    try:
        act = json.loads(actJson)
    except Exception as e:
        sys.stderr.write(indexPath[2:-1] + "\t" + namePath[1:-1] + "\t" + curl + "\t" + actJson + "\t" + expJson + "\tBad response JSON\n")
        failed = True
        return
    errors = validateObj("res", exp, act)
    if len(errors) > 0:
        sys.stderr.write(indexPath[2:-1] + "\t" + namePath[1:-1] + "\t" + curl + "\t" + actJson + "\t" + expJson + "\tValidation failed: " + errors + "\n")
        failed = True
    else:
        print indexPath[2:-1] + "\t" + namePath[1:-1] + "\t" + curl + "\t" + actJson + "\t" + expJson + "\tOK\n"

def validateObj(objPath, exp, act):
    errors = ""
    for k, expV in exp.items():
        actV = act.get(k)
        if expV is None:
            if actV is not None:
                errors += objPath + "." + k + " should be null; "
        elif actV is None:
            errors += objPath + "." + k + " should not be null; "
        elif type(expV) == bool:
            if type(actV) != bool:
                errors += objPath + "." + k + "'s value " + str(actV) + " is not bool; "
        elif type(expV) == int or type(expV) == float:
            if type(actV) != int and type(actV) != float:
                errors += objPath + "." + k + "'s value " + str(actV) + " is not int or float; "
        elif type(expV) == str or type(expV) == unicode:
            if re.match("^\$[a-zA-Z_]+$", expV):
                vars[expV] = actV
            if expV.endswith(")"):
                rule = expV[expV.find("("):][1:-1]
            #    print rule
            #if type(actV) != str and type(actV) != unicode:
            #    errors += objPath + "." + k + "'s value " + str(actV) + " is not string or unicode; "
        elif type(expV) == list:
            if type(actV) != list:
                errors += objPath + "." + k + "'s value " + str(actV) + " is not list; "
            else:
                for i, item in enumerate(actV):
                    errors += validateObj(objPath + "." + k + "[" + str(i) + "]", expV[0], item)
        else:
            if type(actV) != dict:
                errors += objPath + "." + k + "'s value " + str(actV) + " is not dict; "
            else:
                errors += validateObj(objPath + "." + k, expV, actV)
    return errors

def build():
    turlML = readTurlFile("", turlFile)

    state = "IN_MODULE"
    currentModule = rootModule = { "highlighted": True, "name": "", "children": [], "lines": [] }
    for line in turlML.split("\n"):
        line = line.strip()
        if len(line) < 1:
            continue
        if state == "IN_MODULE":
            if line.startswith("curl "):
                currentModule["lines"].append(line)
                state = "IN_CASE"
            else:
                currentModule = metNewModule(rootModule, line)
        elif state == "IN_CASE":
            if line.startswith("curl ") or line.startswith("{"):
                currentModule["lines"].append(line)
            else:
                currentModule = metNewModule(rootModule, line)
                state = "IN_MODULE"
    return rootModule

def readTurlFile(turlML, file):
    f = open(file)
    for line in f.readlines():
        if line.startswith("("):
            turlML = ref(turlML, line.rstrip("\n")[1:-1])
        else:
            turlML += line.replace("\\\n", " ")
    f.close()
    return turlML

def ref(turlML, filePattern):
    refFileNames = [fileName for fileName in os.listdir(".") if re.match(filePattern.replace("(", "\\(").replace(")", "\\)").replace("*", ".*"), fileName)]
    for refFileName in refFileNames:
        turlML += "\n"
        turlML = readTurlFile(turlML, refFileName)
    return turlML

def metNewModule(rootModule, line):
    moduleName = line
    highlighted = False
    if moduleName.startswith("!!!"):
        highlighted = True
        rootModule["highlighted"] = False
        moduleName = moduleName[3:].lstrip()
    modulePathMatcher = re.match(r'^([0-9X\.]+) *(.*)', moduleName)
    if modulePathMatcher:
        modulePath = modulePathMatcher.group(1)
        moduleName = modulePathMatcher.group(2)
    else:
        modulePath = "X"

    parentModule = rootModule
    modulePathParts = modulePath.split(".")
    partIndex = 0
    for moduleIndexStr in modulePathParts:
        moduleIndex = 0
        if moduleIndexStr == "X":
            if partIndex < len(modulePathParts) - 1:
                moduleIndex = len(parentModule["children"]) - 1
                if moduleIndex < 0:
                    moduleIndex = 0
            else:
                moduleIndex = len(parentModule["children"])
        else:
            moduleIndex = int(moduleIndexStr) - 1
        for emptyModuleIndex in range(len(parentModule["children"]), moduleIndex + 1):
            parentModule["children"].append({ "highlighted": False, "name": "", "children": [], "lines": [] })
        parentModule = parentModule["children"][moduleIndex]
        partIndex += 1
    parentModule["name"] = moduleName
    parentModule["highlighted"] = highlighted
    return parentModule

lastRandom = ""

rootModule = build()
runModule(rootModule, 0, "", "")

if failed:
    exit(1)
else:
    exit(0)
