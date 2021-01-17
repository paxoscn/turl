# 网关服务


**简介**:网关服务


**HOST**:test-soul-admin.k8s.startdtapi.com


**联系人**:刑天


**Version**:1.0


**接口路径**:http://test-soul-server.k8s.startdtapi.com/admin/v2/api-docs


[TOC]






# license服务


## 激活


**接口地址**:`/license/activity`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"key": "",
	"onlyId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|req|req|body|true|ActicityReq|ActicityReq|
|&emsp;&emsp;key|激活码||true|string||
|&emsp;&emsp;onlyId|实例id||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc||string||
|codeNum||integer(int32)|integer(int32)|
|success||boolean||
|value||object||


**响应示例**:
```javascript
{
	"codeDesc": "",
	"codeNum": 0,
	"success": true,
	"value": {}
}
```


## license状态查询


**接口地址**:`/license/status`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult«LicenseConfigVO»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc||string||
|codeNum||integer(int32)|integer(int32)|
|success||boolean||
|value||LicenseConfigVO|LicenseConfigVO|
|&emsp;&emsp;key|激活码|string||
|&emsp;&emsp;onlyId|实例id|string||
|&emsp;&emsp;status|状态 0:不存在 1：有效，2:license已经使用 3：实例不匹配，4：时间过期|integer(int32)||
|&emsp;&emsp;endTime|有效截止时间|string||
|&emsp;&emsp;remindDays|剩余天数|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "",
	"codeNum": 0,
	"success": true,
	"value": {
		"key": "",
		"onlyId": "",
		"status": 0,
		"endTime": "",
		"remindDays": 0
	}
}
```


## syncData


**接口地址**:`/license/syncData`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SoulAdminResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code||integer(int32)|integer(int32)|
|data||object||
|message||string||


**响应示例**:
```javascript
{
	"code": 0,
	"data": {},
	"message": ""
}
```


## license上传安装


**接口地址**:`/license/upload`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|false|file||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult«LicenseConfigVO»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc||string||
|codeNum||integer(int32)|integer(int32)|
|success||boolean||
|value||LicenseConfigVO|LicenseConfigVO|
|&emsp;&emsp;key|激活码|string||
|&emsp;&emsp;onlyId|实例id|string||
|&emsp;&emsp;status|状态 0:不存在 1：有效，2:license已经使用 3：实例不匹配，4：时间过期|integer(int32)||
|&emsp;&emsp;endTime|有效截止时间|string||
|&emsp;&emsp;remindDays|剩余天数|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "",
	"codeNum": 0,
	"success": true,
	"value": {
		"key": "",
		"onlyId": "",
		"status": 0,
		"endTime": "",
		"remindDays": 0
	}
}
```


# simba-auth-controller


## appkey新增修改


**接口地址**:`/simbaAuth/apply`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"appKey": "",
	"appName": "",
	"appSecret": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|simbaAppAuthApplyDTO|simbaAppAuthApplyDTO|body|true|SimbaAppAuthApplyDTO|SimbaAppAuthApplyDTO|
|&emsp;&emsp;appKey|凭证key||false|string||
|&emsp;&emsp;appName|应用名||false|string||
|&emsp;&emsp;appSecret|密钥||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult«ObjectResult«boolean»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc||string||
|codeNum||integer(int32)|integer(int32)|
|success||boolean||
|value||ObjectResult«boolean»|ObjectResult«boolean»|
|&emsp;&emsp;data||boolean||


**响应示例**:
```javascript
{
	"codeDesc": "",
	"codeNum": 0,
	"success": true,
	"value": {
		"data": true
	}
}
```


## appkey删除


**接口地址**:`/simbaAuth/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|appKey|appKey|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult«ObjectResult«boolean»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc||string||
|codeNum||integer(int32)|integer(int32)|
|success||boolean||
|value||ObjectResult«boolean»|ObjectResult«boolean»|
|&emsp;&emsp;data||boolean||


**响应示例**:
```javascript
{
	"codeDesc": "",
	"codeNum": 0,
	"success": true,
	"value": {
		"data": true
	}
}
```


# swagger-controller


## swaggerResources


**接口地址**:`/swagger-resources`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SwaggerResource|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|location||string||
|name||string||
|swaggerVersion||string||
|url||string||


**响应示例**:
```javascript
[
	{
		"location": "",
		"name": "",
		"swaggerVersion": "",
		"url": ""
	}
]
```