# 测试的描述


**简介**:测试的描述


**HOST**:datasimba-customerauth-svc.test.svc.cluster.local


**联系人**:


**Version**:1.0


**接口路径**:http://test-soul-server.k8s.startdtapi.com/customerauth/v2/api-docs


[TOC]






# 账号管理-子账号管理


## 获取子账号列表


**接口地址**:`/auth/accounts`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|true|integer(int32)||
|pageSize|分页大小|query|true|integer(int32)||
|name|登录名或用户名|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«子账号列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«子账号列表»|PageResult«子账号列表»|
|&emsp;&emsp;data||array|子账号列表|
|&emsp;&emsp;&emsp;&emsp;admin|管理员,默认0-非管理员，1-管理员|boolean||
|&emsp;&emsp;&emsp;&emsp;createTime|创建日期|string||
|&emsp;&emsp;&emsp;&emsp;email|邮箱|string||
|&emsp;&emsp;&emsp;&emsp;loginName|用户账号|string||
|&emsp;&emsp;&emsp;&emsp;moduleIds|模块角色列表|array|模块信息|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;moduleId|模块编号|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;title|标题|string||
|&emsp;&emsp;&emsp;&emsp;phone|手机号码|string||
|&emsp;&emsp;&emsp;&emsp;roleIds|账号角色（多个角色逗号分隔）|string||
|&emsp;&emsp;&emsp;&emsp;theme|主题，默认黑色0，白色1|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;userId|用户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|用户名|string||
|&emsp;&emsp;pageInfo||PageInfo|PageInfo|
|&emsp;&emsp;&emsp;&emsp;currentPage||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;pageSize||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;totalCount||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;totalPage||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"admin": false,
				"createTime": "",
				"email": "",
				"loginName": "",
				"moduleIds": [
					{
						"moduleId": 0,
						"title": ""
					}
				],
				"phone": "",
				"roleIds": "",
				"theme": 0,
				"userId": 0,
				"userName": ""
			}
		],
		"pageInfo": {
			"currentPage": 0,
			"pageSize": 0,
			"totalCount": 0,
			"totalPage": 0
		}
	}
}
```


## 子账号配置-账号角色列表【修改】


**接口地址**:`/auth/accounts/roles`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«成员角色下拉列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«成员角色下拉列表»|CollectionResult«成员角色下拉列表»|
|&emsp;&emsp;data||array|成员角色下拉列表|
|&emsp;&emsp;&emsp;&emsp;description|角色描述|string||
|&emsp;&emsp;&emsp;&emsp;roleId|角色id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;roleName|角色名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"description": "",
				"roleId": 0,
				"roleName": ""
			}
		]
	}
}
```


## V2.2.0【新增】个人设置-账号安全-修改密码


**接口地址**:`/auth/accounts/updatePassword`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"id": 0,
	"newPwd": "",
	"oldPwd": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userPwdUpdateReq|userPwdUpdateReq|body|true|修改子账号密码|修改子账号密码|
|&emsp;&emsp;id|用户ID||false|integer(int64)||
|&emsp;&emsp;newPwd|新密码||false|string||
|&emsp;&emsp;oldPwd|原密码||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## V2.2.0【修改】新增子账号


**接口地址**:`/auth/accounts/user`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"email": "",
	"loginName": "",
	"password": "",
	"phone": "",
	"userName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userAddReq|userAddReq|body|true|新增子账号|新增子账号|
|&emsp;&emsp;email|邮箱||false|string||
|&emsp;&emsp;loginName|用户账号（登录名）||false|string||
|&emsp;&emsp;password|密码||false|string||
|&emsp;&emsp;phone|手机号码||false|string||
|&emsp;&emsp;userName|用户姓名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## V2.2.0【新增】个人设置-基本信息-修改


**接口地址**:`/auth/accounts/user/updateUser`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"email": "",
	"id": 0,
	"loginName": "",
	"phone": "",
	"userName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|个人设置-基本信息修改|个人设置-基本信息修改|
|&emsp;&emsp;email|邮箱||false|string||
|&emsp;&emsp;id|用户ID||false|integer(int64)||
|&emsp;&emsp;loginName|用户账号（登录名）||false|string||
|&emsp;&emsp;phone|手机号码||false|string||
|&emsp;&emsp;userName|用户姓名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 删除子账号


**接口地址**:`/auth/accounts/users`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"userIds": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userIdsReq|userIdsReq|body|true|多个子账号id|多个子账号id|
|&emsp;&emsp;userIds|多个用户id，以逗号分隔||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 修改子账号


**接口地址**:`/auth/accounts/{userId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"email": "",
	"loginName": "",
	"phone": "",
	"roleIds": "",
	"theme": 0,
	"userName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateReq|updateReq|body|true|修改子账号|修改子账号|
|&emsp;&emsp;email|邮箱||false|string||
|&emsp;&emsp;loginName|用户账号（登录名）||false|string||
|&emsp;&emsp;phone|手机号码||false|string||
|&emsp;&emsp;roleIds|成员角色（多个角色逗号分隔）||false|string||
|&emsp;&emsp;theme|首页主题，默认黑色0，白色1||false|integer(int32)||
|&emsp;&emsp;userName|用户姓名||false|string||
|userId|用户id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## V2.2.0【修改】个人设置-基本信息


**接口地址**:`/auth/accounts/{userId}/getUserById`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|用户id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«用户信息响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«用户信息响应对象»|ObjectResult«用户信息响应对象»|
|&emsp;&emsp;data||用户信息响应对象|用户信息响应对象|
|&emsp;&emsp;&emsp;&emsp;email|邮箱|string||
|&emsp;&emsp;&emsp;&emsp;id|用户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;loginName|登录名|string||
|&emsp;&emsp;&emsp;&emsp;name|用户名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父id，如果是主账号，为空|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;password|密码|string||
|&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;theme|背景主题|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;type|类型 主账号：888 子账号：777|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;userName|用户名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"email": "",
			"id": 0,
			"loginName": "",
			"name": "",
			"parentId": 0,
			"password": "",
			"phone": "",
			"theme": 0,
			"type": 0,
			"userName": ""
		}
	}
}
```


## 授权


**接口地址**:`/auth/accounts/{userId}/privileges`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"admin": false,
	"moduleIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|privilegeAssignReq|privilegeAssignReq|body|true|授权|授权|
|&emsp;&emsp;admin|管理员||false|boolean||
|&emsp;&emsp;moduleIds|授权模块ID集合||false|array|integer|
|userId|用户id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 重置密码为123456


**接口地址**:`/auth/accounts/{userId}/resetPassword`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|用户id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## V2.2.0【新增】个人设置-主题切换


**接口地址**:`/auth/accounts/{userId}/theme/{themeId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|用户id|path|true|integer(int64)||
|themeId|主题ID,默认0-黑色、1-白色|path|true|ref||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


# simba平台登录


## 检查心跳


**接口地址**:`/check/session`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 根据ticket获取用户信息


**接口地址**:`/check/ticket`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"pwd": "",
	"ticket": "",
	"userName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|thirdCheckReq|thirdCheckReq|body|true|全知获取session接口|全知获取session接口|
|&emsp;&emsp;pwd|密码||false|string||
|&emsp;&emsp;ticket|ticket||false|string||
|&emsp;&emsp;userName|登录名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«string»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": ""
}
```


## 根据用户名和密码获取用户信息


**接口地址**:`/check/user`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"pwd": "",
	"ticket": "",
	"userName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|thirdCheckReq|thirdCheckReq|body|true|全知获取session接口|全知获取session接口|
|&emsp;&emsp;pwd|密码||false|string||
|&emsp;&emsp;ticket|ticket||false|string||
|&emsp;&emsp;userName|登录名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«用户信息响应对象»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||用户信息响应对象|用户信息响应对象|
|&emsp;&emsp;email|邮箱|string||
|&emsp;&emsp;id|用户id|integer(int64)||
|&emsp;&emsp;loginName|登录名|string||
|&emsp;&emsp;name|用户名称|string||
|&emsp;&emsp;parentId|父id，如果是主账号，为空|integer(int64)||
|&emsp;&emsp;password|密码|string||
|&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;theme|背景主题|integer(int32)||
|&emsp;&emsp;type|类型 主账号：888 子账号：777|integer(int32)||
|&emsp;&emsp;userName|用户名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"email": "",
		"id": 0,
		"loginName": "",
		"name": "",
		"parentId": 0,
		"password": "",
		"phone": "",
		"theme": 0,
		"type": 0,
		"userName": ""
	}
}
```


## 检查登录用户


**接口地址**:`/checkUser`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|token|token|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«登录响应对象»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«登录响应对象»|ObjectResult«登录响应对象»|
|&emsp;&emsp;data||登录响应对象|登录响应对象|
|&emsp;&emsp;&emsp;&emsp;accountCode|租户编号|string||
|&emsp;&emsp;&emsp;&emsp;accountId|租户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;id|用户编号|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;token|用户token|string||
|&emsp;&emsp;&emsp;&emsp;userName|用户名|string||
|&emsp;&emsp;&emsp;&emsp;userType|用户类型 类型  0:PE管理员 主账号：888 子账号：777|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"accountCode": "",
			"accountId": 0,
			"id": 0,
			"token": "",
			"userName": "",
			"userType": 0
		}
	}
}
```


## 用户登出


**接口地址**:`/logout`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## pe用户登录


**接口地址**:`/pe/login`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"loginName": "",
	"pwd": "",
	"type": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|loginReq|loginReq|body|true|登录请求对象|登录请求对象|
|&emsp;&emsp;code|验证码||false|string||
|&emsp;&emsp;loginName|登录名||false|string||
|&emsp;&emsp;pwd|密码||false|string||
|&emsp;&emsp;type|环境类型||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«登录响应对象»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«登录响应对象»|ObjectResult«登录响应对象»|
|&emsp;&emsp;data||登录响应对象|登录响应对象|
|&emsp;&emsp;&emsp;&emsp;accountCode|租户编号|string||
|&emsp;&emsp;&emsp;&emsp;accountId|租户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;id|用户编号|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;token|用户token|string||
|&emsp;&emsp;&emsp;&emsp;userName|用户名|string||
|&emsp;&emsp;&emsp;&emsp;userType|用户类型 类型  0:PE管理员 主账号：888 子账号：777|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"accountCode": "",
			"accountId": 0,
			"id": 0,
			"token": "",
			"userName": "",
			"userType": 0
		}
	}
}
```


## test


**接口地址**:`/test`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## test2


**接口地址**:`/test2`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## test3


**接口地址**:`/test3`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## test4


**接口地址**:`/test4`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## test5


**接口地址**:`/test5`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 用户登录


**接口地址**:`/v2/login`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"loginName": "",
	"pwd": "",
	"type": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|loginReq|loginReq|body|true|登录请求对象|登录请求对象|
|&emsp;&emsp;code|验证码||false|string||
|&emsp;&emsp;loginName|登录名||false|string||
|&emsp;&emsp;pwd|密码||false|string||
|&emsp;&emsp;type|环境类型||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«登录响应对象»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«登录响应对象»|ObjectResult«登录响应对象»|
|&emsp;&emsp;data||登录响应对象|登录响应对象|
|&emsp;&emsp;&emsp;&emsp;accountCode|租户编号|string||
|&emsp;&emsp;&emsp;&emsp;accountId|租户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;id|用户编号|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;token|用户token|string||
|&emsp;&emsp;&emsp;&emsp;userName|用户名|string||
|&emsp;&emsp;&emsp;&emsp;userType|用户类型 类型  0:PE管理员 主账号：888 子账号：777|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"accountCode": "",
			"accountId": 0,
			"id": 0,
			"token": "",
			"userName": "",
			"userType": 0
		}
	}
}
```


## 获取验证码


**接口地址**:`/verifyCode`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|loginName|loginName|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 查询是否开启验证码


**接口地址**:`/verifyCode/status`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|loginName|loginName|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«boolean»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«boolean»|ObjectResult«boolean»|
|&emsp;&emsp;data||boolean||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": true
	}
}
```


# 账号管理-安全设置


## 获取安全设置


**接口地址**:`/config/security`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«安全设置对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«安全设置对象»|ObjectResult«安全设置对象»|
|&emsp;&emsp;data||安全设置对象|安全设置对象|
|&emsp;&emsp;&emsp;&emsp;smsCodeNeeded|登录时是否需要短信验证码|boolean||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"smsCodeNeeded": false
		}
	}
}
```


## 修改安全设置


**接口地址**:`/config/security`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"smsCodeNeeded": false
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|securityConfigVo|securityConfigVo|body|true|安全设置对象|安全设置对象|
|&emsp;&emsp;smsCodeNeeded|登录时是否需要短信验证码||true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


# 测试


## get


**接口地址**:`/test/get`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|userId|query|false|string||
|url|url|query|false|string||
|httpMethod|httpMethod|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|HttpResult|
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


# 角色、权限管理【新增】


## 项目配置-获取角色权限列表


**接口地址**:`/auth/roleMapping/listAuth/{roleId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|roleId|角色Id|path|true|ref||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«角色权限列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«角色权限列表»|CollectionResult«角色权限列表»|
|&emsp;&emsp;data||array|角色权限列表|
|&emsp;&emsp;&emsp;&emsp;children|二级权限列表|array|权限列表|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|二级权限code|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;moduleName|二级权限|string||
|&emsp;&emsp;&emsp;&emsp;code|一级权限code|string||
|&emsp;&emsp;&emsp;&emsp;moduleName|一级权限名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"children": [
					{
						"code": "",
						"moduleName": ""
					}
				],
				"code": "",
				"moduleName": ""
			}
		]
	}
}
```


## V2.2.0 【新增】子账号配置-登录获取账号首页模块权限列表


**接口地址**:`/auth/roleMapping/listAuthHomeModules/{userId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|登录账号|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«主页所有授权模块信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«主页所有授权模块信息»|CollectionResult«主页所有授权模块信息»|
|&emsp;&emsp;data||array|主页所有授权模块信息|
|&emsp;&emsp;&emsp;&emsp;detail|内容详情|string||
|&emsp;&emsp;&emsp;&emsp;icon|图标url|string||
|&emsp;&emsp;&emsp;&emsp;moduleId|模块编号|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;opened|授权标志|boolean||
|&emsp;&emsp;&emsp;&emsp;platformCode|平台代码 1-平台、2-首页模块、3-资源、数据源管理、账号管理角色|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;title|标题|string||
|&emsp;&emsp;&emsp;&emsp;url|url|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"detail": "",
				"icon": "",
				"moduleId": 0,
				"opened": false,
				"platformCode": 0,
				"title": "",
				"url": ""
			}
		]
	}
}
```


## V2.2.0 【新增】子账号配置-登录获取账号首页资源管理、数据源管理、账号中心权限


**接口地址**:`/auth/roleMapping/listAuthMgrModules/{userId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|登录账号|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«主页所有授权模块信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«主页所有授权模块信息»|CollectionResult«主页所有授权模块信息»|
|&emsp;&emsp;data||array|主页所有授权模块信息|
|&emsp;&emsp;&emsp;&emsp;detail|内容详情|string||
|&emsp;&emsp;&emsp;&emsp;icon|图标url|string||
|&emsp;&emsp;&emsp;&emsp;moduleId|模块编号|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;opened|授权标志|boolean||
|&emsp;&emsp;&emsp;&emsp;platformCode|平台代码 1-平台、2-首页模块、3-资源、数据源管理、账号管理角色|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;title|标题|string||
|&emsp;&emsp;&emsp;&emsp;url|url|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"detail": "",
				"icon": "",
				"moduleId": 0,
				"opened": false,
				"platformCode": 0,
				"title": "",
				"url": ""
			}
		]
	}
}
```


## V2.2.0 【新增】新增子账号配置获取授权模块列表


**接口地址**:`/auth/roleMapping/listAuthModules/{userId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userId|登录账号|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«授权模块信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«授权模块信息»|CollectionResult«授权模块信息»|
|&emsp;&emsp;data||array|授权模块信息|
|&emsp;&emsp;&emsp;&emsp;moduleId|模块编号|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;title|标题|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"moduleId": 0,
				"title": ""
			}
		]
	}
}
```


## 子账号配置-登录获取账号权限列表


**接口地址**:`/auth/roleMapping/{projectId}/listAuth/{userId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|projectId|path|true|integer(int64)||
|userId|登录账号|path|true|integer(int64)||
|moduleId|moduleId|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«string»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«string»|CollectionResult«string»|
|&emsp;&emsp;data||array|string|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": []
	}
}
```


# 项目配置-成员管理


## V2.2.3 【修改-新增入参】项目配置-项目角色列表


**接口地址**:`/auth/members/v2/roles`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|moduleId|首页模块编号|query|true|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«成员角色下拉列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«成员角色下拉列表»|CollectionResult«成员角色下拉列表»|
|&emsp;&emsp;data||array|成员角色下拉列表|
|&emsp;&emsp;&emsp;&emsp;description|角色描述|string||
|&emsp;&emsp;&emsp;&emsp;roleId|角色id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;roleName|角色名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"description": "",
				"roleId": 0,
				"roleName": ""
			}
		]
	}
}
```


## V2.3.0【修改】项目配置-成员管理-成员列表


**接口地址**:`/auth/projects/{projectId}/members`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|path|true|integer(int64)||
|moduleId|模块编号|query|true|integer(int32)||
|pageNum|页数|query|false|integer(int32)||
|pageSize|分页大小|query|false|integer(int32)||
|userName|成员名称|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«项目成员列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«项目成员列表»|PageResult«项目成员列表»|
|&emsp;&emsp;data||array|项目成员列表|
|&emsp;&emsp;&emsp;&emsp;loginName|成员账号|string||
|&emsp;&emsp;&emsp;&emsp;managerFlag|是否项目负责人标识（0：否，1：是）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;roleIds|成员角色（多个角色逗号分隔）|string||
|&emsp;&emsp;&emsp;&emsp;userId|项目成员id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|成员姓名|string||
|&emsp;&emsp;pageInfo||PageInfo|PageInfo|
|&emsp;&emsp;&emsp;&emsp;currentPage||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;pageSize||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;totalCount||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;totalPage||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"loginName": "",
				"managerFlag": 0,
				"roleIds": "",
				"userId": 0,
				"userName": ""
			}
		],
		"pageInfo": {
			"currentPage": 0,
			"pageSize": 0,
			"totalCount": 0,
			"totalPage": 0
		}
	}
}
```


## 项目配置-成员管理-添加成员


**接口地址**:`/auth/projects/{projectId}/members`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"roleIds": "",
	"userIds": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|memberAddReq|memberAddReq|body|true|添加项目成员|添加项目成员|
|&emsp;&emsp;roleIds|成员角色（多个角色逗号分隔）||false|string||
|&emsp;&emsp;userIds|子账号id（多个子账号逗号分隔）||false|string||
|projectId|项目id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 项目配置-编辑成员列表-新增-不分页查所有


**接口地址**:`/auth/projects/{projectId}/members/list`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«项目成员列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«项目成员列表»|PageResult«项目成员列表»|
|&emsp;&emsp;data||array|项目成员列表|
|&emsp;&emsp;&emsp;&emsp;loginName|成员账号|string||
|&emsp;&emsp;&emsp;&emsp;managerFlag|是否项目负责人标识（0：否，1：是）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;roleIds|成员角色（多个角色逗号分隔）|string||
|&emsp;&emsp;&emsp;&emsp;userId|项目成员id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|成员姓名|string||
|&emsp;&emsp;pageInfo||PageInfo|PageInfo|
|&emsp;&emsp;&emsp;&emsp;currentPage||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;pageSize||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;totalCount||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;totalPage||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"loginName": "",
				"managerFlag": 0,
				"roleIds": "",
				"userId": 0,
				"userName": ""
			}
		],
		"pageInfo": {
			"currentPage": 0,
			"pageSize": 0,
			"totalCount": 0,
			"totalPage": 0
		}
	}
}
```


## 项目配置-成员管理-获取非本项目成员列表


**接口地址**:`/auth/projects/{projectId}/members/notProMembers`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«非本项目成员列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«非本项目成员列表»|CollectionResult«非本项目成员列表»|
|&emsp;&emsp;data||array|非本项目成员列表|
|&emsp;&emsp;&emsp;&emsp;loginName|登录名|string||
|&emsp;&emsp;&emsp;&emsp;userId|子账号id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|子账号姓名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"loginName": "",
				"userId": 0,
				"userName": ""
			}
		]
	}
}
```


## 项目配置-成员管理-修改用户绑定角色【修改】


**接口地址**:`/auth/projects/{projectId}/members/users/{userId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"roleIds": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|memberUpdateReq|memberUpdateReq|body|true|修改成员角色|修改成员角色|
|&emsp;&emsp;roleIds|成员角色（多个角色逗号分隔）||false|string||
|projectId|项目id|path|true|integer(int64)||
|userId|子账号id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```


## 项目配置-成员管理-移出本项目


**接口地址**:`/auth/projects/{projectId}/members/users/{userId}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|path|true|integer(int64)||
|userId|子账号id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«string»»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«string»|ObjectResult«string»|
|&emsp;&emsp;data||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": ""
	}
}
```