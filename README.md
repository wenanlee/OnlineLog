# Log
简单日志平台.

## 安装

> 测试平台:
>
> Python 3.x
>
> Windows 10 or Ubuntu server 18.04

## 运行

> * 本地运行
>
> ```bash
> #默认模式运行 端口80
> cd Log
> python server.py
> #自指定端口运行 端口 8080
> cd Log
> python server -p 8080
> ```
>
> * Docker
>
> ```bash
> docker build -t log .
> docker run -d -p 8080:80 log
> ```
> * sql
> ```
> id
uid
app_name
time
log_level
log_info
create_date



## 测试
> #### 本地测试
> > * [插入测试](http://127.0.0.1/insert?name=测试软件&uid=1&log=[{"level":1,"time":"1.2223s","info":"测试消息1"},{"level":2,"time":"1.2223s","info":"测试消息2"}]) PS:GET方法单次传输数据有限,请注意.
> > * [默认查询测试](http://127.0.0.1/select?1=1)
> > * [查询用户[test]测试](http://127.0.0.1/select?uid=1)
> > * [查询测试(MJ 最后一次测试 错误)](http://127.0.0.1/select?log_level>=2 and app_name = 测试软件)
> > * todo[查询测试(日志等级<2)](http://127.0.0.1/select?level=<2)
> > * todo[查询测试(项目:测试软件 且 日志等级<3)](http://127.0.0.1/select?name=测试软件&level=<3))

> ####  远程测试
>> * [插入测试](/insert?name=测试软件&log=[{"level":1,"time":"1.2223s","info":"测试消息1"},{"level":2,"time":"1.2223s","info":"测试消息2"}]) PS:GET方法单次传输数据有限,请注意.
>> * [默认查询测试](/select)
>> * todo[查询测试(日志等级<2)](/select?level=<2)
>> * todo[查询测试(项目:测试软件 且 日志等级<3)](/select?name=测试软件&level=<3)
