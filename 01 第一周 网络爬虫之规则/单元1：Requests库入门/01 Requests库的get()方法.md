# Requests库的get()方法

` r = requests.get(url)`		获得网页最简单的代码

+ 构造一个向服务器请求资源的Request对象
  + 这里的Request的R要大写
+ 返回一个包含服务器资源的Response对象
  + 用变量r表示

++++

`requests.get(url, params = None, **kwargs)`

+ request的get函数的完整使用方法有三个参数
  1. url  
     + 获得页面的url链接
  2. params
     + url中增加的额外参数，可以是字典或者字节流格式，可选
  3. **kwargs
     + 12个控制访问的参数，可选

+ get函数使用了request的方法来封装
  + request库中的7个方法，除了第一个request方法是基础方法外，其余6个方法都是通过调用request方法来实现的。
    + 意思就是，request库只有一个方法，就是request方法，为了编程方便，所以提供了6个方法。

+ Request库的两个重要对象，` r = requests.get(url)`
  1. Request
  2. Response：重中之重，获得网络内容相关
     + 包含了爬虫返回的全部内容

****

## Response 对象

### 之前的例子

`import requests`

+ 调用库

`r = requests.get("http://www.baidu.com")`

+ 用get方法访问百度主页

`r.status_code`

+ 检测请求的状态码
  + 如果状态码是200 --> 访问成功
  + 如果不是200 --> 访问失败

`type(r)`

+ 检测r的类型
  + 返回的类的名字 -- Response

`r.headers`

+ 返回get请求获得页面的头部信息



### Response对象的属性

|        属性         |                         说明                          |
| :-----------------: | :---------------------------------------------------: |
|    r.status_code    | HTTP请求的返回状态，200表示连接成功，不是200就是失败  |
|       r.text        |     HTTP响应内容的字符串形式，url页面的字符串形式     |
|     r.encoding      | 网页的编码方式，从HTTP header中猜测的响应内容编码方式 |
| r.apparent_encoding |   从内容中分析出的响应内容编码方式（备选编码方式）    |
|      r.content      |    HTTP响应内容的二进制形式，如图片的二进制的表示     |



### 使用get()方法获取网上资源的流程

1. 用`r.status_code`检查返回的response对象的状态
2. 如果返回200，就用`r.text` ，`r.encoding`， `r.apparent_encoding`， `r.content` 等去解析返回的内容。 
3. 如果返回的状态码是404或其他，说明这次访问出错或产生异常了



****

### 例子

```python
>>> import requests
>>> r = requests.get("http://wwwbaidu.com")
>>> r.status_code
200
>>> r.text
# 发现是乱码
>>> r.encoding # 看编码是什么
'ISO-8859-1'
>>> r.apparent_encoding
'utf-8'
>>> r.encoding = 'utf-8' # 用utf-8替换
>>> r.text
# 发现看到中文字符
```

****

### 理解Response的编码

*了解两种编码的区别*

|        属性         |                         说明                          |
| :-----------------: | :---------------------------------------------------: |
|     r.encoding      | 网页的编码方式，从HTTP header中猜测的响应内容编码方式 |
| r.apparent_encoding |   从内容中分析出的响应内容编码方式（备选编码方式）    |

网络上的资源有它的编码，如果没有编码，人就不能读懂内容

**r.encoding**编码方式是从**HTTP header**中的**charset**字段获得的，如果**HTTP header**中有这样的字段，说明我们访问的服务器对它资源的编码是有要求的，这样的编码会被获得并存到 **r.encoding**中。

但是并不是所有的服务器对它的资源编码都有相关要求，所以 如果当header中不存在**charset**字段，则默认编码为**ISO-8859-1**。

访问百度的时候返回的就是这样的编码，但是，这种编码无法解析中文。所以，**request**库提供了另外一个备选编码，**r.apparent_encoding**，这种编码不是根据**HTTP**的头部分，而是根据内容部分，去分析其中出现文本的可能的编码方式。

 原则上来说，**apparent_encoding **的编码比**encoding**更准确，因为**encoding**并没有分析内容，只是从**header**的相关字段中提取编码。而**apparent_encoding**却是分析内容并且找到其中可能的编码。所以当使用**encoding**不能正确解码返回内容时，要使用**apparent_encoding**来解析相关的编码信息，所以当把**apparent_encoding**赋给**encoding**之后，就可以读到**r.text**中的中文。

