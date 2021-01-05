# tURL

RESTiful接口自动测试工具。

读取.turl文件，自动执行接口测试。

* turl文件是用来描述测试用例及接口请求和响应定义的专有格式。

## 1 使用步骤
### 1.1 编写.turl文件
请参考 [2 turl文件格式](#2-turl文件格式)

### 1.2 设置环境变量
在执行测试前可设置以下环境变量来改变测试时使用的全局参数：

| 环境变量 | 描述 |
| --- | --- |
| TURL_DOMAIN | 接口所属的域名 |
| TURL_ARGS | 访问接口时设置的cURL参数 |

#### 示例
```shell script
% export TURL_DOMAIN="test-simba.startdt.net"
% export TURL_ARGS="-H 'token: eyJ...mf8' -H 'Cookie: exp...031'"
```

### 1.3 执行测试
将.turl文件作为参数传入turl.py并执行。

成功用例的请求信息将打印在stdout中，失败用例的信息则会打印在stderr中。

输出信息以\t分隔，格式如下：

| 编号 | 模块/用例名称 | cURL命令 | cURL响应 | 响应定义 | 测试用例结果描述 |
| --- | --- | --- | --- | --- | --- |

#### 示例
```shell script
% python turl.py xxx.turl
1.1.1	运维平台/日志管理/获取日志列表	curl -s 'http://tes...	{"success":true,...}	{"success":true,...}	OK
...
```

#### 在项目目录下存有一组示例turl文件，可以通过以下命令调用参考：
```shell script
% export TURL_DOMAIN="test-simba.startdt.net"
% export TURL_ARGS="-H 'token: eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJzaW1iYSIsInN1YiI6IntcImFjY291bnRJZFwiOjEzMjY0ODUxOTA2MDgwMzE3NDQsXCJhY2NvdW50Q29kZVwiOlwic3RhcnRkdFwiLFwibmFtZVwiOlwibW9yaWdlbkBzdGFydGR0XCIsXCJ1c2VyVHlwZVwiOjc3NyxcInVzZXJOYW1lXCI6XCJtb3JpZ2VuXCIsXCJ1c2VySWRcIjoxMDYwOCxcInByaW1hcnlVc2VySWRcIjoxNSxcInJlZnJlc2hUb2tlblwiOlwic2ltYmE6YXV0aDpzZXNzaW9uOjcxOGVlMWI3NDU1ZTVmODYzYzc2YmU5MzQ2YzYzZTk4XCJ9IiwiaXNzIjoic2ltYmEiLCJpYXQiOjE2MDk2OTQwMzYsImV4cCI6MTYwOTc4MDQzNn0.VcyElXkVk18G6jTAVSJ9iWb3uoFpFkopz3GsZESamf8' -H 'Cookie: experimentation_subject_id=ImM5YjZlNTQ3LWZiZTgtNGMwYi1iM2JjLTE5ODMzMmRiNDY2NCI%3D--ccd989d7278bf4806438d7efebaf3aa8beb5e763; SERVERID=cb6a5096204fd12c537ba954f3414f4a|1609694037|1609694031'"
% python turl.py simba.turl
```

## 2 turl文件格式
turl文件可包含以下内容：

### 2.1 模块/测试用例名称
以文字或数字开头的模块或用例的标题，用于在执行测试后标示是哪个用例产生的结果。

"用例"指模块树中的叶子模块，通常包含一对或多对cURL命令和响应定义。

标题前可使用数字进行编号，格式为以"."分隔的数字。数字可使用"X"来代表自动顺延。

编号的层级决定了用例或模块的层级关系，

在该行开头可使用"!!!"前缀表示本次执行只实际执行该模块或用例而忽略其他所有模块和用例，从而方便调试单个模块或用例。若有多处模块或用例被标注了"!!!"，则只有最后一个会被执行。

#### 示例
```text
1.1 工作空间
X.X.X 创建工作空间
!!! X.X.X 删除工作空间
```

### 2.2 cURL请求命令
以"curl"开头，在用例中被实际执行的cURL请求命令。

通常可以直接从Chrome的控制台复制出该命令并粘贴至此。

在其下一行通常跟着该命令期望的响应定义，若没有响应定义则tURL会忽略其响应。

在命令中可以使用$开头的全局变量来在运行时替换成需要的值，请参考 [2.5 全局变量](#25-全局变量)

#### 示例
```text
curl 'http://test-simba.startdt.net/api/upms/api/v3/workspaces' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'Content-Type: application/json;charset=utf-8' \
  -H 'Referer: http://test-simba.startdt.net/workspace/workspaceManage/' \
  --compressed \
  --insecure \
  -d '{"code":"turl-$random","name":"turl-$random","description":"turl-$random","visitUrl":"http://dev-fe-simba.k8s.startdt.com","apiUrl":"http://dev-soul-server.k8s.startdtapi.com","favicon":"aaa","title":"aaa","logo":"aaa","copyright":"aaa" }'
```

### 2.3 响应定义
以"{}"包围，在用例中用以验证cURL实际请求响应的JSON定义。

通常可以直接从Chrome的控制台复制出响应并粘贴至此。

在定义中可以使用$开头的全局变量来在运行时将响应值赋给全局变量，以便后续请求使用，请参考 [2.5 全局变量](#25-全局变量)

#### 示例
```text
{"success":true,"codeNum":1000,"codeDesc":"","value":{"data":{"workspaceId":"$workspaceId","code":"test","name":"test","description":"test","status":0,"visitUrl":"http://dev-fe-simba.k8s.startdt.com","apiUrl":"http://dev-soul-server.k8s.startdtapi.com","favicon":"","title":"","logo":"","copyright":"","createUserName":"","createTime":1608700110430,"modifyUserName":"","modifyTime":1608700110430,"engineList":[],"resourceGroupList":[]}}}
```

### 2.4 turl文件引用
以"()"包围的turl文件名，在文件中引用其他turl文件的内容，方便模块化管理用例。

注意请勿进行文件循环引用，这可能会出错或耗尽您的系统资源。

#### 示例
```text
(logs.turl)
```

### 2.5 全局变量
在cURL请求和响应定义中标示一个全局可访问的变量。

全局变量包含自定义变量和预设变量。自定义变量在实际响应中被赋值，可在后续请求中被使用。预设变量由tURL自动进行赋值，可直接在请求中使用。

预设变量表如下：

| 预设变量 | 取值 | 描述 |
| --- | --- | --- |
| random | 随机整数 | 可用在创建实体类接口中的实体名称中，避免可能的名称重复。请参考workspaces.turl中的应用。 |

## 3 与第三方系统的集成
### 3.1 Swagger
TODO

### 3.2 Knife4j
请将从Knife4j下载的Markdown文件放在任一文件夹下并执行项目中的knife4j.py，生成的testcases.turl即为需要的turl文件.

## 4 版本变更历史
| 版本 | 日期 | 描述 |
| --- | --- | --- |
| 0.0.2 | 2021-01-06 | 增加knife4j.py |
| 0.0.1 | 2021-01-05 | 初始版本 |

## 5 关于作者
unrealwalker#gmail.com
