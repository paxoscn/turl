#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import re
import json
import random

reload(sys)
sys.setdefaultencoding("utf8")

def endCase(turlFile, case):
    caseStr = ""
    caseStr += "curl -X" + case["method"] + " 'http://default-host" + case["path"] + "?1=1"
    for param in case["params"]:
        if param["required"]:
            caseStr += "&" + param["name"] + "=1111111"
    caseStr += "' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: zh-CN' -H 'token: ...' -H 'Content-Type: application/json;charset=utf-8' -H 'Cookie: ...' --compressed --insecure"
    if case["req"] is not None:
        caseStr += " -d '" + case["req"] + "'"
    caseStr += "\n\n" + case["res"] + "\n\n"
    turlFile.write(caseStr + "\n")

mainTURL = ""
mdFileNames = [fileName for fileName in os.listdir(".") if re.match(".*.md", fileName) and fileName != "README.md"]
for mdFileName in mdFileNames:
    mainTURL += "X " + mdFileName[:-3] + "\n\n(" + mdFileName[:-3] + ".turl)\n\n"
    mdFile = open(mdFileName)
    turlFile = open(mdFileName[:-3] + ".turl", "w")
    state = "INIT"
    currentCase = None
    for line in mdFile.readlines():
        line = line.strip()
        if state == "INIT":
            if line.startswith("# "):
                state = "AWAITING_MODULE"
        elif state == "AWAITING_MODULE":
            if line.startswith("# "):
                turlFile.write("X.X " + line[2:] + "\n")
                state = "AWAITING_CASE"
        elif state == "AWAITING_CASE":
            if line.startswith("## "):
                turlFile.write("X.X.X " + line[3:] + "\n")
                currentCase = { "req": None, "params": [] }
                state = "IN_CASE"
        elif state == "IN_CASE":
            if line.startswith("**"):
                if line.startswith("**接口地址**"):
                    currentCase["path"] = line[line.find("`") + 1:-1]
                elif line.startswith("**请求方式**"):
                    currentCase["method"] = line[line.find("`") + 1:-1]
                elif line.startswith("**请求示例**"):
                    state = "AWAITING_REQ"
                elif line.startswith("**请求参数**"):
                    state = "AWAITING_PARAMS"
                elif line.startswith("**响应示例**"):
                    state = "AWAITING_RES"
            elif line.startswith("# "):
                endCase(turlFile, currentCase)
                currentCase = None
                turlFile.write("X.X " + line[2:] + "\n")
                state = "AWAITING_CASE"
            elif line.startswith("## "):
                endCase(turlFile, currentCase)
                currentCase = None
                turlFile.write("X.X.X " + line[3:] + "\n")
                currentCase = { "req": None, "params": [] }
                state = "IN_CASE"
        elif state == "AWAITING_REQ":
            if line.startswith("{"):
                currentCase["req"] = line
                state = "IN_REQ"
        elif state == "IN_REQ":
            currentCase["req"] += line
            if line.startswith("}"):
                state = "IN_CASE"
        elif state == "AWAITING_PARAMS":
            if line.startswith("| -"):
                state = "IN_PARAMS"
            elif line == "暂无":
                state = "IN_CASE"
        elif state == "IN_PARAMS":
            if len(line) < 1:
                state = "IN_CASE"
            else:
                paramParts = line.split("|")
                currentCase["params"].append({ "name": paramParts[1].replace("&emsp;", ""), "in": paramParts[3], "required": paramParts[4] == "true", "type": paramParts[5] })
        elif state == "AWAITING_RES":
            if line.startswith("{"):
                currentCase["res"] = line
                state = "IN_RES"
        elif state == "IN_RES":
            currentCase["res"] += line
            if line.startswith("}"):
                state = "IN_CASE"

    if currentCase is not None:
        endCase(turlFile, currentCase)
        currentCase = None

    turlFile.close()
    mdFile.close()

mainFile = open("testcases.turl", "w")
mainFile.write(mainTURL)
mainFile.close()
