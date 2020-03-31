[TOC]



# 第四周内容导学

本周介绍`Scrapy框架`，一个专业的网络爬虫框架。

介绍这个框架的基本原理和使用方法以及一个实例



****

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

5. 通过网站`https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted`下载对应版本的`Twisted`

6. 保存到电脑，然后通过`cd `命令找到下载目录下：

   ```python
   >>> pip install Twisted-20.3.0-cp38-cp38-win32.whl
   ```

   安装完成

7. 重新安装Scrapy：

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

![](E:/Notes/WebSpider/04 第四周 网络爬虫之框架/单元10：Scrapy爬虫框架/Scrapy框架.PNG)

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



****

# Scrapy爬虫框架解析

## 框架结构

三个不需要用户修改的模块：

+ `Engine`

  `Engine`模块是整个框架的核心，控制所有模块之间的数据流

  根据条件触发事件

  不需要用户修改



+ `Downloader`

  `Downloader`模块根据用户提供的请求来下载网页

  获得一个请求，并且向网络中提交这个请求并最终获得返回的相关内容

  不需要用户修改



+ `Scheduler`

  `Scheduler`模块对所有的爬取请求进行调度管理的模块

  对于一个中规模的爬虫，一时间有很多对网络的爬取请求，`Scheduler`模块会进行调度，决定哪些请求先访问，哪些后访问

  不需要用户修改



`Downloader Middleware`模块

之前的三个模块都不需要用户修改，这三个模块在一起形成了一个功能：由`scheduler`发送访问请求经过`engine`到达`downloader`。

如果用户希望对这个请求做一定地配置，可以通过`engine`模块和`downloader`模块之间的中间键进行配置

目的：实施`engine`, `scheduler`和`downloader`之间进行用户可配置的控制

功能：修改、丢弃、新增请求或响应

用户可以编写配置代码，不过一般如果没有需要修改`requests`和`response`的时候，可以不更改这个中间键

举例，`scheduler`发送请求要访问百度，用户如果想要修改可以通过`downloader middleware`模块将这个请求拦截下来或者修改为访问雅虎。



`Spiders`

解析downloader返回的响应(`response`)

产生爬取项(`scraped item`)

产生额外的爬取请求(`request`) 

简单来说，`spiders`向整个框架提供了最开始的访问链接，同时对每次爬取回来的内容进行解析，再次产生新的爬取请求，并且从内容中分析出相关的数据。

需要用户编写配置代码



`Item pipelines`

这个模块是以流水线来处理`spiders`产生的爬取项，`spiders`以爬取项的形式向`item pipelines`发送爬取之后的信息，而`item pipelines`以一个个的功能模块来处理，像流水线一样来处理。

由一组操作顺序组成，类似流水线，每个操作是一个`item pipelines`类型

可能的操作包括：清理，检验和查重爬取项中的HTML数据、将数据存储到数据库。

需要用户编写配置代码

用户需要编写的是，对于从网页中提取到的信息，希望怎么处理，以及如何存储数据。



`Spider Middleware`

目的：对`spiders`产生的请求和爬取项的再处理

功能：修改、丢弃、新增请求或爬取项

用户可以编写配置代码



****

重点编写的是`spiders`模块和`item pipelines`模块，如果用户想要对数据流进行控制，可以通过两个中间键对`requests`，`response`和`item`做一定地操作



****

# requests库和Scrapy爬虫的比较

相同点

+ 两者都可以进行页面请求和爬取，Python爬虫的两个重要技术路线
+ 两者可用性都好，文档丰富，入门简单
+ 两者都没有处理JavaScript、提交表单、应对验证码等（需要拓展额外的库）

不同点

| requests                 | Scrapy                                                       |
| ------------------------ | ------------------------------------------------------------ |
| 页面级爬虫               | 网站级爬虫                                                   |
| 功能库                   | 框架                                                         |
| 并发性考虑不足，性能较差 | 并发性好，性能较高 <br>（基于异步结构设计，可以同时向多个网站发起爬取请求） |
| 重点在于页面下载         | 重点在于爬虫结构                                             |
| 定制灵活                 | 一般定制灵活，深度定制困难                                   |
| 上手十分简单             | 入门稍难                                                     |

对于一部分带有反爬功能的网站来说，爬取速度不能太快，不然IP会被屏蔽，所以爬取性能只是一个参数，不是越快越好，要结合特定情况来考虑。



如何选用技术路线

+ 对于非常小的爬取请求，使用requests库
+ 对于不太小的需求，使用Scrapy框架，比如希望对一个网站不间断或持续性地爬取一个网站的信息，并且对爬取到的信息进行积累形成自己的爬取库，这种情况就可以使用Scrapy框架。
+ 对于定制程度更高的需求（不考虑规模），自搭框架，使用requests库比Scrapy库更好



****

# Scrapy爬虫的常用命令

## Scrapy命令行

Scrapy是为持续运行设计的专业爬虫框架，提供操作的Scrapy命令行

在cmd中用`scrapy -h`可以看到Scrapy命令行

Scrapy库的很多的操作包括建立爬虫和运行爬虫都是通过命令行来实现的。



Scrapy命令行的格式：

```scrapy
>scrapy<command>[options][args]
```

6个常用命令：

| 命令         | 说明               | 格式                                        |
| ------------ | ------------------ | ------------------------------------------- |
| startproject | 创建一个新工程     | `scrapy startproect <name>[dir]`            |
| genspider    | 创建一个爬虫       | `scrapy genspider [options] <name><domain>` |
| settings     | 获得爬虫配置信息   | `scrapy settings [opetions]`                |
| crawl        | 运行一个爬虫       | `scrapy crawl <spider>`                     |
| list         | 列出工程中所有爬虫 | `scrapy list`                               |
| shell        | 启动URL调试命令行  | `scrapy shell [url]`                        |

在Scrapy框架下，一个工程是一个最大的单元，工程并不是爬虫，一个工程可以相当于一个大的Scrapy框架，在Scrapy框架中，可以有多个爬虫，每一个爬虫相当于框架中的一个`spiders`模块。

在6个命令中，最常用的是其中的3个命令：

1. startproject
2. genspider
3. crawl



****

Scrapy爬虫并不是给用户操作来使用的，它更多的是一个后台的爬虫框架，所以使用命令行可以方便地让程序员编写自动化的脚本，对爬虫的控制和访问以及对数据的操作会变得更加灵活。

对于程序来讲，它更关心的是一个一个的指令，所以通过命令行，指令就可以被程序接收。所以没有图形界面给用户使用。

本质上，Scrapy是给程序员用的，功能（而不是界面）更重要



****

# 单元小结

## Scrapy框架包含“5+2”结构和3个数据流的路径

![](E:/Notes/WebSpider/04 第四周 网络爬虫之框架/单元10：Scrapy爬虫框架/Scrapy框架.PNG)

 

## Scrapy与requests的不同

小规模--requests库

不太小规模--Scrapy框架



## Scrapy命令行

用户只需要知道基本功能，命令行并不是编程的一部分