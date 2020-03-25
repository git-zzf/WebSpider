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