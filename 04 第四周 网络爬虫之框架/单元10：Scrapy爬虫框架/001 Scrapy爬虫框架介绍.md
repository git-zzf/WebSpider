# Scrapy爬虫框架介绍

一个功能强大的网络爬虫框架，使用Python实现爬虫的重要的技术路线



## 安装Scrapy库遇到的问题：

1. `pip install scrapy`遇到`twisted`报错

2. 根据`https://blog.csdn.net/qq_32145097/article/details/90241733`得知是缺失`Twisted`文件

3. 安装`Twisted`，需要要先查找到兼容的格式

4. 根据`https://blog.csdn.net/qq_38161040/article/details/88062405`

   ```cmd
   >>> python
   >>> import pip._internal.pep425tags
   >>> print(pip._internal.pep425tags.get_supported())
   ```

   通过结果得知，需要安装`cp38 win32`版本的`Twisted`

4. 通过网站`https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted`下载对应版本的`Twisted`

5. 保存到电脑，然后通过`cd `命令找到下载目录下：

   ```python
   >>> pip install Twisted-20.3.0-cp38-cp38-win32.whl
   ```

   安装完成

6. 重新安装Scrapy：

   ```python
   pip intall scrapy
   ```

   `Scrapy`库安装成功



Scrapy不是一个简单的函数功能库，而是一个爬虫框架

爬虫框架是实现爬虫功能的一个软件结构和功能组件集合，简单来说，爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫



****

## 5+2结构：

包含7个部分，5+2结构，其中5个部分是框架的主体部分，另外包含2个中间键

### 5个模块：

1. `engine`
2. `scheduler`
3. `item pipelines`
4. `spiders`
5. `downloader`

### 2个中间键模块：

在`engine`和`spiders`之间以及`engine`和`downloader`之间



## 示意图

![](E:\Notes\WebSpider\04 第四周 网络爬虫之框架\单元10：Scrapy爬虫框架\Scrapy框架.png)

****

## 数据流

在这5个模块之间，数据包括用户提交的网络爬虫请求， 从网络获取的相关内容，在这些结构之间进行流动，形成了数据流

Scrapy框架包含了3条主要的数据流路径：

1. `spiders`经过`engine`到达`scheduler`

   其中`engine`从`spiders`那里获得了爬取用户的请求`requests`，可以理解为一个url，请求到达`engine`之后，`engine`将这个爬取请求转发给了`scheduler`模块，`scheduler`模块负责对爬取请求进行调度。

2. `scheduler`通过`engine`到达`downloader`，`downloader`返回数据经过`engine`到达`spiders`

   首先，`engine`模块从`scheduler`获得下一个要爬取的网络请求，这个网络请求是实际要准备去网络上去爬取的请求，`engine`获得这样的请求之后通过中间键发送给`downloader`模块，`downloader`模块拿到请求之后，真实地连接互联网，并且爬取相关的网页，爬取到网页之后，`downloader`模块将爬取的内容形成一个对象，这个对象叫响应`response`，`downloader`封装完所有信息后，将响应再通过`engine`发送给`spiders`。

3. `spiders`经过`engine`到达`item pipelines`以及`scheduler`

   首先`spiders`处理从`downloader`获得的响应，也就是从网络中爬取的相关内容，处理之后产生了两个数据类型，爬取项`items`以及新的爬取请求`requests`，也就是说我们从网络上获得一个网页之后，如果这个网页中有其它的链接，也是我们感兴趣的，那么可以再`spiders`中增加相关的功能，对新的链接发起再次爬取请求，`spiders`生成两个数据类型之后将它们发送给`engine`，`engine`模块收到两类数据之后，将其中的`items`发送给`item pipelines`，将其中的`requests`发送给`scheduler`进行调度。从而为后期的数据处理以及再次启动网络爬虫请求提供了新的数据来源。



### 理解

在这三条主要数据流中，`engine`模块控制着各个模块的数据流，并且不断地从`scheduler`获得真实要爬取的请求并且将请求发送给`downloader`，整个框架的执行是从向`engine`发送第一个请求开始，到获得所有链接的内容并将内容进行处理后放到`item pipelines`为止。

所以框架的入口是`spiders`，框架的出口是`item pipelines`，在这个框架中，Scrapy是“5+2“结构，其中的`engine`、`schedule`r和`downloader`都是已有的功能实现，用户不需要编写，用户需要编写的是`spiders`模块和`item pipelines`模块，其中`spiders`模块用来向整个框架提供要访问的url链接，同时要解析从网络上获得的页面的内容，而`item pipelines`模块负责对提取的信息进行后处理。

由于在这个框架下，用户编写的并不是完整的大片代码，而仅仅是对`spiders`和`item pipelines`中已有的代码框架或代码模板进行编写，所以，称这种代码编写方式：配置，相当于用户在Scrapy爬虫框架下，经过简单的配置，就可以实现这个框架的运行功能并且最终完成用户的爬取需求。