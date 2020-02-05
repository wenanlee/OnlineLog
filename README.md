# Log
简单日志平台

## 安装

> Python 3.x

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
> #TODO
> ```

## 测试
>  [插入测试](http://127.0.0.1/insert?{"name":"测试软件","log":[{"level":1,"time":"1.2223s","info":"测试消息1"},{"level":2,"time":"1.2223s","info":"测试消息2"}]})
>  [默认查询测试](http://127.0.0.1/select?{"name":"null","level":"null","info":"null","create_date":"null"})
> todo[查询测试(日志等级<2)](http://127.0.0.1/select?{"name":"null","level":"<2","info":"null","create_date":"null"})
> todo[查询测试(项目:测试软件 且 日志等级<3)](http://127.0.0.1/select?{"name":"测试软件","level":"<3","info":"null","create_date":"null"}))
