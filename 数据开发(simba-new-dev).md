# 测试的描述


**简介**:测试的描述


**HOST**:datasimba-dev-new-svc.test.svc.cluster.local


**联系人**:


**Version**:1.0


**接口路径**:http://test-soul-server.k8s.startdtapi.com/new-dev/v2/api-docs


[TOC]






# 管理中心


## 导出


**接口地址**:`/api/v1/managecenter/export`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|managerCenterIds|managerCenterIds|query|true|array|integer|
|managerCenterId|提交记录id集合|path|true|integer(int64)||


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


## 提交记录列表


**接口地址**:`/api/v1/managecenter/{projectId}/list`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|projectId|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«ManageCenterVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«ManageCenterVo»|PageResult«ManageCenterVo»|
|&emsp;&emsp;data||array|ManageCenterVo|
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
			{}
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


# 任务开发


## V2.4.12 【修改】添加任务（包括离线任务、实时任务、数据科学任务


**接口地址**:`/api/v1/jobs`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"businessFlag": 0,
	"description": "",
	"doubleEnvFlag": false,
	"jobMode": 0,
	"jobType": 0,
	"name": "",
	"periodType": 0,
	"projectId": 0,
	"scheduleResourceId": 0,
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addJob|addJob|body|true|任务新增请求实体（包括离线任务、实时任务、数据科学任务）|任务新增请求实体（包括离线任务、实时任务、数据科学任务）|
|&emsp;&emsp;businessFlag|业务标识（0:离线计算，1:实时计算，2:数据科学）||false|integer(int32)||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;doubleEnvFlag|是否双环境项目||false|boolean||
|&emsp;&emsp;jobMode|实时任务模式（0:可配置模式，1:脚本模式）||false|integer(int32)||
|&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink 8--实时采集||false|integer(int32)||
|&emsp;&emsp;name|任务名称||false|string||
|&emsp;&emsp;periodType|任务周期类型:0--手工任务、1--周期任务||false|integer(int32)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;scheduleResourceId|资源组id||false|integer(int64)||
|&emsp;&emsp;workdirId|工作目录id||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«新增任务响应对象»»|
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
|value||ObjectResult«新增任务响应对象»|ObjectResult«新增任务响应对象»|
|&emsp;&emsp;data||新增任务响应对象|新增任务响应对象|
|&emsp;&emsp;&emsp;&emsp;id|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|任务锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|目录Id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;periodType|任务周期类型:0--手工任务、1--周期任务|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态，true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"id": 0,
			"isLock": 0,
			"jobType": 0,
			"label": "",
			"lockTime": "",
			"locker": "",
			"lockerShow": "",
			"parentId": 0,
			"periodType": 0,
			"publish": false,
			"type": 0
		}
	}
}
```


## 批量同步


**接口地址**:`/api/v1/jobs/batchSync`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"cycleType": 0,
	"dataSourceId": 0,
	"dayCron": {
		"hour": "",
		"minute": ""
	},
	"fieldMappings": [
		{
			"sourceType": "",
			"targetType": ""
		}
	],
	"hourCron": {
		"endHour": "",
		"interval": "",
		"startHour": ""
	},
	"md5": "",
	"minuteCron": {
		"endHour": "",
		"interval": "",
		"startHour": ""
	},
	"monthCron": {
		"hour": "",
		"minute": "",
		"monthDay": []
	},
	"partition": "",
	"projectId": 0,
	"publishFlag": false,
	"tables": [
		{
			"descTable": "",
			"jobName": "",
			"srcTable": "",
			"where": ""
		}
	],
	"weekCron": {
		"hour": "",
		"minute": "",
		"weekDay": []
	},
	"where": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|batchSyncReq|batchSyncReq|body|true|批量数据同步|批量数据同步|
|&emsp;&emsp;cycleType|周期类型   0：天   1：周    2：月   3：分钟    4：小时||false|integer(int32)||
|&emsp;&emsp;dataSourceId|数据源Id||true|integer(int64)||
|&emsp;&emsp;dayCron|天调度表达式||false|DayCron|DayCron|
|&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;fieldMappings|字段映射,源字段为key,目标字段为value||true|array|字段类型映射对应关系|
|&emsp;&emsp;&emsp;&emsp;sourceType|源字段类型||false|string||
|&emsp;&emsp;&emsp;&emsp;targetType|目标字段类型||false|string||
|&emsp;&emsp;hourCron|小时调度表达式||false|HourCron|HourCron|
|&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;md5|||false|string||
|&emsp;&emsp;minuteCron|分钟调度表达式||false|MinuteCron|MinuteCron|
|&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;monthCron|月调度表达式||false|MonthCron|MonthCron|
|&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;monthDay|||false|array|string|
|&emsp;&emsp;partition|分区表达式||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;publishFlag|是否发布,true发布||true|boolean||
|&emsp;&emsp;tables|同步表信息||false|array|批量数据同步表信息|
|&emsp;&emsp;&emsp;&emsp;descTable|||false|string||
|&emsp;&emsp;&emsp;&emsp;jobName|||false|string||
|&emsp;&emsp;&emsp;&emsp;srcTable|||false|string||
|&emsp;&emsp;&emsp;&emsp;where|||false|string||
|&emsp;&emsp;weekCron|周调度表达式||false|WeekCron|WeekCron|
|&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;weekDay|||false|array|string|
|&emsp;&emsp;where|全局过滤条件||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«批量同步响应对象»»|
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
|value||CollectionResult«批量同步响应对象»|CollectionResult«批量同步响应对象»|
|&emsp;&emsp;data||array|批量同步响应对象|
|&emsp;&emsp;&emsp;&emsp;jobName||string||
|&emsp;&emsp;&emsp;&emsp;msg||string||
|&emsp;&emsp;&emsp;&emsp;status||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;table||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"jobName": "",
				"msg": "",
				"status": 0,
				"table": ""
			}
		]
	}
}
```


## 下载运行结果


**接口地址**:`/api/v1/jobs/downloadResult`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|codeMd5|任务运行codeMd5|body|true|String|String|


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


## 获取运行结果


**接口地址**:`/api/v1/jobs/executeResult`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|codeMd5|任务运行codeMd5|body|true|String|String|
|pageNum|页码|query|true|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«Array«string»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«Array«string»»|PageResult«Array«string»»|
|&emsp;&emsp;data||array|array|
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
		"data": [],
		"pageInfo": {
			"currentPage": 0,
			"pageSize": 0,
			"totalCount": 0,
			"totalPage": 0
		}
	}
}
```


## 运行历史


**接口地址**:`/api/v1/jobs/history`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|cycleTime|查询时间周期（0全部时间,1最近24小时,2最近三天,3最近一周|query|false|integer(int32)||
|jobName|任务名|query|false|string||
|runStatus|运行状态（0:等待运行,3:运行中,4:运行成功,5:运行失败,6:已被停止|query|false|integer(int32)||
|pageNum|页数|query|false|integer(int32)||
|pageSize|分页大小|query|false|integer(int32)||
|projectId|项目Id|query|false|integer(int64)||
|sync|是否数据集成|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«运行历史列表»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«运行历史列表»|PageResult«运行历史列表»|
|&emsp;&emsp;data||array|运行历史列表|
|&emsp;&emsp;&emsp;&emsp;code|sql脚本|string||
|&emsp;&emsp;&emsp;&emsp;codeMd5|codeMd5|string||
|&emsp;&emsp;&emsp;&emsp;jobId|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;runStatus|任务运行状态：0 等待运行   3 运行中  4  运行成功 5  运行失败 6 已被停止|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;runtime|运行时间|string(date-time)||
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
				"code": "",
				"codeMd5": "",
				"jobId": 0,
				"jobName": "",
				"runStatus": 0,
				"runtime": ""
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


## 运行详情


**接口地址**:`/api/v1/jobs/history/{codeMd5}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|codeMd5|codeMd5|path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«运行历史详情»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«运行历史详情»|ObjectResult«运行历史详情»|
|&emsp;&emsp;data||运行历史详情|运行历史详情|
|&emsp;&emsp;&emsp;&emsp;code|sql脚本|string||
|&emsp;&emsp;&emsp;&emsp;codeMd5|codeMd5|string||
|&emsp;&emsp;&emsp;&emsp;jobId|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;runStatus|任务运行状态：0 等待运行   3 运行中  4  运行成功 5  运行失败 6 已被停止|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;runtime|运行时间|string(date-time)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"code": "",
			"codeMd5": "",
			"jobId": 0,
			"jobName": "",
			"jobType": 0,
			"runStatus": 0,
			"runtime": ""
		}
	}
}
```


## 运行日志


**接口地址**:`/api/v1/jobs/history/{codeMd5}/log`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|codeMd5|codeMd5|path|true|string||


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


## 日志下载


**接口地址**:`/api/v1/jobs/history/{codeMd5}/log/download`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|codeMd5|codeMd5|path|true|string||


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


## 获取任务历史版本code


**接口地址**:`/api/v1/jobs/version/{id}/code`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|版本id|path|true|integer(int64)||


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


## 获取任务详情


**接口地址**:`/api/v1/jobs/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«获取任务详情响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«获取任务详情响应对象»|ObjectResult«获取任务详情响应对象»|
|&emsp;&emsp;data||获取任务详情响应对象|获取任务详情响应对象|
|&emsp;&emsp;&emsp;&emsp;businessFlag|业务标识（0:离线计算，1:实时计算，2:数据科学）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;envParams|环境参数（目前只有离线任务和数据科学算法任务用到）|string||
|&emsp;&emsp;&emsp;&emsp;id|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobMode|实时任务模式（0:可配置模式，1:脚本模式）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lockTime|任务锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;manager|责任人|string||
|&emsp;&emsp;&emsp;&emsp;managerShow|责任人名称|string||
|&emsp;&emsp;&emsp;&emsp;modifyTime|修改时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;modifyUser|修改人|string||
|&emsp;&emsp;&emsp;&emsp;name|任务名|string||
|&emsp;&emsp;&emsp;&emsp;opFlag|可操作标识，true:可操作，false：不可操作|boolean||
|&emsp;&emsp;&emsp;&emsp;periodType|任务周期类型:0--手工任务、1--周期任务|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;periodTypeString|任务周期类型名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|是否已发布（true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;scheduleResourceId|资源组id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"businessFlag": 0,
			"createTime": "",
			"description": "",
			"envParams": "",
			"id": 0,
			"isLock": 0,
			"jobMode": 0,
			"jobType": 0,
			"lockTime": "",
			"locker": "",
			"lockerShow": "",
			"manager": "",
			"managerShow": "",
			"modifyTime": "",
			"modifyUser": "",
			"name": "",
			"opFlag": false,
			"periodType": 0,
			"periodTypeString": "",
			"publish": false,
			"scheduleResourceId": 0
		}
	}
}
```


## VR2.5.0【修改】保存任务 支持ftp、sftp、oss


**接口地址**:`/api/v1/jobs/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"dataxCode": {
		"columnMappings": [
			{
				"from": "",
				"showDelete": true,
				"to": ""
			}
		],
		"reader": {
			"cat": "",
			"changeColName": [],
			"colChange": true,
			"column": [
				{}
			],
			"compressedType": "",
			"constants": [],
			"dataFileResource": {
				"columnSeparator": "",
				"dataFileName": "",
				"includeMetadata": false,
				"isHa": true,
				"nameNode1": "",
				"nameNode2": "",
				"nullFormat": "",
				"resourceId": 0,
				"resourcePath": ""
			},
			"dataSource": "",
			"dsCode": "",
			"dsName": "",
			"expression": "",
			"fileDataSourceReaderOptionView": {
				"columnSeparator": "",
				"compressedType": "",
				"encryptionType": "",
				"filePaths": [],
				"fileType": "",
				"fileWildcard": "",
				"includeMetadata": false,
				"metadataLocation": "",
				"metadataPath": "",
				"nullFormat": "",
				"partitionFormat": "",
				"secretKey": "",
				"syncModel": ""
			},
			"hbaseReadMode": "",
			"highSetting": "",
			"id": 0,
			"partition": "",
			"pavingData": true,
			"readMode": "",
			"splitPk": "",
			"table": "",
			"type": "",
			"typeString": "",
			"where": ""
		},
		"setting": {
			"channel": 0,
			"record": 0,
			"speedByte": 0
		},
		"writer": {
			"changeColName": [],
			"colChange": true,
			"column": [
				{}
			],
			"dataSource": "",
			"dsCode": "",
			"dsName": "",
			"fileDataSourceWriteOptionView": {
				"columnSeparator": "",
				"compressedType": "",
				"fileName": "",
				"filePath": "",
				"fileType": "",
				"nullFormat": "",
				"writeMetaData": true,
				"writeModel": ""
			},
			"flushMode": "",
			"id": 0,
			"partition": "",
			"postSql": "",
			"preSql": "",
			"rowKeyRule": "",
			"table": "",
			"topic": "",
			"type": "",
			"typeString": "",
			"versionColumnRule": "",
			"writeMode": ""
		}
	},
	"description": "",
	"dimTableInfoList": [
		{
			"columnSql": "",
			"datasourceId": 0,
			"datasourceType": 0,
			"id": 0,
			"mappingTable": "",
			"primaryKey": "",
			"tableName": ""
		}
	],
	"envParams": "",
	"projectId": 0,
	"resultTableInfoList": [
		{
			"columnSql": "",
			"datasourceId": 0,
			"datasourceType": 0,
			"id": 0,
			"mappingTable": "",
			"outputNums": 0,
			"primaryKey": "",
			"tableName": "",
			"timeInterval": 0,
			"updateMode": 0
		}
	],
	"schedule": {
		"custom": 0,
		"cycleType": 0,
		"dayCron": {
			"hour": "",
			"minute": ""
		},
		"hourCron": {
			"endHour": "",
			"interval": "",
			"startHour": ""
		},
		"minuteCron": {
			"endHour": "",
			"interval": "",
			"startHour": ""
		},
		"monthCron": {
			"hour": "",
			"minute": "",
			"monthDay": []
		},
		"preJobIds": "",
		"priority": 0,
		"retry": 0,
		"selfDepend": 0,
		"status": 0,
		"timeOut": 0,
		"weekCron": {
			"hour": "",
			"minute": "",
			"weekDay": []
		}
	},
	"scheduleResourceId": 0,
	"sourceTableInfoList": [
		{
			"columnSql": "",
			"datasourceId": 0,
			"datasourceType": 0,
			"eventTimeField": "",
			"flinkWindow": 0,
			"id": 0,
			"mappingTable": "",
			"maxDelayTime": 0,
			"offsetReset": 0,
			"tableName": ""
		}
	],
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|saveJob|saveJob|body|true|保存任务请求对象（包括离线任务、实时任务、数据科学任务）|保存任务请求对象（包括离线任务、实时任务、数据科学任务）|
|&emsp;&emsp;code|代码||false|string||
|&emsp;&emsp;dataxCode|数据同步datax脚本（目前只有离线任务用到）||false|DataxView|DataxView|
|&emsp;&emsp;&emsp;&emsp;columnMappings|||false|array|ColumnMapping|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;from|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;showDelete|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;to|||false|string||
|&emsp;&emsp;&emsp;&emsp;reader|||false|DataxReaderView|DataxReaderView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;cat|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;changeColName|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colChange|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;column|||false|array|Map«string,object»|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;constants|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataFileResource|数据文件资源详情||false|数据文件资源|数据文件资源|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataFileName|数据文件名称||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;isHa|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nameNode1|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nameNode2|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;resourceId|资源id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;resourcePath|资源路径||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataSource|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsCode|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsName|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;expression|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileDataSourceReaderOptionView|VR2.5.0 新增文件数据源选项,ftp sftp 使用该对象||false|文件数据源选项对象|文件数据源选项对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;encryptionType|加密类型,可用值:none,rsa||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;filePaths|文件路径列表||false|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:csv,txt,orc,rc,seq,parquet||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileWildcard|文件通配符||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;metadataLocation|元数据文件位置,可用值:unknown,none,this_ftp||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;metadataPath|元数据文件路径||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partitionFormat|分区格式||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;secretKey|密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;syncModel|同步模式,可用值:increment_sync_model,full_sync_model||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hbaseReadMode|读取模式 1.normal 2.multi_version_fixed_column,可用值:unknown,normal,multi_version_fixed_column||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;highSetting|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partition|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;pavingData|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;readMode|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;splitPk|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;table|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;where|||false|string||
|&emsp;&emsp;&emsp;&emsp;setting|||false|SettingView|SettingView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;channel|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;record|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;speedByte|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;writer|||false|DataxWriteView|DataxWriteView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;changeColName|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colChange|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;column|||false|array|Map«string,object»|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataSource|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsCode|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsName|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileDataSourceWriteOptionView|VR2.5.0 ftp/sftp 目标数据源保存对象||false|文件数据源保存目标选项对象|文件数据源保存目标选项对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileName|文件名||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;filePath|文件路径||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:csv,txt,orc,rc,seq,parquet||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeMetaData|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeModel|写入模式,可用值:truncate,append||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;flushMode|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partition|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;postSql|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;preSql|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rowKeyRule|rowkeyRule 规则||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;table|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;topic|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;versionColumnRule|版本列规则||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeMode|||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;dimTableInfoList|实时任务维表）||false|array|任务保存-保存实时任务-维表信息请求对象|
|&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql||false|string||
|&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|实时任务源表主键id（新增时传空）||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）||false|string||
|&emsp;&emsp;&emsp;&emsp;primaryKey|主键||false|string||
|&emsp;&emsp;&emsp;&emsp;tableName|表名或kafka主题(源表为kafka主题，维表为kafka主题或表名，结果表为表名)||false|string||
|&emsp;&emsp;envParams|环境参数（目前只有离线任务和数据科学算法任务用到）||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;resultTableInfoList|实时任务结果表）||false|array|任务保存-保存实时任务-结果表信息请求对象|
|&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql||false|string||
|&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|实时任务源表主键id（新增时传空）||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）||false|string||
|&emsp;&emsp;&emsp;&emsp;outputNums|输出数量（条/次）||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;primaryKey|主键||false|string||
|&emsp;&emsp;&emsp;&emsp;tableName|表名或kafka主题(源表为kafka主题，维表为kafka主题或表名，结果表为表名)||false|string||
|&emsp;&emsp;&emsp;&emsp;timeInterval|数据输出时间间隔||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;updateMode|更新模式（0:append,1:overwriter）||false|integer(int32)||
|&emsp;&emsp;schedule|调度周期（目前只有离线任务用到）||false|保存任务-调度周期请求对象（离线任务）|保存任务-调度周期请求对象（离线任务）|
|&emsp;&emsp;&emsp;&emsp;custom|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;cycleType|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;dayCron|||false|DayCron|DayCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;hourCron|||false|HourCron|HourCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;minuteCron|||false|MinuteCron|MinuteCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;monthCron|||false|MonthCron|MonthCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;monthDay|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;preJobIds|||false|string||
|&emsp;&emsp;&emsp;&emsp;priority|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;retry|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;selfDepend|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;status|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeOut|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;weekCron|||false|WeekCron|WeekCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weekDay|||false|array|string|
|&emsp;&emsp;scheduleResourceId|资源组id||false|integer(int64)||
|&emsp;&emsp;sourceTableInfoList|实时任务源表）||false|array|任务保存-保存实时任务-源表信息请求对象|
|&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql||false|string||
|&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;eventTimeField|时间基准列||false|string||
|&emsp;&emsp;&emsp;&emsp;flinkWindow|flink窗口（时间特征 0:eventTime, 1:ProcessingTime）||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|实时任务源表主键id（新增时传空）||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）||false|string||
|&emsp;&emsp;&emsp;&emsp;maxDelayTime|最大延迟时间||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;offsetReset|消费起始点，0:earliest（最旧），1:latest(最新)||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tableName|表名或kafka主题(源表为kafka主题，维表为kafka主题或表名，结果表为表名)||false|string||
|&emsp;&emsp;workdirId|工作目录id||false|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## 删除任务


**接口地址**:`/api/v1/jobs/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0,
	"submitRemark": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|delJobReq|delJobReq|body|true|任务删除请求|任务删除请求|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;submitRemark|提交备注||false|string||
|id|任务id|path|true|integer(int64)||


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


## 自动推荐上游任务


**接口地址**:`/api/v1/jobs/{id}/autoRecommendPreJobs`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|autoRecommend|autoRecommend|body|true|任务推荐上游请求对象|任务推荐上游请求对象|
|&emsp;&emsp;code|code||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|任务id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«自动推荐上游任务信息»»|
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
|value||CollectionResult«自动推荐上游任务信息»|CollectionResult«自动推荐上游任务信息»|
|&emsp;&emsp;data||array|自动推荐上游任务信息|
|&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;manager||string||
|&emsp;&emsp;&emsp;&emsp;managerShow||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;tableName||string||
|&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;userName||string||


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
				"id": 0,
				"manager": "",
				"managerShow": "",
				"name": "",
				"tableName": "",
				"typeString": "",
				"userName": ""
			}
		]
	}
}
```


## 取消任务


**接口地址**:`/api/v1/jobs/{id}/cancel`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"codeMd5": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|cancelJob|cancelJob|body|true|取消任务|取消任务|
|&emsp;&emsp;codeMd5|任务codeMd5值||false|string||
|id|任务id|path|true|integer(int64)||


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


## 任务克隆


**接口地址**:`/api/v1/jobs/{id}/clone`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|cloneJob|cloneJob|body|true|克隆任务|克隆任务|
|&emsp;&emsp;name|任务名称||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|任务id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«任务克隆响应对象»»|
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
|value||ObjectResult«任务克隆响应对象»|ObjectResult«任务克隆响应对象»|
|&emsp;&emsp;data||任务克隆响应对象|任务克隆响应对象|
|&emsp;&emsp;&emsp;&emsp;id|克隆后的任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|任务锁定时间|string||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录Id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;periodType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;periodTypeString|任务类型名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|是否已发布（true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;type|目录类型|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"id": 0,
			"isLock": 0,
			"jobType": 0,
			"label": "",
			"lockTime": "",
			"locker": "",
			"lockerShow": "",
			"parentId": 0,
			"periodType": 0,
			"periodTypeString": "",
			"publish": false,
			"type": 0
		}
	}
}
```


## 获取任务代码


**接口地址**:`/api/v1/jobs/{id}/code`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«获取任务代码响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«获取任务代码响应对象»|ObjectResult«获取任务代码响应对象»|
|&emsp;&emsp;data||获取任务代码响应对象|获取任务代码响应对象|
|&emsp;&emsp;&emsp;&emsp;code|任务代码|string||
|&emsp;&emsp;&emsp;&emsp;dataxCode|数据同步datax脚本（目前只有离线任务用到）|DataxView|DataxView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnMappings||array|ColumnMapping|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;from||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;showDelete||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;to||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;reader||DataxReaderView|DataxReaderView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;cat||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;changeColName||array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colChange||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;column||array|Map«string,object»|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;constants||array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataFileResource|数据文件资源详情|数据文件资源|数据文件资源|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataFileName|数据文件名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;isHa||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nameNode1||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nameNode2||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;resourceId|资源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;resourcePath|资源路径|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataSource||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsCode||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;expression||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileDataSourceReaderOptionView|VR2.5.0 新增文件数据源选项,ftp sftp 使用该对象|文件数据源选项对象|文件数据源选项对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;encryptionType|加密类型,可用值:none,rsa|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;filePaths|文件路径列表|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:csv,txt,orc,rc,seq,parquet|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileWildcard|文件通配符|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;metadataLocation|元数据文件位置,可用值:unknown,none,this_ftp|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;metadataPath|元数据文件路径|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partitionFormat|分区格式|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;secretKey|密钥|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;syncModel|同步模式,可用值:increment_sync_model,full_sync_model|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hbaseReadMode|读取模式 1.normal 2.multi_version_fixed_column,可用值:unknown,normal,multi_version_fixed_column|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;highSetting||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partition||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;pavingData||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;readMode||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;splitPk||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;table||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;where||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;setting||SettingView|SettingView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;channel||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;record||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;speedByte||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writer||DataxWriteView|DataxWriteView|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;changeColName||array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colChange||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;column||array|Map«string,object»|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataSource||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsCode||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dsName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileDataSourceWriteOptionView|VR2.5.0 ftp/sftp 目标数据源保存对象|文件数据源保存目标选项对象|文件数据源保存目标选项对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileName|文件名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;filePath|文件路径|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:csv,txt,orc,rc,seq,parquet|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeMetaData||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeModel|写入模式,可用值:truncate,append|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;flushMode||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;partition||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;postSql||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;preSql||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rowKeyRule|rowkeyRule 规则|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;table||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;topic||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;versionColumnRule|版本列规则|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;writeMode||string||
|&emsp;&emsp;&emsp;&emsp;id|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;name|任务名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"code": "",
			"dataxCode": {
				"columnMappings": [
					{
						"from": "",
						"showDelete": true,
						"to": ""
					}
				],
				"reader": {
					"cat": "",
					"changeColName": [],
					"colChange": true,
					"column": [
						{}
					],
					"compressedType": "",
					"constants": [],
					"dataFileResource": {
						"columnSeparator": "",
						"dataFileName": "",
						"includeMetadata": false,
						"isHa": true,
						"nameNode1": "",
						"nameNode2": "",
						"nullFormat": "",
						"resourceId": 0,
						"resourcePath": ""
					},
					"dataSource": "",
					"dsCode": "",
					"dsName": "",
					"expression": "",
					"fileDataSourceReaderOptionView": {
						"columnSeparator": "",
						"compressedType": "",
						"encryptionType": "",
						"filePaths": [],
						"fileType": "",
						"fileWildcard": "",
						"includeMetadata": false,
						"metadataLocation": "",
						"metadataPath": "",
						"nullFormat": "",
						"partitionFormat": "",
						"secretKey": "",
						"syncModel": ""
					},
					"hbaseReadMode": "",
					"highSetting": "",
					"id": 0,
					"partition": "",
					"pavingData": true,
					"readMode": "",
					"splitPk": "",
					"table": "",
					"type": "",
					"typeString": "",
					"where": ""
				},
				"setting": {
					"channel": 0,
					"record": 0,
					"speedByte": 0
				},
				"writer": {
					"changeColName": [],
					"colChange": true,
					"column": [
						{}
					],
					"dataSource": "",
					"dsCode": "",
					"dsName": "",
					"fileDataSourceWriteOptionView": {
						"columnSeparator": "",
						"compressedType": "",
						"fileName": "",
						"filePath": "",
						"fileType": "",
						"nullFormat": "",
						"writeMetaData": true,
						"writeModel": ""
					},
					"flushMode": "",
					"id": 0,
					"partition": "",
					"postSql": "",
					"preSql": "",
					"rowKeyRule": "",
					"table": "",
					"topic": "",
					"type": "",
					"typeString": "",
					"versionColumnRule": "",
					"writeMode": ""
				}
			},
			"id": 0,
			"jobType": 0,
			"name": ""
		}
	}
}
```


## 获取任务代码Md5值


**接口地址**:`/api/v1/jobs/{id}/codeMd5`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|codeJob|codeJob|body|true|获取任务代码md5值|获取任务代码md5值|
|&emsp;&emsp;code|代码||false|string||


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


## V2.4.12【新增】根据历史任务id获取历史版本源表、维表、结果表信息(实时计算), 暂时未实现


**接口地址**:`/api/v1/jobs/{id}/hisTableInfo`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|历史任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«实时计算获取源表、维表、结果表信息响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«实时计算获取源表、维表、结果表信息响应对象»|ObjectResult«实时计算获取源表、维表、结果表信息响应对象»|
|&emsp;&emsp;data||实时计算获取源表、维表、结果表信息响应对象|实时计算获取源表、维表、结果表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;dimTableInfoList|实时任务维表）|array|任务保存-保存实时任务-维表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务维表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;primaryKey|主键|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||
|&emsp;&emsp;&emsp;&emsp;resultTableInfoList|实时任务结果表）|array|任务保存-保存实时任务-结果表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务结果表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;outputNums|输出数量（条/次）|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;primaryKey|主键|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeInterval|数据输出时间间隔|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateMode|更新模式（0:append,1:overwriter）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;sourceTableInfoList|实时任务源表）|array|任务保存-保存实时任务-源表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;eventTimeField|时间基准列|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;flinkWindow|flink窗口（时间特征 0:eventTime, 1:ProcessingTime）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务源表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;maxDelayTime|最大延迟时间|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;offsetReset|消费起始点，0:earliest（最旧），1:latest(最新)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"dimTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"id": 0,
					"mappingTable": "",
					"primaryKey": "",
					"tableName": ""
				}
			],
			"resultTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"id": 0,
					"mappingTable": "",
					"outputNums": 0,
					"primaryKey": "",
					"tableName": "",
					"timeInterval": 0,
					"updateMode": 0
				}
			],
			"sourceTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"eventTimeField": "",
					"flinkWindow": 0,
					"id": 0,
					"mappingTable": "",
					"maxDelayTime": 0,
					"offsetReset": 0,
					"tableName": ""
				}
			]
		}
	}
}
```


## 获取已发布任务列表


**接口地址**:`/api/v1/jobs/{id}/listPubJobs`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|projectId|projectId|query|true|integer(int64)||
|name|name|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«JobBasePublish»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«JobBasePublish»|CollectionResult«JobBasePublish»|
|&emsp;&emsp;data||array|JobBasePublish|
|&emsp;&emsp;&emsp;&emsp;baselineId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;code||string||
|&emsp;&emsp;&emsp;&emsp;comment||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;&emsp;&emsp;createUser||string||
|&emsp;&emsp;&emsp;&emsp;deleted||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;envParams||string||
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobCategory||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;manager||string||
|&emsp;&emsp;&emsp;&emsp;managerId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;modifyTime||string(date-time)||
|&emsp;&emsp;&emsp;&emsp;modifyUser||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;periodType||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;projectId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;runParams||string||
|&emsp;&emsp;&emsp;&emsp;scheduleResourceId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;scheduleResourceName||string||
|&emsp;&emsp;&emsp;&emsp;type||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"baselineId": 0,
				"code": "",
				"comment": "",
				"createTime": "",
				"createUser": "",
				"deleted": 0,
				"envParams": "",
				"id": 0,
				"jobCategory": 0,
				"jobId": 0,
				"manager": "",
				"managerId": 0,
				"modifyTime": "",
				"modifyUser": "",
				"name": "",
				"periodType": 0,
				"projectId": 0,
				"runParams": "",
				"scheduleResourceId": 0,
				"scheduleResourceName": "",
				"type": 0
			}
		]
	}
}
```


## 任务移动


**接口地址**:`/api/v1/jobs/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|moveJob|moveJob|body|true|移动任务请求对象|移动任务请求对象|
|&emsp;&emsp;parentId|目录Id||false|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## 获取下游任务列表


**接口地址**:`/api/v1/jobs/{id}/nextJobs`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|projectId|projectId|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«NextJobBaseVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«NextJobBaseVo»|CollectionResult«NextJobBaseVo»|
|&emsp;&emsp;data||array|NextJobBaseVo|
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;manager||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;userName||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"id": 0,
				"manager": "",
				"name": "",
				"typeString": "",
				"userName": ""
			}
		]
	}
}
```


## 任务发布


**接口地址**:`/api/v1/jobs/{id}/publish`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"comment": "",
	"cpu": 0,
	"memory": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|publishJob|publishJob|body|true|任务发布请求对象|任务发布请求对象|
|&emsp;&emsp;comment|发布说明||false|string||
|&emsp;&emsp;cpu|cpu（实时计算用）||false|integer(int32)||
|&emsp;&emsp;memory|memory（实时计算用）||false|integer(int32)||
|&emsp;&emsp;projectId|项目ID||false|integer(int64)||
|jobId|任务id|path|true|integer(int64)||


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


## 任务重命名


**接口地址**:`/api/v1/jobs/{id}/rename`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|renameJob|renameJob|body|true|重命名任务请求对象|重命名任务请求对象|
|&emsp;&emsp;name|任务名||false|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## 运行任务


**接口地址**:`/api/v1/jobs/{id}/run`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"codeMd5": "",
	"envParams": "",
	"jobType": 0,
	"parameters": [
		{
			"label": "",
			"value": ""
		}
	],
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|runJob|runJob|body|true|运行任务|运行任务|
|&emsp;&emsp;code|任务code||false|string||
|&emsp;&emsp;codeMd5|任务codeMd5||false|string||
|&emsp;&emsp;envParams|环境参数||false|string||
|&emsp;&emsp;jobType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink 8--实时采集||false|integer(int32)||
|&emsp;&emsp;parameters|运行参数列表（数据科学算法任务使用）||false|array|数据科学算法任务运行参数请求对象|
|&emsp;&emsp;&emsp;&emsp;label|运行参数名||false|string||
|&emsp;&emsp;&emsp;&emsp;value|运行参数值||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## 获取任务调度信息


**接口地址**:`/api/v1/jobs/{id}/schedule`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«JobScheduleVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«JobScheduleVo»|ObjectResult«JobScheduleVo»|
|&emsp;&emsp;data||JobScheduleVo|JobScheduleVo|
|&emsp;&emsp;&emsp;&emsp;cycleType||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;dayCron||DayCron|DayCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute||string||
|&emsp;&emsp;&emsp;&emsp;hourCron||HourCron|HourCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour||string||
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;minuteCron||MinuteCron|MinuteCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour||string||
|&emsp;&emsp;&emsp;&emsp;monthCron||MonthCron|MonthCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;monthDay||array|string|
|&emsp;&emsp;&emsp;&emsp;preJobScheduleRes||array|上游任务信息|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;manager||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;managerShow||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;userName||string||
|&emsp;&emsp;&emsp;&emsp;priority||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;retry||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;scheduleResourceId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;scheduleResourceName||string||
|&emsp;&emsp;&emsp;&emsp;selfDepend||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;weekCron||WeekCron|WeekCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weekDay||array|string|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"cycleType": 0,
			"dayCron": {
				"hour": "",
				"minute": ""
			},
			"hourCron": {
				"endHour": "",
				"interval": "",
				"startHour": ""
			},
			"id": 0,
			"jobId": 0,
			"minuteCron": {
				"endHour": "",
				"interval": "",
				"startHour": ""
			},
			"monthCron": {
				"hour": "",
				"minute": "",
				"monthDay": []
			},
			"preJobScheduleRes": [
				{
					"id": 0,
					"manager": "",
					"managerShow": "",
					"name": "",
					"type": 0,
					"typeString": "",
					"userName": ""
				}
			],
			"priority": 0,
			"retry": 0,
			"scheduleResourceId": 0,
			"scheduleResourceName": "",
			"selfDepend": 0,
			"weekCron": {
				"hour": "",
				"minute": "",
				"weekDay": []
			}
		}
	}
}
```


## 保存任务调度信息


**接口地址**:`/api/v1/jobs/{id}/schedule`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0,
	"saveJobSchedule": {
		"custom": 0,
		"cycleType": 0,
		"dayCron": {
			"hour": "",
			"minute": ""
		},
		"hourCron": {
			"endHour": "",
			"interval": "",
			"startHour": ""
		},
		"minuteCron": {
			"endHour": "",
			"interval": "",
			"startHour": ""
		},
		"monthCron": {
			"hour": "",
			"minute": "",
			"monthDay": []
		},
		"preJobIds": "",
		"priority": 0,
		"retry": 0,
		"selfDepend": 0,
		"status": 0,
		"timeOut": 0,
		"weekCron": {
			"hour": "",
			"minute": "",
			"weekDay": []
		}
	}
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|tagSaveJobSchedule|tagSaveJobSchedule|body|true|保存任务-调度周期请求对象（离线任务）(标签)|保存任务-调度周期请求对象（离线任务）(标签)|
|&emsp;&emsp;projectId|||false|integer(int64)||
|&emsp;&emsp;saveJobSchedule|||false|保存任务-调度周期请求对象（离线任务）|保存任务-调度周期请求对象（离线任务）|
|&emsp;&emsp;&emsp;&emsp;custom|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;cycleType|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;dayCron|||false|DayCron|DayCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;hourCron|||false|HourCron|HourCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;minuteCron|||false|MinuteCron|MinuteCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;endHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;interval|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;startHour|||false|string||
|&emsp;&emsp;&emsp;&emsp;monthCron|||false|MonthCron|MonthCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;monthDay|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;preJobIds|||false|string||
|&emsp;&emsp;&emsp;&emsp;priority|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;retry|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;selfDepend|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;status|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeOut|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;weekCron|||false|WeekCron|WeekCron|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weekDay|||false|array|string|


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


## 智能ide


**接口地址**:`/api/v1/jobs/{id}/smartide/info`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«智能ide信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«智能ide信息»|ObjectResult«智能ide信息»|
|&emsp;&emsp;data||智能ide信息|智能ide信息|
|&emsp;&emsp;&emsp;&emsp;functions||array|string|
|&emsp;&emsp;&emsp;&emsp;tables||array|SmartIdeTableVO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columns||array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;text||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"functions": [],
			"tables": [
				{
					"columns": [],
					"text": ""
				}
			]
		}
	}
}
```


## V2.4.12 【新增】 配置模式切换为脚本模式


**接口地址**:`/api/v1/jobs/{id}/switch`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"jobMode": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|switchFlinkJob|switchFlinkJob|body|true|配置模式/脚本模式切换|配置模式/脚本模式切换|
|&emsp;&emsp;jobMode|目标实时任务模式（0:可配置模式，1:脚本模式）||false|integer(int32)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## V2.4.12【新增】根据任务id获取源表、维表、结果表信息(实时计算)


**接口地址**:`/api/v1/jobs/{id}/tableInfo`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|jobId|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«实时计算获取源表、维表、结果表信息响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«实时计算获取源表、维表、结果表信息响应对象»|ObjectResult«实时计算获取源表、维表、结果表信息响应对象»|
|&emsp;&emsp;data||实时计算获取源表、维表、结果表信息响应对象|实时计算获取源表、维表、结果表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;dimTableInfoList|实时任务维表）|array|任务保存-保存实时任务-维表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务维表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;primaryKey|主键|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||
|&emsp;&emsp;&emsp;&emsp;resultTableInfoList|实时任务结果表）|array|任务保存-保存实时任务-结果表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务结果表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;outputNums|输出数量（条/次）|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;primaryKey|主键|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeInterval|数据输出时间间隔|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateMode|更新模式（0:append,1:overwriter）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;sourceTableInfoList|实时任务源表）|array|任务保存-保存实时任务-源表信息响应对象|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;columnSql|建表字段sql|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceId|数据源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;datasourceType|数据源类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;eventTimeField|时间基准列|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;flinkWindow|flink窗口（时间特征 0:eventTime, 1:ProcessingTime）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|实时任务源表主键id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mappingTable|映射表（源表名）|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;maxDelayTime|最大延迟时间|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;offsetReset|消费起始点，0:earliest（最旧），1:latest(最新)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableName|数据表或kafka主题|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"dimTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"id": 0,
					"mappingTable": "",
					"primaryKey": "",
					"tableName": ""
				}
			],
			"resultTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"id": 0,
					"mappingTable": "",
					"outputNums": 0,
					"primaryKey": "",
					"tableName": "",
					"timeInterval": 0,
					"updateMode": 0
				}
			],
			"sourceTableInfoList": [
				{
					"columnSql": "",
					"datasourceId": 0,
					"datasourceType": 0,
					"eventTimeField": "",
					"flinkWindow": 0,
					"id": 0,
					"mappingTable": "",
					"maxDelayTime": 0,
					"offsetReset": 0,
					"tableName": ""
				}
			]
		}
	}
}
```


## 表结构信息


**接口地址**:`/api/v1/jobs/{id}/tableMeta`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"asTarget": false,
	"projectId": 0,
	"source": {
		"columnSeparator": "",
		"compressedType": "",
		"encryptionType": "",
		"filePaths": [],
		"fileType": "",
		"fileWildcard": "",
		"filterData": "",
		"hdfsAddress": "",
		"id": 0,
		"includeMetadata": false,
		"inputJSON": "",
		"localDataResource": true,
		"metadataLocation": "",
		"metadataPath": "",
		"nullFormat": "",
		"ossObjectPrefix": "",
		"paramSettings": "",
		"partitionFormat": "",
		"readModel": "",
		"readType": 0,
		"resourceId": 0,
		"secretKey": "",
		"tableName": [],
		"where": ""
	},
	"target": {
		"columnSeparator": "",
		"compressedType": "",
		"encryptionType": "",
		"filePaths": [],
		"fileType": "",
		"fileWildcard": "",
		"filterData": "",
		"hdfsAddress": "",
		"id": 0,
		"includeMetadata": false,
		"inputJSON": "",
		"metadataLocation": "",
		"metadataPath": "",
		"nullFormat": "",
		"ossObjectPrefix": "",
		"paramSettings": "",
		"partitionFormat": "",
		"readModel": "",
		"readType": 0,
		"secretKey": "",
		"tableName": "",
		"where": ""
	}
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sourceAndTarget|sourceAndTarget|body|true|创建任务时用于获取字段映射的来源及目标信息|创建任务时用于获取字段映射的来源及目标信息|
|&emsp;&emsp;asTarget|是否指定目的地||true|boolean||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;source|来源对象||true|创建任务时用于获取字段映射的来源信息|创建任务时用于获取字段映射的来源信息|
|&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符||false|string||
|&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2||false|string||
|&emsp;&emsp;&emsp;&emsp;encryptionType|加密类型,可用值:none,rsa||false|string||
|&emsp;&emsp;&emsp;&emsp;filePaths|文件路径||false|array|string|
|&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:unknown,none,csv,txt,可用值:csv,txt,orc,rc,seq,parquet||false|string||
|&emsp;&emsp;&emsp;&emsp;fileWildcard|文件通配符||false|string||
|&emsp;&emsp;&emsp;&emsp;filterData|HBase数据过滤||false|string||
|&emsp;&emsp;&emsp;&emsp;hdfsAddress|HDFS地址||false|string||
|&emsp;&emsp;&emsp;&emsp;id|数据源id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据||false|boolean||
|&emsp;&emsp;&emsp;&emsp;inputJSON|json数据||false|string||
|&emsp;&emsp;&emsp;&emsp;localDataResource|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;metadataLocation|元数据文件位置,可用值:unknown,none,this_ftp||false|string||
|&emsp;&emsp;&emsp;&emsp;metadataPath|元数据文件路径||false|string||
|&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat||false|string||
|&emsp;&emsp;&emsp;&emsp;ossObjectPrefix|OSS对象前缀||false|string||
|&emsp;&emsp;&emsp;&emsp;paramSettings|高级配置参数||false|string||
|&emsp;&emsp;&emsp;&emsp;partitionFormat|分区格式||false|string||
|&emsp;&emsp;&emsp;&emsp;readModel|HBase读取模式 1.normal 2.multi_version_fixed_column,可用值:unknown,normal,multi_version_fixed_column||false|string||
|&emsp;&emsp;&emsp;&emsp;readType|couchbase 字段属性读取方式||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;resourceId|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;secretKey|密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;tableName|表名||false|array|string|
|&emsp;&emsp;&emsp;&emsp;where|查询条件||false|string||
|&emsp;&emsp;target|目标对象||false|创建任务时用于获取字段映射的目标信息|创建任务时用于获取字段映射的目标信息|
|&emsp;&emsp;&emsp;&emsp;columnSeparator|列分隔符||false|string||
|&emsp;&emsp;&emsp;&emsp;compressedType|压缩类型,可用值:none,zip,gzip,bzip2||false|string||
|&emsp;&emsp;&emsp;&emsp;encryptionType|加密类型,可用值:none,rsa||false|string||
|&emsp;&emsp;&emsp;&emsp;filePaths|文件路径||false|array|string|
|&emsp;&emsp;&emsp;&emsp;fileType|文件类型,可用值:unknown,none,csv,txt,可用值:csv,txt,orc,rc,seq,parquet||false|string||
|&emsp;&emsp;&emsp;&emsp;fileWildcard|文件通配符||false|string||
|&emsp;&emsp;&emsp;&emsp;filterData|HBase数据过滤||false|string||
|&emsp;&emsp;&emsp;&emsp;hdfsAddress|HDFS地址||false|string||
|&emsp;&emsp;&emsp;&emsp;id|数据源id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;includeMetadata|是否包含元数据||false|boolean||
|&emsp;&emsp;&emsp;&emsp;inputJSON|json数据||false|string||
|&emsp;&emsp;&emsp;&emsp;metadataLocation|元数据文件位置,可用值:unknown,none,this_ftp||false|string||
|&emsp;&emsp;&emsp;&emsp;metadataPath|元数据文件路径||false|string||
|&emsp;&emsp;&emsp;&emsp;nullFormat|nullFormat||false|string||
|&emsp;&emsp;&emsp;&emsp;ossObjectPrefix|OSS对象前缀||false|string||
|&emsp;&emsp;&emsp;&emsp;paramSettings|高级配置参数||false|string||
|&emsp;&emsp;&emsp;&emsp;partitionFormat|分区格式||false|string||
|&emsp;&emsp;&emsp;&emsp;readModel|HBase读取模式 1.normal 2.multi_version_fixed_column,可用值:unknown,normal,multi_version_fixed_column||false|string||
|&emsp;&emsp;&emsp;&emsp;readType|couchbase 字段属性读取方式||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;secretKey|密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;tableName|表名||false|string||
|&emsp;&emsp;&emsp;&emsp;where|查询条件||false|string||
|id|任务id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«表信息»»|
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
|value||ObjectResult«表信息»|ObjectResult«表信息»|
|&emsp;&emsp;data||表信息|表信息|
|&emsp;&emsp;&emsp;&emsp;columns|字段集合列表|array|TableCol|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colType||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colTypeInt||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;comment||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;index||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;ifPt|是否分区|boolean||
|&emsp;&emsp;&emsp;&emsp;pts|分区信息|array|string|
|&emsp;&emsp;&emsp;&emsp;splitPk||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"columns": [
				{
					"colName": "",
					"colType": "",
					"colTypeInt": 0,
					"comment": "",
					"index": 0
				}
			],
			"ifPt": false,
			"pts": [],
			"splitPk": ""
		}
	}
}
```


## 解锁任务


**接口地址**:`/api/v1/jobs/{id}/unlock`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|baseReq|删除请求基础对象|body|true|BaseReq|BaseReq|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|id|任务id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«解锁任务响应对象»»|
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
|value||ObjectResult«解锁任务响应对象»|ObjectResult«解锁任务响应对象»|
|&emsp;&emsp;data||解锁任务响应对象|解锁任务响应对象|
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lockTime|任务锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"entityId": 0,
			"isLock": 0,
			"lockTime": "",
			"locker": 0,
			"lockerShow": ""
		}
	}
}
```


## 获取任务历史版本


**接口地址**:`/api/v1/jobs/{id}/versions`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|任务id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«获取任务发布历史版本响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«获取任务发布历史版本响应对象»|CollectionResult«获取任务发布历史版本响应对象»|
|&emsp;&emsp;data||array|获取任务发布历史版本响应对象|
|&emsp;&emsp;&emsp;&emsp;comment|发布说明|string||
|&emsp;&emsp;&emsp;&emsp;commitTime|发布时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;commitUser|提交者|string||
|&emsp;&emsp;&emsp;&emsp;id|发布历史id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobId|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|提交者名称|string||
|&emsp;&emsp;&emsp;&emsp;version|发布版本|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"comment": "",
				"commitTime": "",
				"commitUser": "",
				"id": 0,
				"jobId": 0,
				"userName": "",
				"version": 0
			}
		]
	}
}
```


# 资源管理-目录


## 新增目录


**接口地址**:`/api/v1/jobs/resource/dir`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"parentId": 0,
	"projectId": 0,
	"sync": false
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addDirReq|增加目录请求对象|body|true|AddDevDir|AddDevDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;parentId|父目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;sync|是否为同步目录(默认为否)||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«AddDevDirVo»»|
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
|value||ObjectResult«AddDevDirVo»|ObjectResult«AddDevDirVo»|
|&emsp;&emsp;data||AddDevDirVo|AddDevDirVo|
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 资源目录及资源树


**接口地址**:`/api/v1/jobs/resource/dir/resourceTree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«ResourceTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«ResourceTreeVo»|CollectionResult«ResourceTreeVo»|
|&emsp;&emsp;data||array|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


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
						"children": [
							{}
						],
						"id": 0,
						"label": "",
						"parentId": 0,
						"type": 0
					}
				],
				"id": 0,
				"label": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 目录


**接口地址**:`/api/v1/jobs/resource/dir/tree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«DirTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«DirTreeVo»|CollectionResult«DirTreeVo»|
|&emsp;&emsp;data||array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|children|array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|lable|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


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
						"children": [
							{}
						],
						"id": 0,
						"label": "",
						"parentId": 0,
						"type": 0
					}
				],
				"id": 0,
				"label": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 目录删除


**接口地址**:`/api/v1/jobs/resource/dir/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|baseReq|删除请求基础对象|body|true|BaseReq|BaseReq|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


## 目录移动


**接口地址**:`/api/v1/jobs/resource/dir/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|optDirReq|目录移动请求对象|body|true|OptDevDir|OptDevDir|
|&emsp;&emsp;parentId|父目录id或目标目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«ResourceTreeVo»»|
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
|value||ObjectResult«ResourceTreeVo»|ObjectResult«ResourceTreeVo»|
|&emsp;&emsp;data||ResourceTreeVo|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"children": [
				{
					"children": [
						{}
					],
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 目录重命名


**接口地址**:`/api/v1/jobs/resource/dir/{id}/rename`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|renameDir|目录重命名请求对象|body|true|RenameDir|RenameDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


# 算法中心-集成开发平台


## 新增算法任务


**接口地址**:`/datascience/job/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"description": "",
	"jobType": 0,
	"name": "",
	"periodType": 0,
	"projectId": 0,
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addJobReq|addJobReq|body|true|新增算法任务请求对象|新增算法任务请求对象|
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;jobType|任务类型4--python、6--PY_SPARK||false|integer(int32)||
|&emsp;&emsp;name|任务名称||false|string||
|&emsp;&emsp;periodType|任务周期类型:0--手工任务、1--周期任务||false|integer(int32)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;workdirId|目录id||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«数据科学新增算法任务响应对象»»|
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
|value||ObjectResult«数据科学新增算法任务响应对象»|ObjectResult«数据科学新增算法任务响应对象»|
|&emsp;&emsp;data||数据科学新增算法任务响应对象|数据科学新增算法任务响应对象|
|&emsp;&emsp;&emsp;&emsp;fileType|类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否被锁定, 0:否 1:是|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobId|任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型4--python、6--PY_SPARK|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lockTime|锁定时间|string||
|&emsp;&emsp;&emsp;&emsp;locker|锁定人用户名|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;name|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;periodType|任务周期类型:0--手工任务、1--周期任务|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"fileType": 0,
			"isLock": 0,
			"jobId": 0,
			"jobType": 0,
			"lockTime": "",
			"locker": "",
			"lockerShow": "",
			"name": "",
			"parentId": 0,
			"periodType": 0
		}
	}
}
```


## 运行任务


**接口地址**:`/datascience/job/run`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"code": "",
	"codeMd5": "",
	"envParams": "",
	"jobId": 0,
	"jobType": 0,
	"parameters": [
		{
			"label": "",
			"value": ""
		}
	],
	"projectId": 0,
	"type": 0,
	"userId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|runJobReq|runJobReq|body|true|RunJobReq|RunJobReq|
|&emsp;&emsp;code|||false|string||
|&emsp;&emsp;codeMd5|||false|string||
|&emsp;&emsp;envParams|||false|string||
|&emsp;&emsp;jobId|||false|integer(int64)||
|&emsp;&emsp;jobType|||false|integer(int32)||
|&emsp;&emsp;parameters|||false|array|数据科学算法任务运行参数请求对象|
|&emsp;&emsp;&emsp;&emsp;label|运行参数名||false|string||
|&emsp;&emsp;&emsp;&emsp;value|运行参数值||false|string||
|&emsp;&emsp;projectId|||false|integer(int64)||
|&emsp;&emsp;type|||false|integer(int32)||
|&emsp;&emsp;userId|||false|integer(int64)||


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


# 资源管理


## 模糊查询资源列表


**接口地址**:`/api/v1/jobs/resource`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|name|资源名称（为空则查询项目下全部资源）|query|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«下拉列表框响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«下拉列表框响应对象»|CollectionResult«下拉列表框响应对象»|
|&emsp;&emsp;data||array|下拉列表框响应对象|
|&emsp;&emsp;&emsp;&emsp;label|名称|string||
|&emsp;&emsp;&emsp;&emsp;value|值|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": ""
			}
		]
	}
}
```


## 资源数据文件上传


**接口地址**:`/api/v1/jobs/resource`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|workdirId|目录id|query|false|integer(int64)||
|projectId|项目id|query|false|integer(int64)||
|name|资源名称|query|false|string||
|resourceType|资源类型(0 jar，1 file，2 archive)|query|false|integer(int32)||
|description|描述|query|false|string||
|businessFlag|业务标识（0:离线计算，1:实时计算，2:数据科学 3: 项目管理-数据文件）|query|false|integer(int32)||
|submitRemark|提交备注|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«ResourceTreeVo»»|
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
|value||ObjectResult«ResourceTreeVo»|ObjectResult«ResourceTreeVo»|
|&emsp;&emsp;data||ResourceTreeVo|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"children": [
				{
					"children": [
						{}
					],
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 资源列表下拉


**接口地址**:`/api/v1/jobs/resource/resources`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|name|资源名称（为空则查询项目下全部资源）|query|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«资源labelvo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«资源labelvo»|CollectionResult«资源labelvo»|
|&emsp;&emsp;data||array|资源labelvo|
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;name||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"id": 0,
				"name": ""
			}
		]
	}
}
```


## 查询资源文件的详细信息


**接口地址**:`/api/v1/jobs/resource/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|资源id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«获取资源详情响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«获取资源详情响应对象»|ObjectResult«获取资源详情响应对象»|
|&emsp;&emsp;data||获取资源详情响应对象|获取资源详情响应对象|
|&emsp;&emsp;&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;createUser|创建人|string||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;modifyTime|修改时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;modifyUser|修改人|string||
|&emsp;&emsp;&emsp;&emsp;name|资源名称|string||
|&emsp;&emsp;&emsp;&emsp;typeString|资源类型名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"createTime": "",
			"createUser": "",
			"description": "",
			"id": 0,
			"modifyTime": "",
			"modifyUser": "",
			"name": "",
			"typeString": ""
		}
	}
}
```


## 删除资源文件


**接口地址**:`/api/v1/jobs/resource/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0,
	"submitRemark": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|delResource|删除资源请求对象|body|true|DelResource|DelResource|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;submitRemark|提交备注||true|string||
|id|资源id|path|true|integer(int64)||


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


## 资源文件下载


**接口地址**:`/api/v1/jobs/resource/{id}/download`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|资源id|path|true|integer(int64)||
|projectId|projectId|query|false|integer(int64)||


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


## 移动资源文件


**接口地址**:`/api/v1/jobs/resource/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|moveResourceFile|moveResourceFile|body|true|移动资源文件请求对象|移动资源文件请求对象|
|&emsp;&emsp;parentId|目标目录id||false|integer(int64)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|资源id|path|true|integer(int64)||


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


## 提交/发布资源到发布管理中心


**接口地址**:`/api/v1/jobs/resource/{id}/submit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|projectId|query|true|integer(int64)||
|id|任务id|path|true|integer(int64)||
|remark|remark|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«long»»|
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
|value||ObjectResult«long»|ObjectResult«long»|
|&emsp;&emsp;data||integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": 0
	}
}
```


# 发布管理


## 发布包列表


**接口地址**:`/api/v1/publishing/packages`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|true|integer(int32)||
|pageSize|分页大小|query|true|integer(int32)||
|projectId|项目Id|query|true|integer(int64)||
|name|发布包名称(未传表示全部)|query|false|string||
|creator|创建人(未传表示全部)|query|false|string||
|minCreatingTime|最小创建时间(闭区间。格式为yyyy-MM-dd。未传表示历史)|query|false|string||
|maxCreatingTime|最大创建时间(闭区间。格式为yyyy-MM-dd。未传表示今日)|query|false|string||
|publishingState|发布状态(取值参考接口返回值。未传表示全部)|query|false|ref||
|publisher|发布人(未传表示全部)|query|false|string||
|minPublishingTime|最小发布时间(闭区间。格式为yyyy-MM-dd。未传表示历史)|query|false|string||
|maxPublishingTime|最大发布时间(闭区间。格式为yyyy-MM-dd。未传表示全部已发布的发布包)|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«发布包»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«发布包»|PageResult«发布包»|
|&emsp;&emsp;data||array|发布包|
|&emsp;&emsp;&emsp;&emsp;creatingTime|创建时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;creator|创建人|string||
|&emsp;&emsp;&emsp;&emsp;creatorName|创建人名称|string||
|&emsp;&emsp;&emsp;&emsp;id|发布包id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;name|发布包名称|string||
|&emsp;&emsp;&emsp;&emsp;publishedTargetCount|发布成功对象数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;publisher|发布人|string||
|&emsp;&emsp;&emsp;&emsp;publisherName|发布人名称|string||
|&emsp;&emsp;&emsp;&emsp;publishingState|发布状态 (1:成功; 2:失败; 3:待发布; 4:发布中)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;publishingTime|发布时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;totalTargetCount|总对象数|integer(int32)||
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
				"creatingTime": "",
				"creator": "",
				"creatorName": "",
				"id": 0,
				"name": "",
				"publishedTargetCount": 0,
				"publisher": "",
				"publisherName": "",
				"publishingState": 0,
				"publishingTime": "",
				"totalTargetCount": 0
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


## 创建发布包


**接口地址**:`/api/v1/publishing/packages`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"ids": "",
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createPublishingPackage|createPublishingPackage|body|true|创建发布包|创建发布包|
|&emsp;&emsp;ids|任务列表||false|string||
|&emsp;&emsp;name|发布包名称||false|string||
|&emsp;&emsp;projectId|项目ID||false|integer(int64)||


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


## 批量发布


**接口地址**:`/api/v1/publishing/packages/publish`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"ids": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|idCollection|idCollection|body|true|ID列表|ID列表|
|&emsp;&emsp;ids|ID列表||false|string||


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


## 发布包详情


**接口地址**:`/api/v1/publishing/packages/{packageId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|true|integer(int32)||
|pageSize|分页大小|query|true|integer(int32)||
|packageId|发布包Id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«待发布对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«待发布对象»|PageResult«待发布对象»|
|&emsp;&emsp;data||array|待发布对象|
|&emsp;&emsp;&emsp;&emsp;id|待发布对象ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;nature|属性(1:实体对象，2:标签对象，3:离线对象)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;operationType|变更类型(1:新增，2:更新，3:删除)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;requestTime|提交时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;requester|提交人|string||
|&emsp;&emsp;&emsp;&emsp;requesterName|提交人名称|string||
|&emsp;&emsp;&emsp;&emsp;state|发布状态(取值参考发布包)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;type|类型 (0:hive-sql; 1:shell; 2:数据同步; 3:spark-sql; 4:python; 5:虚任务; 6:pyspark; 7:flink; 100:数据层级; 101:数据域; 102:业务过程; 103:规范建表;104:离线资源;105:离线函数)|integer(int32)||
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
				"id": 0,
				"name": "",
				"nature": 0,
				"operationType": 0,
				"requestTime": "",
				"requester": "",
				"requesterName": "",
				"state": 0,
				"type": 0
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


## 待发布对象列表


**接口地址**:`/api/v1/publishing/targets`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|true|integer(int32)||
|pageSize|分页大小|query|true|integer(int32)||
|projectId|项目Id|query|true|integer(int64)||
|name|对象名称(未传表示全部)|query|false|string||
|requester|提交人(未传表示全部)|query|false|string||
|minRequestTime|最小提交时间(闭区间。格式为yyyy-MM-dd。未传表示今日)|query|false|string||
|maxRequestTime|最大提交时间(闭区间。格式为yyyy-MM-dd。未传表示今日)|query|false|string||
|nature|属性(取值参考接口返回值。未传表示全部)|query|false|ref||
|type|类型(取值参考接口返回值。未传表示全部)|query|false|ref||
|operationType|变更类型(取值参考接口返回值。未传表示全部)|query|false|ref||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«待发布对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«待发布对象»|PageResult«待发布对象»|
|&emsp;&emsp;data||array|待发布对象|
|&emsp;&emsp;&emsp;&emsp;id|待发布对象ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;nature|属性(1:实体对象，2:标签对象，3:离线对象)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;operationType|变更类型(1:新增，2:更新，3:删除)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;requestTime|提交时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;requester|提交人|string||
|&emsp;&emsp;&emsp;&emsp;requesterName|提交人名称|string||
|&emsp;&emsp;&emsp;&emsp;state|发布状态(取值参考发布包)|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;type|类型 (0:hive-sql; 1:shell; 2:数据同步; 3:spark-sql; 4:python; 5:虚任务; 6:pyspark; 7:flink; 100:数据层级; 101:数据域; 102:业务过程; 103:规范建表;104:离线资源;105:离线函数)|integer(int32)||
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
				"id": 0,
				"name": "",
				"nature": 0,
				"operationType": 0,
				"requestTime": "",
				"requester": "",
				"requesterName": "",
				"state": 0,
				"type": 0
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


# 数据文件


## [数据集成二期] 数据集成上传资源


**接口地址**:`/api/v1/resource/batchUpload`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|files|files|query|true|array|file|
|projectId|projectId|body|false|integer||
|businessFlag|businessFlag|body|false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«long»»|
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
|value||ObjectResult«long»|ObjectResult«long»|
|&emsp;&emsp;data||integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": 0
	}
}
```


## [数据集成二期] 数据文件列表(分页)


**接口地址**:`/api/v1/resource/datafile`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|false|integer(int32)||
|pageSize|分页大小|query|false|integer(int32)||
|projectId|项目id|query|false|integer(int32)||
|fileName|文件名称|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«数据文件详情»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«数据文件详情»|PageResult«数据文件详情»|
|&emsp;&emsp;data||array|数据文件详情|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;fileName|文件名称|string||
|&emsp;&emsp;&emsp;&emsp;opsUserName|操作人|string||
|&emsp;&emsp;&emsp;&emsp;projectId|项目id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;resourceId|数据文件资源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;uploadTime|上传时间|string||
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
				"description": "",
				"fileName": "",
				"opsUserName": "",
				"projectId": 0,
				"resourceId": 0,
				"uploadTime": ""
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


## [数据集成二期] 数据文件列表


**接口地址**:`/api/v1/resource/list`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|false|integer(int64)||
|fileName|查询字符|query|false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«数据文件详情»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«数据文件详情»|CollectionResult«数据文件详情»|
|&emsp;&emsp;data||array|数据文件详情|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;fileName|文件名称|string||
|&emsp;&emsp;&emsp;&emsp;opsUserName|操作人|string||
|&emsp;&emsp;&emsp;&emsp;projectId|项目id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;resourceId|数据文件资源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;uploadTime|上传时间|string||


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
				"fileName": "",
				"opsUserName": "",
				"projectId": 0,
				"resourceId": 0,
				"uploadTime": ""
			}
		]
	}
}
```


## [数据集成二期] 数据文件详情


**接口地址**:`/api/v1/resource/{resourceId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|resourceId|数据文件id|path|false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«数据文件详情»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«数据文件详情»|ObjectResult«数据文件详情»|
|&emsp;&emsp;data||数据文件详情|数据文件详情|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;fileName|文件名称|string||
|&emsp;&emsp;&emsp;&emsp;opsUserName|操作人|string||
|&emsp;&emsp;&emsp;&emsp;projectId|项目id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;resourceId|数据文件资源id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;uploadTime|上传时间|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"description": "",
			"fileName": "",
			"opsUserName": "",
			"projectId": 0,
			"resourceId": 0,
			"uploadTime": ""
		}
	}
}
```


## [数据集成二期] 数据文件保存


**接口地址**:`/api/v1/resource/{resourceId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"description": "",
	"fileName": "",
	"opsUserName": "",
	"projectId": 0,
	"resourceId": 0,
	"uploadTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dataFileResourcesVo|dataFileResourcesVo|body|true|数据文件详情|数据文件详情|
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;fileName|文件名称||false|string||
|&emsp;&emsp;opsUserName|操作人||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;resourceId|数据文件资源id||false|integer(int64)||
|&emsp;&emsp;uploadTime|上传时间||false|string||
|resourceId|数据文件id|path|false|integer(int64)||


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


## [数据集成二期] 数据文件删除


**接口地址**:`/api/v1/resource/{resourceId}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|resourceId|数据文件id|path|false|integer(int64)||


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


# 函数管理-目录


## 新增目录


**接口地址**:`/api/v1/jobs/function/dir`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"parentId": 0,
	"projectId": 0,
	"sync": false
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addDirReq|增加目录请求对象|body|true|AddDevDir|AddDevDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;parentId|父目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;sync|是否为同步目录(默认为否)||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«AddFuncDirVo»»|
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
|value||ObjectResult«AddFuncDirVo»|ObjectResult«AddFuncDirVo»|
|&emsp;&emsp;data||AddFuncDirVo|AddFuncDirVo|
|&emsp;&emsp;&emsp;&emsp;funcType|函数目录类型（0 系统函数,1 自定义函数）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"funcType": 0,
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 函数及目录树


**接口地址**:`/api/v1/jobs/function/dir/funcTree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«FuncTreeListVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«FuncTreeListVo»|ObjectResult«FuncTreeListVo»|
|&emsp;&emsp;data||FuncTreeListVo|FuncTreeListVo|
|&emsp;&emsp;&emsp;&emsp;customData|自定义函数|array|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;children|子目录|array|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;funcType|函数类型:0 系统函数,1 自定义函数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;systemData|系统函数|array|FuncTreeVo|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"customData": [
				{
					"children": [
						{
							"children": [
								{}
							],
							"funcType": 0,
							"id": 0,
							"label": "",
							"parentId": 0,
							"type": 0
						}
					],
					"funcType": 0,
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"systemData": [
				{
					"children": [
						{
							"children": [
								{}
							],
							"funcType": 0,
							"id": 0,
							"label": "",
							"parentId": 0,
							"type": 0
						}
					],
					"funcType": 0,
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			]
		}
	}
}
```


## 函数及目录树


**接口地址**:`/api/v1/jobs/function/dir/functionTree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«FuncTreeListVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«FuncTreeListVo»|ObjectResult«FuncTreeListVo»|
|&emsp;&emsp;data||FuncTreeListVo|FuncTreeListVo|
|&emsp;&emsp;&emsp;&emsp;customData|自定义函数|array|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;children|子目录|array|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;funcType|函数类型:0 系统函数,1 自定义函数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;systemData|系统函数|array|FuncTreeVo|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"customData": [
				{
					"children": [
						{
							"children": [
								{}
							],
							"funcType": 0,
							"id": 0,
							"label": "",
							"parentId": 0,
							"type": 0
						}
					],
					"funcType": 0,
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"systemData": [
				{
					"children": [
						{
							"children": [
								{}
							],
							"funcType": 0,
							"id": 0,
							"label": "",
							"parentId": 0,
							"type": 0
						}
					],
					"funcType": 0,
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			]
		}
	}
}
```


## 函数目录树


**接口地址**:`/api/v1/jobs/function/dir/tree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«DirTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«DirTreeVo»|CollectionResult«DirTreeVo»|
|&emsp;&emsp;data||array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|children|array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|lable|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


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
						"children": [
							{}
						],
						"id": 0,
						"label": "",
						"parentId": 0,
						"type": 0
					}
				],
				"id": 0,
				"label": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 目录删除


**接口地址**:`/api/v1/jobs/function/dir/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|baseReq|删除请求基础对象|body|true|BaseReq|BaseReq|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


## 目录移动


**接口地址**:`/api/v1/jobs/function/dir/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|optDirReq|目录移动请求对象|body|true|OptDevDir|OptDevDir|
|&emsp;&emsp;parentId|父目录id或目标目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«FuncTreeVo»»|
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
|value||ObjectResult«FuncTreeVo»|ObjectResult«FuncTreeVo»|
|&emsp;&emsp;data||FuncTreeVo|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|FuncTreeVo|
|&emsp;&emsp;&emsp;&emsp;funcType|函数类型:0 系统函数,1 自定义函数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"children": [
				{
					"children": [
						{}
					],
					"funcType": 0,
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"funcType": 0,
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 目录重命名


**接口地址**:`/api/v1/jobs/function/dir/{id}/rename`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|renameDir|目录重命名请求对象|body|true|RenameDir|RenameDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


# 标签工厂-标签管理


## 查询标签列表


**接口地址**:`/api/v1/tags/tag`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|pageNum|页数|query|false|integer(int32)||
|pageSize|分页大小|query|false|integer(int32)||
|publish|发布状态 true:已发布,false:未发布|query|false|boolean||
|entityId|实体id|query|false|integer(int64)||
|keywordsFuzzy|查询条件|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«标签列表响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«标签列表响应对象»|PageResult«标签列表响应对象»|
|&emsp;&emsp;data||array|标签列表响应对象|
|&emsp;&emsp;&emsp;&emsp;description|标签描述|string||
|&emsp;&emsp;&emsp;&emsp;entityName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobId|标签任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName|标签任务名称|string||
|&emsp;&emsp;&emsp;&emsp;lifeCycleStr|标签生命周期|string||
|&emsp;&emsp;&emsp;&emsp;logicTable|标签逻辑表|string||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态，true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;tag|标签英文名|string||
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagName|标签中文名|string||
|&emsp;&emsp;&emsp;&emsp;tagScheduleCycle|标签调度周期|string||
|&emsp;&emsp;&emsp;&emsp;tagValue|标签属性值|string||
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
				"description": "",
				"entityName": "",
				"isLock": 0,
				"jobId": 0,
				"jobName": "",
				"lifeCycleStr": "",
				"logicTable": "",
				"publish": false,
				"tag": "",
				"tagId": 0,
				"tagName": "",
				"tagScheduleCycle": "",
				"tagValue": ""
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


## 新增标签


**接口地址**:`/api/v1/tags/tag`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"description": "",
	"entityId": 0,
	"lifeCycle": 0,
	"lifeCycleCustom": 0,
	"projectId": 0,
	"tag": "",
	"tagName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addTag|addTag|body|true|新增标签请求实体|新增标签请求实体|
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;entityId|实体id||false|integer(int64)||
|&emsp;&emsp;lifeCycle|生命周期:0.7d 1.15d 2.30d 3.90d 4.365d 5.永久 6.自定义||false|integer(int32)||
|&emsp;&emsp;lifeCycleCustom|生命周期天数||false|integer(int64)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;tag|标签英文名||false|string||
|&emsp;&emsp;tagName|标签中文名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«新增标签响应对象»»|
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
|value||ObjectResult«新增标签响应对象»|ObjectResult«新增标签响应对象»|
|&emsp;&emsp;data||新增标签响应对象|新增标签响应对象|
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"tagId": 0
		}
	}
}
```


## 实体及标签目录树


**接口地址**:`/api/v1/tags/tag/tree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«TagTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«TagTreeVo»|CollectionResult«TagTreeVo»|
|&emsp;&emsp;data||array|TagTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|TagTreeVo|
|&emsp;&emsp;&emsp;&emsp;enName|英文名|string||
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|中文名|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|标签锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型|integer(int32)||


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
						"children": [
							{}
						],
						"enName": "",
						"id": 0,
						"isLock": 0,
						"label": "",
						"lockTime": "",
						"locker": 0,
						"lockerShow": "",
						"parentId": 0,
						"type": 0
					}
				],
				"enName": "",
				"id": 0,
				"isLock": 0,
				"label": "",
				"lockTime": "",
				"locker": 0,
				"lockerShow": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 查询标签基本信息


**接口地址**:`/api/v1/tags/tag/{tagId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|标签id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«查询标签基本信息对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«查询标签基本信息对象»|ObjectResult«查询标签基本信息对象»|
|&emsp;&emsp;data||查询标签基本信息对象|查询标签基本信息对象|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;entityName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;lifeCycleStr|标签生命周期|string||
|&emsp;&emsp;&emsp;&emsp;tag|标签英文名|string||
|&emsp;&emsp;&emsp;&emsp;tagName|标签中文名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"description": "",
			"entityName": "",
			"lifeCycleStr": "",
			"tag": "",
			"tagName": ""
		}
	}
}
```


## 编辑标签


**接口地址**:`/api/v1/tags/tag/{tagId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"description": "",
	"lifeCycle": 0,
	"lifeCycleCustom": 0,
	"tagName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|tagId|path|true|integer(int64)||
|editTag|editTag|body|true|编辑标签请求实体|编辑标签请求实体|
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;lifeCycle|生命周期:0.7d 1.15d 2.30d 3.90d 4.365d 5.永久 6.自定义||false|integer(int32)||
|&emsp;&emsp;lifeCycleCustom|生命周期天数||false|integer(int64)||
|&emsp;&emsp;tagName|标签中文名||false|string||


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


## 删除标签


**接口地址**:`/api/v1/tags/tag/{tagId}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|标签id|path|true|integer(int64)||


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


## 克隆标签


**接口地址**:`/api/v1/tags/tag/{tagId}/clone`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"tag": "",
	"tagName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|tagId|path|true|integer(int64)||
|cloneTag|cloneTag|body|true|标签克隆请求实体|标签克隆请求实体|
|&emsp;&emsp;tag|标签英文名||false|string||
|&emsp;&emsp;tagName|标签中文名||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«新增标签响应对象»»|
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
|value||ObjectResult«新增标签响应对象»|ObjectResult«新增标签响应对象»|
|&emsp;&emsp;data||新增标签响应对象|新增标签响应对象|
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"tagId": 0
		}
	}
}
```


## 查询标签详细信息


**接口地址**:`/api/v1/tags/tag/{tagId}/detail`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|tagId|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«标签内容VO»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«标签内容VO»|ObjectResult«标签内容VO»|
|&emsp;&emsp;data||标签内容VO|标签内容VO|
|&emsp;&emsp;&emsp;&emsp;entityCnName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;entityScheduleCycle|实体调度周期 0：天,1：周,2：月,3：分钟,4：小时|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobId|标签任务ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|标签锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态，true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;tagExtendConfig|偏好标签额外配置|TagExtendConfig|TagExtendConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;maxNumber|最多返回个数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeDecay|时间衰减曲线,0:无衰减,1:线性衰减,2:指数衰减|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeDecayPeriod|时间衰减周期,0,无衰减,1:7天,2:30天|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeSpan|时间跨度,0:1天,1:30天,2:60天,3:90天,4:1180天,5:365天|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weights|行为权重|array|GroupWeight|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weight||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tagGroups|标签配置|array|标签组|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;entityId|实体ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupName|标签组|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;subType|0:实体属性为标签值,1:自定义属性与标签值映射关系|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tagValues|标签配置|array|标签值|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;configRels|标签配置关系 1且 2或|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tagConfigs|标签配置|array|标签配置|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;conditionType|满足条件 1>，2<，3=，4!=，5>=，6<=，6<and<，7<and<=，8<=and<，9<=and<=，10包含，11不包含，12等于，13不等于，14剩余所有|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldName|实体属性 详情不需要/编辑不需要/版本对比需要|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyId|实体属性ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyType|实体属性类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;values|值|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;value|标签值中文|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;valueType|复合标签 1剩余所有 0其他|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;tagType|类型 0:基础标签,1:复合标签,2:偏好标签|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"entityCnName": "",
			"entityId": 0,
			"entityScheduleCycle": 0,
			"isLock": 0,
			"jobId": 0,
			"jobName": "",
			"lockTime": "",
			"locker": 0,
			"lockerShow": "",
			"publish": false,
			"tagExtendConfig": {
				"maxNumber": 0,
				"timeDecay": 0,
				"timeDecayPeriod": 0,
				"timeSpan": 0,
				"weights": [
					{
						"groupName": "",
						"weight": 0
					}
				]
			},
			"tagGroups": [
				{
					"entityId": 0,
					"groupName": "",
					"subType": 0,
					"tagValues": [
						{
							"configRels": [],
							"tagConfigs": [
								{
									"conditionType": 0,
									"fieldName": "",
									"propertyId": 0,
									"propertyType": 0,
									"values": []
								}
							],
							"value": "",
							"valueType": 0
						}
					]
				}
			],
			"tagId": 0,
			"tagName": "",
			"tagType": 0
		}
	}
}
```


## 保存标签详细信息


**接口地址**:`/api/v1/tags/tag/{tagId}/detail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"entityId": 0,
	"tagExtendConfig": {
		"maxNumber": 0,
		"timeDecay": 0,
		"timeDecayPeriod": 0,
		"timeSpan": 0,
		"weights": [
			{
				"groupName": "",
				"weight": 0
			}
		]
	},
	"tagGroups": [
		{
			"entityId": 0,
			"groupName": "",
			"subType": 0,
			"tagValues": [
				{
					"configRels": [],
					"tagConfigs": [
						{
							"conditionType": 0,
							"fieldName": "",
							"propertyId": 0,
							"propertyType": 0,
							"values": []
						}
					],
					"value": "",
					"valueType": 0
				}
			]
		}
	],
	"tagId": 0,
	"tagType": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|tagId|path|true|integer(int64)||
|tagDetail|tagDetail|body|true|标签内容-标签工厂|标签内容-标签工厂|
|&emsp;&emsp;entityId|实体id||false|integer(int64)||
|&emsp;&emsp;tagExtendConfig|偏好标签额外配置||false|TagExtendConfig|TagExtendConfig|
|&emsp;&emsp;&emsp;&emsp;maxNumber|最多返回个数||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeDecay|时间衰减曲线,0:无衰减,1:线性衰减,2:指数衰减||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeDecayPeriod|时间衰减周期,0,无衰减,1:7天,2:30天||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeSpan|时间跨度,0:1天,1:30天,2:60天,3:90天,4:1180天,5:365天||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;weights|行为权重||false|array|GroupWeight|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupName|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weight|||false|integer(int32)||
|&emsp;&emsp;tagGroups|标签组||false|array|标签组|
|&emsp;&emsp;&emsp;&emsp;entityId|实体ID||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;groupName|标签组||false|string||
|&emsp;&emsp;&emsp;&emsp;subType|0:实体属性为标签值,1:自定义属性与标签值映射关系||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tagValues|标签配置||false|array|标签值|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;configRels|标签配置关系 1且 2或||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tagConfigs|标签配置||false|array|标签配置|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;conditionType|满足条件 1>，2<，3=，4!=，5>=，6<=，6<and<，7<and<=，8<=and<，9<=and<=，10包含，11不包含，12等于，13不等于，14剩余所有||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldName|实体属性 详情不需要/编辑不需要/版本对比需要||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyId|实体属性ID||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyType|实体属性类型||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;values|值||false|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;value|标签值中文||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;valueType|复合标签 1剩余所有 0其他||false|integer(int32)||
|&emsp;&emsp;tagId|标签id||false|integer(int64)||
|&emsp;&emsp;tagType|类型 0:基础标签,1:复合标签,2:偏好标签||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«标签保存返回结果»»|
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
|value||ObjectResult«标签保存返回结果»|ObjectResult«标签保存返回结果»|
|&emsp;&emsp;data||标签保存返回结果|标签保存返回结果|
|&emsp;&emsp;&emsp;&emsp;jobId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"jobId": 0,
			"jobName": ""
		}
	}
}
```


## 标签版本对比


**接口地址**:`/api/v1/tags/tag/{tagId}/detail/version/{version}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|version|version|path|true|integer(int64)||
|tagId|标签id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«标签内容VO»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«标签内容VO»|ObjectResult«标签内容VO»|
|&emsp;&emsp;data||标签内容VO|标签内容VO|
|&emsp;&emsp;&emsp;&emsp;entityCnName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;entityScheduleCycle|实体调度周期 0：天,1：周,2：月,3：分钟,4：小时|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobId|标签任务ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;jobName|任务名称|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|标签锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态，true:已发布，false:未发布|boolean||
|&emsp;&emsp;&emsp;&emsp;tagExtendConfig|偏好标签额外配置|TagExtendConfig|TagExtendConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;maxNumber|最多返回个数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeDecay|时间衰减曲线,0:无衰减,1:线性衰减,2:指数衰减|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeDecayPeriod|时间衰减周期,0,无衰减,1:7天,2:30天|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeSpan|时间跨度,0:1天,1:30天,2:60天,3:90天,4:1180天,5:365天|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weights|行为权重|array|GroupWeight|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;weight||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tagGroups|标签配置|array|标签组|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;entityId|实体ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupName|标签组|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;subType|0:实体属性为标签值,1:自定义属性与标签值映射关系|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tagValues|标签配置|array|标签值|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;configRels|标签配置关系 1且 2或|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tagConfigs|标签配置|array|标签配置|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;conditionType|满足条件 1>，2<，3=，4!=，5>=，6<=，6<and<，7<and<=，8<=and<，9<=and<=，10包含，11不包含，12等于，13不等于，14剩余所有|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldName|实体属性 详情不需要/编辑不需要/版本对比需要|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyId|实体属性ID|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyType|实体属性类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;values|值|array|string|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;value|标签值中文|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;valueType|复合标签 1剩余所有 0其他|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;tagType|类型 0:基础标签,1:复合标签,2:偏好标签|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"entityCnName": "",
			"entityId": 0,
			"entityScheduleCycle": 0,
			"isLock": 0,
			"jobId": 0,
			"jobName": "",
			"lockTime": "",
			"locker": 0,
			"lockerShow": "",
			"publish": false,
			"tagExtendConfig": {
				"maxNumber": 0,
				"timeDecay": 0,
				"timeDecayPeriod": 0,
				"timeSpan": 0,
				"weights": [
					{
						"groupName": "",
						"weight": 0
					}
				]
			},
			"tagGroups": [
				{
					"entityId": 0,
					"groupName": "",
					"subType": 0,
					"tagValues": [
						{
							"configRels": [],
							"tagConfigs": [
								{
									"conditionType": 0,
									"fieldName": "",
									"propertyId": 0,
									"propertyType": 0,
									"values": []
								}
							],
							"value": "",
							"valueType": 0
						}
					]
				}
			],
			"tagId": 0,
			"tagName": "",
			"tagType": 0
		}
	}
}
```


## 标签发布


**接口地址**:`/api/v1/tags/tag/{tagId}/publish`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"description": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|publishTag|publishTag|body|true|发布标签请求实体|发布标签请求实体|
|&emsp;&emsp;description|发布描述||false|string||
|tagId|标签id|path|true|integer(int64)||


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


## 获取标签信息（编辑标签用）


**接口地址**:`/api/v1/tags/tag/{tagId}/simple`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|tagId|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«编辑标签响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«编辑标签响应对象»|ObjectResult«编辑标签响应对象»|
|&emsp;&emsp;data||编辑标签响应对象|编辑标签响应对象|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;lifeCycle|生命周期:0.7d 1.15d 2.30d 3.90d 4.365d 5.永久 6.自定义|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lifeCycleCustom|生命周期天数|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagId|标签id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagName|标签中文名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"description": "",
			"lifeCycle": 0,
			"lifeCycleCustom": 0,
			"tagId": 0,
			"tagName": ""
		}
	}
}
```


## 标签解锁


**接口地址**:`/api/v1/tags/tag/{tagId}/unlock`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|标签id|path|true|integer(int64)||


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


## 查询标签版本信息


**接口地址**:`/api/v1/tags/tag/{tagId}/version`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagId|标签id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«标签版本管理对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«标签版本管理对象»|CollectionResult«标签版本管理对象»|
|&emsp;&emsp;data||array|标签版本管理对象|
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;publishTime|发布时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;publishUser|发布者|string||
|&emsp;&emsp;&emsp;&emsp;version|版本号|integer(int32)||


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
				"publishTime": "",
				"publishUser": "",
				"version": 0
			}
		]
	}
}
```


# 表查询


## 表字段查询


**接口地址**:`/api/v1/jobs/table/columns`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tableName|表|query|true|string||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«表字段查询vo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«表字段查询vo»|CollectionResult«表字段查询vo»|
|&emsp;&emsp;data||array|表字段查询vo|
|&emsp;&emsp;&emsp;&emsp;cdId|表id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;columnName|字段名|string||
|&emsp;&emsp;&emsp;&emsp;comment|注释|string||
|&emsp;&emsp;&emsp;&emsp;integerIdx|表id|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;typeName|字段类型|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"cdId": 0,
				"columnName": "",
				"comment": "",
				"integerIdx": 0,
				"typeName": ""
			}
		]
	}
}
```


## 表字段查询


**接口地址**:`/api/v1/jobs/table/data/preview`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tableName|表|query|true|string||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«LinkedHashMap«string,object»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«LinkedHashMap«string,object»»|CollectionResult«LinkedHashMap«string,object»»|
|&emsp;&emsp;data||array|LinkedHashMap«string,object»|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{}
		]
	}
}
```


## 分区字段查询


**接口地址**:`/api/v1/jobs/table/partitions`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tableName|表|query|true|string||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«分区信息查询»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«分区信息查询»|CollectionResult«分区信息查询»|
|&emsp;&emsp;data||array|分区信息查询|
|&emsp;&emsp;&emsp;&emsp;createTime|创建时间|string||
|&emsp;&emsp;&emsp;&emsp;partId|分区id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;partName|分区名|string||
|&emsp;&emsp;&emsp;&emsp;recordNum|记录数|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;store|store|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;updateTime|修改时间|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"createTime": "",
				"partId": 0,
				"partName": "",
				"recordNum": 0,
				"store": 0,
				"updateTime": ""
			}
		]
	}
}
```


## 表列表


**接口地址**:`/api/v1/jobs/table/tables`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tableName|表名称|query|true|string||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«表列表查询vo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«表列表查询vo»|CollectionResult«表列表查询vo»|
|&emsp;&emsp;data||array|表列表查询vo|
|&emsp;&emsp;&emsp;&emsp;tblId|表id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tblName|表名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"tblId": 0,
				"tblName": ""
			}
		]
	}
}
```


# 平台配置


## 任务同步模式: 1 增量同步、2 全量同步


**接口地址**:`/api/v1/conf/dataSyncModes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## 字段映射模版


**接口地址**:`/api/v1/conf/fieldMapping`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dsType|数据源类型|query|true|integer(int32)||
|targetDsType|目标数据源类型|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«字段类型映射模板»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«字段类型映射模板»|ObjectResult«字段类型映射模板»|
|&emsp;&emsp;data||字段类型映射模板|字段类型映射模板|
|&emsp;&emsp;&emsp;&emsp;fieldMapingInfos|字段类型映射列表|array|字段类型映射对应关系|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sourceType|源字段类型|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;targetType|目标字段类型|string||
|&emsp;&emsp;&emsp;&emsp;sourceFieldTypes|源字段类型列表|array|string|
|&emsp;&emsp;&emsp;&emsp;targetFieldTypes|目标字段类型列表|array|string|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"fieldMapingInfos": [
				{
					"sourceType": "",
					"targetType": ""
				}
			],
			"sourceFieldTypes": [],
			"targetFieldTypes": []
		}
	}
}
```


## 文件压缩类型: 1 none 、2 zip 、3 gzip


**接口地址**:`/api/v1/conf/fileCompressedTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## 文件加密类型: 1 none、2 rsa 


**接口地址**:`/api/v1/conf/fileEncryptionTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## 文件类型:1 none 、2 csv 、3 txt


**接口地址**:`/api/v1/conf/fileTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## 文件写入模式: 1 truncate 写入前清理已有数据  2 append 追加写入


**接口地址**:`/api/v1/conf/fileWriteModes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## job类型查询


**接口地址**:`/api/v1/conf/jobTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«Map«string,object»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«Map«string,object»»|CollectionResult«Map«string,object»»|
|&emsp;&emsp;data||array|Map«string,object»|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{}
		]
	}
}
```


## 待发布对象类型列表


**接口地址**:`/api/v1/conf/publishingTargetTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«List«字典条目»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«List«字典条目»»|ObjectResult«List«字典条目»»|
|&emsp;&emsp;data||array|字典条目|
|&emsp;&emsp;&emsp;&emsp;label|标签|string||
|&emsp;&emsp;&emsp;&emsp;value|取值|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": 0
			}
		]
	}
}
```


## 资源类型


**接口地址**:`/api/v1/conf/resourceTypes`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«Map«string,object»»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«Map«string,object»»|CollectionResult«Map«string,object»»|
|&emsp;&emsp;data||array|Map«string,object»|


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{}
		]
	}
}
```


# 算法中心-资源数据管理


## 资源数据文件上传


**接口地址**:`/datascience/resource/upload`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|workdirId|目录id|query|false|integer(int64)||
|projectId|项目id|query|false|integer(int64)||
|projectName|项目名称|query|false|string||
|name|资源名称|query|false|string||
|fileType|资源文件类型|query|false|string||
|description|描述|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«ResourceTreeVo»»|
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
|value||ObjectResult«ResourceTreeVo»|ObjectResult«ResourceTreeVo»|
|&emsp;&emsp;data||ResourceTreeVo|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|ResourceTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父节点id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"children": [
				{
					"children": [
						{}
					],
					"id": 0,
					"label": "",
					"parentId": 0,
					"type": 0
				}
			],
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


# 函数管理


## 新建函数


**接口地址**:`/api/v1/jobs/function`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"businessFlag": 0,
	"className": "",
	"command": "",
	"description": "",
	"flinkFuncType": 0,
	"name": "",
	"projectId": 0,
	"resourceIds": "",
	"submitRemark": "",
	"usage": "",
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|saveFunction|saveFunction|body|true|新建/编辑函数请求对象|新建/编辑函数请求对象|
|&emsp;&emsp;businessFlag|业务标识（0:离线计算，1:实时计算，2:数据科学）||false|integer(int32)||
|&emsp;&emsp;className|类名||true|string||
|&emsp;&emsp;command|命令格式||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;flinkFuncType|flink函数类型（0:标量函数 SCALA，1:表值函数 TABLE，2:聚合函数 AGGREGATE）||false|integer(int32)||
|&emsp;&emsp;name|函数名||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;resourceIds|资源id（多个资源id逗号分隔）||true|string||
|&emsp;&emsp;submitRemark|提交备注||false|string||
|&emsp;&emsp;usage|用途||false|string||
|&emsp;&emsp;workdirId|目录id||true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«AddFuncVo»»|
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
|value||ObjectResult«AddFuncVo»|ObjectResult«AddFuncVo»|
|&emsp;&emsp;data||AddFuncVo|AddFuncVo|
|&emsp;&emsp;&emsp;&emsp;funcType|函数目录类型（0 系统函数,1 自定义函数）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|函数id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|函数名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|目录Id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"funcType": 0,
			"id": 0,
			"label": "",
			"parentId": 0
		}
	}
}
```


## 查询函数的详细信息


**接口地址**:`/api/v1/jobs/function/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|函数id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«查询函数详细信息响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«查询函数详细信息响应对象»|ObjectResult«查询函数详细信息响应对象»|
|&emsp;&emsp;data||查询函数详细信息响应对象|查询函数详细信息响应对象|
|&emsp;&emsp;&emsp;&emsp;className|类名|string||
|&emsp;&emsp;&emsp;&emsp;command|命令格式|string||
|&emsp;&emsp;&emsp;&emsp;createTime|修改时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;createUser|创建人|string||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;flinkFuncType|flink函数类型（0:标量函数 SCALA，1:表值函数 TABLE，2:聚合函数 AGGREGATE）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;id|函数id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;modifyTime|修改时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;modifyUser|修改人|string||
|&emsp;&emsp;&emsp;&emsp;name|函数名|string||
|&emsp;&emsp;&emsp;&emsp;resourceIds|资源id（多个资源id逗号分隔）|string||
|&emsp;&emsp;&emsp;&emsp;type|函数类型:0 系统函数,1 自定义函数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;typeString|函数类型名称|string||
|&emsp;&emsp;&emsp;&emsp;usage|用途|string||
|&emsp;&emsp;&emsp;&emsp;workdirId|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;workdirName|目录名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"className": "",
			"command": "",
			"createTime": "",
			"createUser": "",
			"description": "",
			"flinkFuncType": 0,
			"id": 0,
			"modifyTime": "",
			"modifyUser": "",
			"name": "",
			"resourceIds": "",
			"type": 0,
			"typeString": "",
			"usage": "",
			"workdirId": 0,
			"workdirName": ""
		}
	}
}
```


## 根据id查询function


**接口地址**:`/api/v1/jobs/function/{id}`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|projectId|query|true|integer(int64)||
|id|任务id|path|true|integer(int64)||


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


## 编辑函数


**接口地址**:`/api/v1/jobs/function/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"businessFlag": 0,
	"className": "",
	"command": "",
	"description": "",
	"flinkFuncType": 0,
	"name": "",
	"projectId": 0,
	"resourceIds": "",
	"submitRemark": "",
	"usage": "",
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|saveFunction|saveFunction|body|true|新建/编辑函数请求对象|新建/编辑函数请求对象|
|&emsp;&emsp;businessFlag|业务标识（0:离线计算，1:实时计算，2:数据科学）||false|integer(int32)||
|&emsp;&emsp;className|类名||true|string||
|&emsp;&emsp;command|命令格式||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;flinkFuncType|flink函数类型（0:标量函数 SCALA，1:表值函数 TABLE，2:聚合函数 AGGREGATE）||false|integer(int32)||
|&emsp;&emsp;name|函数名||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;resourceIds|资源id（多个资源id逗号分隔）||true|string||
|&emsp;&emsp;submitRemark|提交备注||false|string||
|&emsp;&emsp;usage|用途||false|string||
|&emsp;&emsp;workdirId|目录id||true|integer(int64)||
|id|函数id|path|true|integer(int64)||


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


## 删除函数


**接口地址**:`/api/v1/jobs/function/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0,
	"submitRemark": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|delFunction|删除函数请求对象|body|true|DelFunction|DelFunction|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;submitRemark|提交备注||false|string||
|id|函数id|path|true|integer(int64)||


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


## 移动函数


**接口地址**:`/api/v1/jobs/function/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|moveFunction|moveFunction|body|true|移动函数请求对象|移动函数请求对象|
|&emsp;&emsp;name|函数名||false|string||
|&emsp;&emsp;parentId|目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|id|函数id|path|true|integer(int64)||


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


## 提交/发布函数到发布管理中心


**接口地址**:`/api/v1/jobs/function/{id}/submit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|projectId|query|true|integer(int64)||
|id|任务id|path|true|integer(int64)||
|remark|remark|query|false|string||


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


# 数据同步


## [数据集成二期] 获取项目下根据数据源类型和数据源关系


**接口地址**:`/api/v1/dataSync/datasource/relation`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jobId|任务id|query|true|integer(int64)||
|scene|场景 1.source (来源)、 2.target (目标),可用值:source,target|query|true|ref||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«数据源类型和数据源关联关系对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«数据源类型和数据源关联关系对象»|CollectionResult«数据源类型和数据源关联关系对象»|
|&emsp;&emsp;data||array|数据源类型和数据源关联关系对象|
|&emsp;&emsp;&emsp;&emsp;dataSourceInfos||array|数据同步获取数据源|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;typeString||string||
|&emsp;&emsp;&emsp;&emsp;datasourceName||string||
|&emsp;&emsp;&emsp;&emsp;datasourceType||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"dataSourceInfos": [
					{
						"id": 0,
						"name": "",
						"type": 0,
						"typeString": ""
					}
				],
				"datasourceName": "",
				"datasourceType": 0
			}
		]
	}
}
```


## 表结构信息


**接口地址**:`/api/v1/dataSync/datasources`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|数据源id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«数据同步获取数据源»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«数据同步获取数据源»|CollectionResult«数据同步获取数据源»|
|&emsp;&emsp;data||array|数据同步获取数据源|
|&emsp;&emsp;&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;type||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;typeString||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"id": 0,
				"name": "",
				"type": 0,
				"typeString": ""
			}
		]
	}
}
```


## [数据集成二期] 获取用户上传文件的元数据


**接口地址**:`/api/v1/dataSync/resources/meta/{resourceId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|columnSeparator|columnSeparator|query|true|string||
|resourceId|资源id|path|true|integer(int64)||
|includeMetadata|是否包含元数据|query|true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«表信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«表信息»|ObjectResult«表信息»|
|&emsp;&emsp;data||表信息|表信息|
|&emsp;&emsp;&emsp;&emsp;columns|字段集合列表|array|TableCol|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colType||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colTypeInt||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;comment||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;index||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;ifPt|是否分区|boolean||
|&emsp;&emsp;&emsp;&emsp;pts|分区信息|array|string|
|&emsp;&emsp;&emsp;&emsp;splitPk||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"columns": [
				{
					"colName": "",
					"colType": "",
					"colTypeInt": 0,
					"comment": "",
					"index": 0
				}
			],
			"ifPt": false,
			"pts": [],
			"splitPk": ""
		}
	}
}
```


## 表数据预览


**接口地址**:`/api/v1/dataSync/{id}/data/preview`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectName|项目名称id|query|true|string||
|projectId|项目id|query|true|integer(int64)||
|id|数据源id|path|true|integer(int64)||
|tableName|表名|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«List»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«List»|CollectionResult«List»|
|&emsp;&emsp;data||array|array|


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


## 表字段


**接口地址**:`/api/v1/dataSync/{id}/table/columns`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|id|数据源id|path|true|integer(int64)||
|tableName|表名|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«TableCol»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«TableCol»|CollectionResult«TableCol»|
|&emsp;&emsp;data||array|TableCol|
|&emsp;&emsp;&emsp;&emsp;colName||string||
|&emsp;&emsp;&emsp;&emsp;colType||string||
|&emsp;&emsp;&emsp;&emsp;colTypeInt||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;comment||string||
|&emsp;&emsp;&emsp;&emsp;index||integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"colName": "",
				"colType": "",
				"colTypeInt": 0,
				"comment": "",
				"index": 0
			}
		]
	}
}
```


## 表结构信息


**接口地址**:`/api/v1/dataSync/{id}/tableMeta`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|数据源id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||
|tableName|表名(模糊搜索)|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«表信息»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«表信息»|ObjectResult«表信息»|
|&emsp;&emsp;data||表信息|表信息|
|&emsp;&emsp;&emsp;&emsp;columns|字段集合列表|array|TableCol|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colType||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;colTypeInt||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;comment||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;index||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;ifPt|是否分区|boolean||
|&emsp;&emsp;&emsp;&emsp;pts|分区信息|array|string|
|&emsp;&emsp;&emsp;&emsp;splitPk||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"columns": [
				{
					"colName": "",
					"colType": "",
					"colTypeInt": 0,
					"comment": "",
					"index": 0
				}
			],
			"ifPt": false,
			"pts": [],
			"splitPk": ""
		}
	}
}
```


## 根据数据源id获取数据库表及kafka主题


**接口地址**:`/api/v1/dataSync/{id}/tables`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|数据源id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||
|tableName|表名(模糊搜索)|query|false|string||


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


# 标签工厂-实体管理


## 根据条件查询实体列表


**接口地址**:`/api/v1/tags/entity`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageNum|页数|query|true|integer(int32)||
|pageSize|分页大小|query|true|integer(int32)||
|projectId|项目id|query|true|integer(int64)||
|dataZoneId|数据域id|query|true|integer(int64)||
|entityName|实体名|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«PageResult«EntityListVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||PageResult«EntityListVo»|PageResult«EntityListVo»|
|&emsp;&emsp;data||array|EntityListVo|
|&emsp;&emsp;&emsp;&emsp;cnName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;dataZoneId|所属数据域id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;dataZoneName|所属数据域名称|string||
|&emsp;&emsp;&emsp;&emsp;deleteFlag|是否可以删除标识 true:可删除 false 不可删除|boolean||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;enName|实体英文名|string||
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tagNums|已创建标签个数|integer(int64)||
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
				"cnName": "",
				"dataZoneId": 0,
				"dataZoneName": "",
				"deleteFlag": false,
				"description": "",
				"enName": "",
				"entityId": 0,
				"tagNums": 0
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


## 新建实体


**接口地址**:`/api/v1/tags/entity`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"bindTableType": 0,
	"cnName": "",
	"dataZoneId": 0,
	"description": "",
	"enName": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addEntity|addEntity|body|true|新增标签实体请求对象|新增标签实体请求对象|
|&emsp;&emsp;bindTableType|绑表方式 0:引用来源表，1:新建来源表||false|integer(int32)||
|&emsp;&emsp;cnName|实体中文名||false|string||
|&emsp;&emsp;dataZoneId|所属数据域||false|integer(int64)||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;enName|实体英文名||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«新增实体响应对象»»|
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
|value||ObjectResult«新增实体响应对象»|ObjectResult«新增实体响应对象»|
|&emsp;&emsp;data||新增实体响应对象|新增实体响应对象|
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"entityId": 0
		}
	}
}
```


## 获取表字段列表


**接口地址**:`/api/v1/tags/entity/columns`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|tableName|表名称|query|true|string||
|dbName|数据库名称|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«获取字段列表响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«获取字段列表响应对象»|CollectionResult«获取字段列表响应对象»|
|&emsp;&emsp;data||array|获取字段列表响应对象|
|&emsp;&emsp;&emsp;&emsp;description|字段描述|string||
|&emsp;&emsp;&emsp;&emsp;fieldName|字段名|string||
|&emsp;&emsp;&emsp;&emsp;fieldType|字段类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;fieldTypeStr|字段类型名称|string||


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
				"fieldName": "",
				"fieldType": 0,
				"fieldTypeStr": ""
			}
		]
	}
}
```


## 获取实体下拉列表


**接口地址**:`/api/v1/tags/entity/dropBox`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«EntityDropBoxVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«EntityDropBoxVo»|CollectionResult«EntityDropBoxVo»|
|&emsp;&emsp;data||array|EntityDropBoxVo|
|&emsp;&emsp;&emsp;&emsp;label|实体id|string||
|&emsp;&emsp;&emsp;&emsp;value|实体中文名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"label": "",
				"value": ""
			}
		]
	}
}
```


## 来源表列表


**接口地址**:`/api/v1/tags/entity/tables`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|tableName|表名（为空则查询项目下所有的来源表）|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«数据来源表响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«数据来源表响应对象»|CollectionResult«数据来源表响应对象»|
|&emsp;&emsp;data||array|数据来源表响应对象|
|&emsp;&emsp;&emsp;&emsp;dbName|数据库名|string||
|&emsp;&emsp;&emsp;&emsp;jobId|任务id|string||
|&emsp;&emsp;&emsp;&emsp;tableName|数据源表名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"dbName": "",
				"jobId": "",
				"tableName": ""
			}
		]
	}
}
```


## 获取保存逻辑表的目标层级目录


**接口地址**:`/api/v1/tags/entity/targetDir`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«获取存放逻辑表的目标层级目录响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«获取存放逻辑表的目标层级目录响应对象»|CollectionResult«获取存放逻辑表的目标层级目录响应对象»|
|&emsp;&emsp;data||array|获取存放逻辑表的目标层级目录响应对象|
|&emsp;&emsp;&emsp;&emsp;defaultDir|是否默认目录 true:是 false:否|boolean||
|&emsp;&emsp;&emsp;&emsp;workdirId|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;workdirName|目录名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": [
			{
				"defaultDir": false,
				"workdirId": 0,
				"workdirName": ""
			}
		]
	}
}
```


## 数据域与标签实体树


**接口地址**:`/api/v1/tags/entity/tree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«EntityTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«EntityTreeVo»|CollectionResult«EntityTreeVo»|
|&emsp;&emsp;data||array|EntityTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|EntityTreeVo|
|&emsp;&emsp;&emsp;&emsp;deleteFlag|是否可删除标识 true: 可删除  false: 不可删除|boolean||
|&emsp;&emsp;&emsp;&emsp;enName|实体英文名|string||
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|锁定人|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型|integer(int32)||


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
						"children": [
							{}
						],
						"deleteFlag": false,
						"enName": "",
						"id": 0,
						"isLock": 0,
						"label": "",
						"lockTime": "",
						"locker": 0,
						"lockerShow": "",
						"parentId": 0,
						"type": 0
					}
				],
				"deleteFlag": false,
				"enName": "",
				"id": 0,
				"isLock": 0,
				"label": "",
				"lockTime": "",
				"locker": 0,
				"lockerShow": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 获取实体信息详情（包括基本信息）


**接口地址**:`/api/v1/tags/entity/{entityId}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|entityId|实体id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«EntityVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«EntityVo»|ObjectResult«EntityVo»|
|&emsp;&emsp;data||EntityVo|EntityVo|
|&emsp;&emsp;&emsp;&emsp;behaviorCnt|行为次数字段名|string||
|&emsp;&emsp;&emsp;&emsp;behaviorTime|行为时间字段名|string||
|&emsp;&emsp;&emsp;&emsp;behaviorTimeFormat|行为时间格式|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;bindTableType|绑表方式 0:引用来源表，1:新建来源表|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;cnName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;columnList|标签属性列表|array|标签属性列表|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;deleteFlag|是否可删除标识 true: 可删除  false: 不可删除|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description|字段描述|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldName|字段名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldType|字段类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldTypeStr|字段类型名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;propertyId|属性id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;dataZoneName|所属数据域名称|string||
|&emsp;&emsp;&emsp;&emsp;dbName|来源表所属数据库|string||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;enName|实体英文名|string||
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;entityKey|实体标识符（实体主键）|string||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lockTime|锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|锁定人|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;opFlag|是否可以操作，true:可操作，false:不可操作|boolean||
|&emsp;&emsp;&emsp;&emsp;sourceJobId|来源表任务id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tableName|来源表|string||
|&emsp;&emsp;&emsp;&emsp;workdirId|生成标签逻辑表所在的目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;workdirName|生成标签逻辑表所在的目录名|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"behaviorCnt": "",
			"behaviorTime": "",
			"behaviorTimeFormat": 0,
			"bindTableType": 0,
			"cnName": "",
			"columnList": [
				{
					"deleteFlag": false,
					"description": "",
					"fieldName": "",
					"fieldType": 0,
					"fieldTypeStr": "",
					"propertyId": 0
				}
			],
			"dataZoneName": "",
			"dbName": "",
			"description": "",
			"enName": "",
			"entityId": 0,
			"entityKey": "",
			"isLock": 0,
			"lockTime": "",
			"locker": 0,
			"lockerShow": "",
			"opFlag": false,
			"sourceJobId": 0,
			"tableName": "",
			"workdirId": 0,
			"workdirName": ""
		}
	}
}
```


## 修改标签实体


**接口地址**:`/api/v1/tags/entity/{entityId}`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"cnName": "",
	"dataZoneId": 0,
	"description": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateEntity|updateEntity|body|true|修改标签实体请求对象|修改标签实体请求对象|
|&emsp;&emsp;cnName|实体中文名||false|string||
|&emsp;&emsp;dataZoneId|所属数据域||false|integer(int64)||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|entityId|实体id|path|true|integer(int64)||


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


## 删除标签实体


**接口地址**:`/api/v1/tags/entity/{entityId}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|entityId|实体id|path|true|integer(int64)||


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


## 克隆标签实体


**接口地址**:`/api/v1/tags/entity/{entityId}/clone`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"cnName": "",
	"enName": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|cloneEntity|cloneEntity|body|true|克隆标签实体请求对象|克隆标签实体请求对象|
|&emsp;&emsp;cnName|实体中文名||false|string||
|&emsp;&emsp;enName|实体英文名||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|entityId|实体id|path|true|integer(int64)||


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


## 【标签二期修改】保存标签实体


**接口地址**:`/api/v1/tags/entity/{entityId}/save`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"behaviorCnt": "",
	"behaviorTime": "",
	"behaviorTimeFormat": 0,
	"bindTableType": 0,
	"columnList": [
		{
			"description": "",
			"fieldName": "",
			"fieldType": 0,
			"propertyId": 0
		}
	],
	"dbName": "",
	"description": "",
	"entityKey": "",
	"projectId": 0,
	"sourceJobId": 0,
	"tableName": "",
	"workdirId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|saveEntity|saveEntity|body|true|保存标签实体请求对象|保存标签实体请求对象|
|&emsp;&emsp;behaviorCnt|行为次数字段名||false|string||
|&emsp;&emsp;behaviorTime|行为时间字段名||false|string||
|&emsp;&emsp;behaviorTimeFormat|行为时间格式，0 yyyyMMdd HH:mm:ss, 1 yyyyMMdd||false|integer(int32)||
|&emsp;&emsp;bindTableType|绑表方式 0:引用来源表，1:新建来源表||false|integer(int32)||
|&emsp;&emsp;columnList|标签属性列表||false|array|获取标签属性列表响应对象|
|&emsp;&emsp;&emsp;&emsp;description|字段描述||true|string||
|&emsp;&emsp;&emsp;&emsp;fieldName|字段名||false|string||
|&emsp;&emsp;&emsp;&emsp;fieldType|字段类型||true|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;propertyId|属性id||false|integer(int64)||
|&emsp;&emsp;dbName|来源表所属数据库||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;entityKey|实体标识符（实体主键）||false|string||
|&emsp;&emsp;projectId|项目id||false|integer(int64)||
|&emsp;&emsp;sourceJobId|来源表任务id||false|integer(int64)||
|&emsp;&emsp;tableName|来源表||false|string||
|&emsp;&emsp;workdirId|生成标签逻辑表所在的目录id||false|integer(int64)||
|entityId|实体id|path|true|integer(int64)||


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


## 获取实体信息（编辑实体用）


**接口地址**:`/api/v1/tags/entity/{entityId}/simple`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|entityId|实体id|path|true|integer(int64)||
|projectId|项目id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«SimpleEntityVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«SimpleEntityVo»|ObjectResult«SimpleEntityVo»|
|&emsp;&emsp;data||SimpleEntityVo|SimpleEntityVo|
|&emsp;&emsp;&emsp;&emsp;cnName|实体中文名|string||
|&emsp;&emsp;&emsp;&emsp;dataZoneId|所属数据域id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;dataZoneName|所属数据域名称|string||
|&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"cnName": "",
			"dataZoneId": 0,
			"dataZoneName": "",
			"description": "",
			"entityId": 0
		}
	}
}
```


## 获取实体属性下拉列表


**接口地址**:`/api/v1/tags/entity/{entityId}/tagProperty`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|entityId|实体id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«标签属性下拉列表响应对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«标签属性下拉列表响应对象»|CollectionResult«标签属性下拉列表响应对象»|
|&emsp;&emsp;data||array|标签属性下拉列表响应对象|
|&emsp;&emsp;&emsp;&emsp;description|字段描述|string||
|&emsp;&emsp;&emsp;&emsp;fieldName|属性字段名|string||
|&emsp;&emsp;&emsp;&emsp;fieldType|字段类型（0:字符型，1:数值型）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;propertyId|属性id|integer(int64)||


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
				"fieldName": "",
				"fieldType": 0,
				"propertyId": 0
			}
		]
	}
}
```


## 解锁实体


**接口地址**:`/api/v1/tags/entity/{entityId}/unlock`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|unlockEntity|解锁实体请求对象|body|true|UnlockEntity|UnlockEntity|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|entityId|实体id|path|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«解锁任务响应对象»»|
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
|value||ObjectResult«解锁任务响应对象»|ObjectResult«解锁任务响应对象»|
|&emsp;&emsp;data||解锁任务响应对象|解锁任务响应对象|
|&emsp;&emsp;&emsp;&emsp;entityId|实体id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;lockTime|任务锁定时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;locker|任务锁定者|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;lockerShow|任务锁定者名称|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"entityId": 0,
			"isLock": 0,
			"lockTime": "",
			"locker": 0,
			"lockerShow": ""
		}
	}
}
```


# 目录管理


## 新增目录


**接口地址**:`/api/v1/jobs/dir`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"parentId": 0,
	"projectId": 0,
	"sync": false
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addDirReq|增加目录请求对象|body|true|AddDevDir|AddDevDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;parentId|父目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||
|&emsp;&emsp;sync|是否为同步目录(默认为否)||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«AddDevDirVo»»|
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
|value||ObjectResult«AddDevDirVo»|ObjectResult«AddDevDirVo»|
|&emsp;&emsp;data||AddDevDirVo|AddDevDirVo|
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"id": 0,
			"label": "",
			"parentId": 0,
			"type": 0
		}
	}
}
```


## 目录及任务树


**接口地址**:`/api/v1/jobs/dir/jobTree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|sync|是否只包含同步目录及任务|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«DirJobTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«DirJobTreeVo»|CollectionResult«DirJobTreeVo»|
|&emsp;&emsp;data||array|DirJobTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|DirJobTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|锁定时间|string||
|&emsp;&emsp;&emsp;&emsp;locker|锁定人|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;opFlag|可操作标识，true:可操作，false：不可操作|boolean||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;periodType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;periodTypeString|任务类型名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态|boolean||
|&emsp;&emsp;&emsp;&emsp;templateDir|是否模版目录及新建层级的时候创建的目录，true:是，false：否|boolean||
|&emsp;&emsp;&emsp;&emsp;type|文件类型|integer(int32)||


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
						"children": [
							{}
						],
						"id": 0,
						"isLock": 0,
						"jobType": 0,
						"label": "",
						"lockTime": "",
						"locker": "",
						"lockerShow": "",
						"opFlag": false,
						"parentId": 0,
						"periodType": 0,
						"periodTypeString": "",
						"publish": false,
						"templateDir": false,
						"type": 0
					}
				],
				"id": 0,
				"isLock": 0,
				"jobType": 0,
				"label": "",
				"lockTime": "",
				"locker": "",
				"lockerShow": "",
				"opFlag": false,
				"parentId": 0,
				"periodType": 0,
				"periodTypeString": "",
				"publish": false,
				"templateDir": false,
				"type": 0
			}
		]
	}
}
```


## 目录树


**接口地址**:`/api/v1/jobs/dir/tree`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectId|项目id|query|true|integer(int64)||
|sync|是否只包含同步目录及任务|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«CollectionResult«DirTreeVo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||CollectionResult«DirTreeVo»|CollectionResult«DirTreeVo»|
|&emsp;&emsp;data||array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|children|array|DirTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;label|lable|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type|文件类型，（100:目录，200文件）|integer(int32)||


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
						"children": [
							{}
						],
						"id": 0,
						"label": "",
						"parentId": 0,
						"type": 0
					}
				],
				"id": 0,
				"label": "",
				"parentId": 0,
				"type": 0
			}
		]
	}
}
```


## 目录删除


**接口地址**:`/api/v1/jobs/dir/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|baseReq|删除请求基础对象|body|true|BaseReq|BaseReq|
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


## 目录移动


**接口地址**:`/api/v1/jobs/dir/{id}/move`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"parentId": 0,
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|optDirReq|目录移动请求对象|body|true|OptDevDir|OptDevDir|
|&emsp;&emsp;parentId|父目录id或目标目录id||true|integer(int64)||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«DirJobTreeVo»»|
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
|value||ObjectResult«DirJobTreeVo»|ObjectResult«DirJobTreeVo»|
|&emsp;&emsp;data||DirJobTreeVo|DirJobTreeVo|
|&emsp;&emsp;&emsp;&emsp;children|子目录|array|DirJobTreeVo|
|&emsp;&emsp;&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;isLock|是否锁定（1:锁定，-1:未锁定）|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;jobType|任务类型|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;label|label|string||
|&emsp;&emsp;&emsp;&emsp;lockTime|锁定时间|string||
|&emsp;&emsp;&emsp;&emsp;locker|锁定人|string||
|&emsp;&emsp;&emsp;&emsp;lockerShow|锁定人名称|string||
|&emsp;&emsp;&emsp;&emsp;opFlag|可操作标识，true:可操作，false：不可操作|boolean||
|&emsp;&emsp;&emsp;&emsp;parentId|父目录id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;periodType|任务类型:0--hive-sql、1--shell,2--数据同步、3--spark-sql、4--python、5--虚任务、6--pyspark 7--flink|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;periodTypeString|任务类型名称|string||
|&emsp;&emsp;&emsp;&emsp;publish|发布状态|boolean||
|&emsp;&emsp;&emsp;&emsp;templateDir|是否模版目录及新建层级的时候创建的目录，true:是，false：否|boolean||
|&emsp;&emsp;&emsp;&emsp;type|文件类型|integer(int32)||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"children": [
				{
					"children": [
						{}
					],
					"id": 0,
					"isLock": 0,
					"jobType": 0,
					"label": "",
					"lockTime": "",
					"locker": "",
					"lockerShow": "",
					"opFlag": false,
					"parentId": 0,
					"periodType": 0,
					"periodTypeString": "",
					"publish": false,
					"templateDir": false,
					"type": 0
				}
			],
			"id": 0,
			"isLock": 0,
			"jobType": 0,
			"label": "",
			"lockTime": "",
			"locker": "",
			"lockerShow": "",
			"opFlag": false,
			"parentId": 0,
			"periodType": 0,
			"periodTypeString": "",
			"publish": false,
			"templateDir": false,
			"type": 0
		}
	}
}
```


## 目录重命名


**接口地址**:`/api/v1/jobs/dir/{id}/rename`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"name": "",
	"projectId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|path|true|integer(int64)||
|renameDir|目录重命名请求对象|body|true|RenameDir|RenameDir|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;projectId|项目id||true|integer(int64)||


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


# 数据克隆


## 数据导出


**接口地址**:`/api/v1/jobs/dataclone/exportV2`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|projectName|projectName|query|false|string||
|path|path|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«FileBo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«FileBo»|ObjectResult«FileBo»|
|&emsp;&emsp;data||FileBo|FileBo|
|&emsp;&emsp;&emsp;&emsp;key||string||
|&emsp;&emsp;&emsp;&emsp;url||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"key": "",
			"url": ""
		}
	}
}
```


## 导入


**接口地址**:`/api/v1/jobs/dataclone/import`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"operationType": 0,
	"preKey": "",
	"projectId": 0,
	"publishFlag": false,
	"targetManagerId": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|importReq|importReq|body|true|导入参数|导入参数|
|&emsp;&emsp;operationType|operationType||false|integer(int32)||
|&emsp;&emsp;preKey|数据缓存key||false|string||
|&emsp;&emsp;projectId|目标项目id||false|integer(int64)||
|&emsp;&emsp;publishFlag|任务发布,true-是，false-否，默认false||false|boolean||
|&emsp;&emsp;targetManagerId|目标责任人id||false|integer(int64)||


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


## 导入


**接口地址**:`/api/v1/jobs/dataclone/importV2`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|projectName|projectName|query|false|string||


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


## 预导入


**接口地址**:`/api/v1/jobs/dataclone/pre/import`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|projectId|目标项目id|query|false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«DataCloneRes»»|
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
|value||ObjectResult«DataCloneRes»|ObjectResult«DataCloneRes»|
|&emsp;&emsp;data||DataCloneRes|DataCloneRes|
|&emsp;&emsp;&emsp;&emsp;operationType|可选操作列表|object||
|&emsp;&emsp;&emsp;&emsp;preKey|缓存数据key|string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"operationType": {},
			"preKey": ""
		}
	}
}
```


## 数据生成文件


**接口地址**:`/api/v1/jobs/dataclone/publish`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|通用返回结果«ObjectResult«FileBo»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|codeDesc|返回描述|string||
|codeNum|返回码|integer(int32)|integer(int32)|
|success|是否成功|boolean||
|value||ObjectResult«FileBo»|ObjectResult«FileBo»|
|&emsp;&emsp;data||FileBo|FileBo|
|&emsp;&emsp;&emsp;&emsp;key||string||
|&emsp;&emsp;&emsp;&emsp;url||string||


**响应示例**:
```javascript
{
	"codeDesc": "成功",
	"codeNum": 1000,
	"success": true,
	"value": {
		"data": {
			"key": "",
			"url": ""
		}
	}
}
```