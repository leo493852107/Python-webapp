# Python-webapp
------

## Python-webapp from [廖雪峰](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001397616003925a3d157284cd24bc0952d6c4a7c9d8c55000)

## [部署Web App](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140262673295076f525af00734a8e924c5fc6ff5b6091000#0)

### 总结一下我们需要用到的服务有：

> * Nginx：高性能Web服务器+负责反向代理；

> * gunicorn：高性能WSGI服务器；

> * gevent：把Python同步代码变成异步协程的库；

> * Supervisor：监控服务进程的工具；

> * MySQL：数据库服务。

### 在Linux服务器上用apt可以直接安装上述服务：

```shell
$ sudo apt-get install nginx gunicorn python-gevent supervisor mysql-server
```

### 然后，再把我们自己的Web App用到的Python库安装了：

```shell
$ sudo apt-get install python-jinja2 python-mysql.connector
```
