## Nginx简介

是一个高性能HTTP和反向代理服务器，也是个邮件（SMTP、POP3）服务器

使用Nginx：BAT，JD，新浪，网易。。。

[中文文档](https://www.nginx.cn/doc/index.html) [中文文档2](http://tengine.taobao.org/book/)

[官方文档](http://nginx.org/)

不支持windows

#### 什么是http服务器？什么是反向代理服务器？

![](E:\Learning\Django\TruePro\GPAXF_fail\App\doc\Http和反向代理.png)

- http服务器
  - Nginx接受客户端请求，找到请求资源并返回，也就是Nginx直接对接资源，这就是充当http服务器。
- 反向代理服务器
  - Nginx与其他任何服务器（这些服务器有对外的能力，但不擅长处理静态资源，但作为http服务器性能很高）对接，比如uWSGI，runserver（Django自带的用于开发环境的），gunicorn，nginx不处理请求，只是做一个转换，将请求交给其他服务器，再接受其他服务器的返回并返回给客户端，这就是反向代理。其他服务器会进行url匹配并进行MVC流程。



##  Nginx安装

- 查看官方文档（英文），有详细教程。
  - 源码安装
    1. 下载源码压缩包（deb，rpm）（缺点是依赖缺失不会解决）
    2. 安装源码编译依赖包 gcc,zlib,make
    3. 配置编译模块
    4. make && make test
    5. make install
  - 包管理工具安装（apt，yum等）（相对最好的方式）
    1. 去官网将所使用依赖添加到包管理工具中
    2. 更新包管理工具资源
    3. 使用包管理工具安装

- 控制nginx
  - 启动

##  Nginx配置文件

##  Django项目部署