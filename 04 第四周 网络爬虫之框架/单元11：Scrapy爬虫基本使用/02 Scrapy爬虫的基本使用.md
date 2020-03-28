# Scrapy爬虫的基本使用

## Scrapy爬虫的使用步骤

步骤一：创建一个工程和`Spider`模板

步骤二：编写`Spider`

步骤三：编写`Item Pipeline`

步骤四：优化配置策略



## Scrapy爬虫的数据类型

`Request`类：向网络上提交请求的内容

`Response`类：从网络中爬取内容的封装类

`Item`类：由`Spider`产生的信息封装的类





## Request类

`class scrapy.http.Request()`

+ 表示的是一个`Request`对象，一个HTTP请求

+ 由`Spider`生成，由`Downloader`执行



Request类的6个常用属性和方法：

| 属性或方法 | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| .url       | Request对应的请求URL地址                                     |
| .method    | 对应的请求方法，'GET''POST'等                                |
| .headers   | 字典类型风格的请求头                                         |
| .body      | 请求内容主体，字符串类型                                     |
| .meta      | 用户添加的扩展信息，在Scrapy内部模块间传递信息使用，爬取不需要使用 |
| .copy()    | 复制该请求                                                   |





## Response类

`class scrapy.http.Response()`

+ `Response`对象表示一个HTTP响应
+ 由`Downloader`生成，由`Spider`处理



包含7个常用的属性和方法：

| 属性或方法 | 说明                               |
| ---------- | ---------------------------------- |
| .url       | Response对应的请求URL地址          |
| .status    | HTTP状态码，默认是200              |
| .headers   | Response对应的头信息               |
| .body      | Response对应的内容信息，字符串类型 |
| .flags     | 一组标记                           |
| .request   | 产生Response类型对应的Request对象  |
| .copy()    | 复制该响应                         |

在这里Request和Response的属性方法和Requests库很相似，这是因为Scrapy库和Requests库都是对HTTP请求做处理和响应，而HTTP相应的字段是相对固定的





## Item类

`class scrapy.item.Item()`

+ `Item`对象标识一个从HTML页面中提取的信息内容
+ 由`Spider`生成，由`Item Pipeline`最终处理

+ `Item`是一个类字典类型，可以按照字典类型操作

由`Spider`对HTML页面进行解析可以解析出很多内容，而`Item`类是这些信息中非常特殊的一种，在`Scrapy`框架下，`Item`类是以字典类型来定义的

在`Scrapy`框架下，`Spider`会从网页中获取信息，并把这些信息生成键值对，并且封装成字典。这种字典就是`Item`类。





## Scrapy爬虫提取信息的方法

这些方法主要应用在`Spider`模块下，也就是`Spider`用来解析HTML页面的方法。

这些提取方法通过使用：

+ BeautifulSoup类
+ lxml类
+ re库
+ Xpath Seletor
+ CSS Selector

对于`Spider`来讲，对于获得的网页信息，有很多种处理方法，可以用上面提到的5个提取方法，也可以用其它方法，这些方法的好处是可以简化信息提取的过程。





## CSS Selector的基本使用

`CSS Selector`是一种国际公认的`HTML`页面的信息提取方法

`CSS Selector`的使用格式：

```css
<HTML>.css('a::attr(href)').extract()
```

我们可以在一个`HTML`的变量后面使用`.css()`方法，通过输入标签名称`a`，标签属性`href`来获得对应的标签信息

`CSS Selector`由W3C组织维护并规范，W3C组织是国际公认的，权威的推进HTML页面标准化的组织，所以这个方法在`Scrapy`框架中应用非常广泛。