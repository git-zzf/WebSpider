[TOC]



# 导论

***Website is the API***

## Requests 库

Python 公认的优秀第三方网络爬虫库

可以自动爬取HTML页面，自动进行网络内容请求的提交

## Robots 协议

网络爬虫盗亦有道

## 5个实战项目

学会使用Requests库



### 三个单元

1. Requests 库的入门
2. Robots协议
3. Requests库爬取实例



****

# 工具的选择

## 文本工具

+ IDLE

  特点：

  1. 适合300行以下的代码编辑
  2. 适合入门

+ Sublime

  特点：

  1. 增强用户编程体验的工具
  2. 丰富的风格和颜色
  3. 专业程序员的选择：
     - 编写代码质量相对较高，对调试需求低，对编程体验要求

## 集成工具 IDE

+ Pycharm

  特点：

  1. 简单，集成度高
  2. 适合较复杂工程 

+ Anaconda

  特点：

  1. 开源免费
  2. 科学计算和数据分析用



****

# Requests库的安装方法

## 安装方法

1. 管理员权限启动cmd

2. 安装：

   ``` pip install requests ```

3. 完成

   ## 测试

   启动IDLE

   ```python
   >>> import requests
   >>> r = requests.get("http://www.baidu.com")
   >>> r.status_code
   200
   >>> r.encoding = 'utf-8'
   >>> r.text
   ```

   ### 7个方法

| 方法                | 说明                                           |
| ------------------- | ---------------------------------------------- |
| requests.requests() | 构造一个请求，支撑以下各方法的基础方法         |
| requests.get()      | 获取HTML网页的主要方法，对应与HTTP的GET        |
| requests.head()     | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| requests.post()     | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()      | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| requests.patch()    | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()   | 向HTML页面提交删除请求，对应于HTTP的DELETE     |



****

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



****

# 爬取网页的通用代码框架

*一组代码，可以准确可靠得爬取网页上的内容*

****

使用request库进行网页访问的时候经常用get函数，requests.get(url) 获得url的相关内容。但是网络连接可能会发生异常，需要进行异常处理。

| 异常                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| requests.ConnectionError  | 网络连接错误异常，如对URL进行DNS查询失败、拒绝连接等         |
| requests.HTTPError        | HTTP协议层面错误异常                                         |
| requests.URL.Required     | URL缺失异常                                                  |
| requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常，通常是对复杂链接访问的时候发生的异常 |
| requests.ConnectTimeout   | 连接远程服务器超时异常                                       |
| requests.Timeout          | 请求URL超时，产生超时异常                                    |

**requests.ConnectTimeout**和**requests.Timeout**区别：

Timeout是指发出URL请求到获得内容的整个过程的超时异常，ConnectTimeout仅指与远程服务器连接过程产生的超时异常

****

## Response对象对于处理异常的方法

| 异常                 | 说明                                    |
| -------------------- | --------------------------------------- |
| r.raise_for_status() | 如果不是200，产生异常requests.HTTPError |

专门处理异常，能够判断返回的response类型r的状态是不是200，如果是200，就会显示返回的内容是正确的，如果不是200，就会产生一个HTTPRError的异常

****

## 通用代码框架

```python
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
```

完整代码

```python
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
```

****

## 使用通用代码框架

 可以有效处理在访问或爬取网页过程中可能出现的错误，或者网络不稳定造成的现象

```python
if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))```
```

正常情况会获得百度首页的HTML代码

```python
if __name__ == "__main__":
    url = "www.baidu.com"
    print(getHTMLText(url))
```

如果去掉`http://`之后，会发生异常，这时候会返回产生异常



****

# HTTP协议及Requests库方法

7个主要方法

| 方法                | 说明                                           |
| :------------------ | :--------------------------------------------- |
| requests.requests() | 构造一个请求，支撑以下各方法的基础方法         |
| requests.get()      | 获取HTML网页的主要方法，对应与HTTP的GET        |
| requests.head()     | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| requests.post()     | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()      | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| requests.patch()    | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()   | 向HTML页面提交删除请求，对应于HTTP的DELETE     |

为了更好理解这些方法，应该了解HTTP协议

## HTTP协议

HTTP，Hypertext Transfer Protocol，超文本传输协议

HTTP是一个基于“请求与响应”模式的、无状态的应用层协议。

+ 用户发出请求，服务器做出响应。

+ 无状态指的是第一次请求和第二次请求之间没有关联。

+ 应用层协议指的是该协议工作在TCP协议之上。

无状态指的是第一次请求和第二次请求之间并没有直接的关联。

应用层协议指的是该协议工作在TCP协议之上。

HTTP协议一般采用URL作为定位网络资源的标识

+ URL格式：`http://host[:port][path]`
+ URL都要以`http://`开头
+ 三个域
  1. host：合法的Internet主机域名或IP地址
  2. port：端口号，可以省略，默认端口号是80
  3. path：请求资源的路径，资源在主机或IP地址的服务器上所包含的内部路径

****

## HTTP URL 实例

`http://www.bit.edu.cn`北京理工大学校园网的首页

`http://220.181.111.188/duty` 指的是这样一台IP主机上duty目录下它的相关资源

****

## HTTP URL的理解

URL是通过HTTP协议存取资源的Internet路径，一个URL对于一个数据资源。 就像电脑中一个文件的路径，只不过这个文件存在Internet上。

## HTTP协议对资源的操作

| 方法   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| GET    | 请求获取URL位置的资源                                        |
| HEAD   | 请求获取URL位置资源的响应消息报告，即获得该资源的头部信息。发现资源很大，无法完全获取，可以用HEAD获取头部信息并分析资源大概的内容 |
| POST   | 请求向URL位置的资源后附加新的数据，不改变现有内容            |
| PUT    | 请求向URL位置存储一个资源，覆盖原URL位置的资源               |
| PATCH  | 请求局部更新URL位置的资源，即改变该处资源的部分内容          |
| DELETE | 请求删除URL位置存储的资源                                    |

网络资源存在云端，URL是这个资源的标识

想要获取资源：

+ 使用GET或HEAD方法，GET获得全部资源，HEAD获得头部信息

 想要放自己的资源：

+ 使用 PUT, POST, PATCH方法

如果想删掉URL对应的现有资源：

+ 使用DELETE

HTTP协议通过URL作定位，通过6个方法管理，每次操作都是独立无状态的。

在HTTP协议的世界里，网络通道和服务器都是黑盒子，能看到的只有URL连接以及对URL连接的相关操作。

## PATCH和PUT的区别

假设在URL位置有一组数据UserInfo，包括UserID、UserName等20个字段

需求：用户只修改了UserName，其余不变 

需要把信息更新到服务器上

+ 可以采用PATCH方法，使用HTTP协议向URL重新提交UsearName
+ 也可以采用PUT方法， PUT方法会覆盖URL位置所对应的资源，所以为了不覆盖这个资源，必须将UsearInfo对应的20个字段同时再次提交到URL对应的位置上，包括UsearName，如果恰巧没有提交其他字段，只提交了UserName，那么URL对应位置上只剩UserName的信息了。

PATCH方法最大的好处：节省网络带宽

如果URL对应的是很庞大的资源时，使用PATCH可以只改一部分，而不需要使用PUT重新提交全部资源。PATCH是HTTP协议改良后的新增指令。

## HTTP协议与Requests库

| HTTP协议方法 |  Requests库方法   | 功能一致性 |
| :----------: | :---------------: | :--------: |
|     GET      |  requests.gets()  |    一致    |
|     HEAD     |  requests.head()  |    一致    |
|     POST     |  requests.post()  |    一致    |
|     PUT      |  requests.put()   |    一致    |
|    PATCH     | requests.patch()  |    一致    |
|    DELETE    | requests.delete() |    一致    |

HTTP协议和Requests库中的方法是一一对应的

### Requests库的head()方法

```python
>>> r = requests.head('http://httpbin.org/get')
>>> r.headers	#展现头部信息的内容
>>> r.text		#发现内容是空
```

head()方法可以用很少的流量来获取网络资源的概要信息

### Requests库的post()方法

```python
>>> payload = {'key1':'value1', 'key2':'vakue2'}	#新建字典
#向URL POST一个字典，自动编码为form（表单）
>>> r = requests.post('http://httpbin.org/post', data = payload)
>>> print(r.text)

#结果
{...
    "form":{
        "key2":"vakue2"
        "key1":"vakue1"
    }
}
```

post()可以向服务器提交新增数据。

key1和key2被放到了form的字段下，说明，我们向URL POST了一个字典或POST了一个键值对的时候，键值对会默认地被存储到表单的字段下。

```python
# 不提交键值对，向URL POST一个字符串，自动编码为data
>>> r = requests.post('http://httpbin.org/post', data = 'ABC')
>>> print(r.text)
#结果
{...
 	"data": "ABC"
    "form": {},
}
```

不提交键值对，提交了一个字符串ABC，发现ABC被存到了data的相关字段下。

post()方法根据用户提交的内容不同，在服务器上会做数据的相关的整理

### Requests库的put()方法

```python
>>> payload = {'key1':'value1', 'key2':'vakue2'}
>>> r = requests.put('http://httpbin.org/post', data = payload)
>>> print(r.text)
{...
    "form":{
        "key2":"vakue2"
        "key1":"vakue1"
    }
}
```

put()方法与post()方法类似，只不过它能将原有的数据覆盖掉



****

# Requests库主要方法解析

| 方法                | 说明                                           |
| ------------------- | ---------------------------------------------- |
| requests.requests() | 构造一个请求，支撑以下各方法的基础方法         |
| requests.get()      | 获取HTML网页的主要方法，对应与HTTP的GET        |
| requests.head()     | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| requests.post()     | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()      | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| requests.patch()    | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()   | 向HTML页面提交删除请求，对应于HTTP的DELETE     |

## request()方法 

requests方法是所有方法中的基础方法

+ 三个参数：method，URL，**kwargs

  - method：通过requests实现的请求方式，对应get/put/post等7种方法

    ```python
    r = requests.request('GET', url, **kwargs)
    r = requests.request('HEAD', url, **kwargs)
    r = requests.request('POST', url, **kwargs)
    r = requests.request('PUT', url, **kwargs)
    r = requests.request('PATCH', url, **kwargs)
    r = requests.request('delete', url, **kwargs)
    r = requests.request('OPTIONS', url, **kwargs)
    ```

    这7个方法就是HTTP协议所对应的请求功能，第7个OPTIONS实际上是向服务器获取一些服务器和客户端能够打交道的参数，并不与获取资源直接相关，因此，在平时使用中用得较少。

    当我们想要实现这7种方法中的一种 ，可以使用request()方法直接实现，也可以用requests库的对应方法，比如说requests.get()，requests.head()等，这些方法是基于request函数之上封装起来的

  - URL：获取页面的URL链接

  - **kwargs：控制访问参数，共13个，均为可选项

    - params：指能够增加到url中的参数。

      例子：

      ``` python
      >>> kv = {'key1': 'value1', 'key2': 'value2'}
      >>> r = requests.request('GET', 'http://python123.io/ws', params=kv)
      >>> print(r.url)
      # 结果
      # http://python123.io/ws?key1=value1&key2=value2
      ```

      建立了一个字典，里面有两个键值对，用GET方法向一个链接请求，同时提供了这个字典作为params相关参数。

      由于访问控制参数是用**开头的，也就是说它是可选的。所以如果想要使用13个字段中的任何一个时，需要用命名方法来调用它的参数，即使用params=kv的方式来调用它。

      这时候如果打印r的URL链接时，发现在给定的URL链接中，后面多了一个问号，问号里有key1=value1&key2=value2，也就是说通过这样一个参数，我们可以把一些键值对增加到URL中，使得URL再去访问时，不止访问到这个资源，而同时带入了一些参数。服务器可以接收这些参数，并根据这些参数筛选部分资源，返回回来。

    + data：字典、字节序列或文件对象，作为Request的内容。重点作为向服务器提供或提交资源时使用。

      例子：

      ```python
      >>> kv = {'key1': 'value1', 'key2': 'value2'}
      >>> r = requests.request('POST', 'http://python123.io/ws', data=kv)
      >>> body = '主体内容'
      >>> r = requests.request('POST', 'http://python123.io/ws', data=body)
      ```

      构造两个键值对，使用POST方法，把它作为data的一部分去提交，这时候，所提交的键值对并不放在URL链接里，而是放在URL链接对应位置的地方作为数据来存储。

      也可以向data域赋值一个字符串，这个字符串就会存到前面URL链接所对应的位置 

    + json：JSON格式的数据，作为Request的内容。

      JSON格式在HTTP，HTML相关的web开发中用到的非常常见，也是HTTP协议最经常使用的数据格式，同样作为内容部分向服务器提交。

      例子：

      ```python
      >>> kv = {'key1': 'value1'}
      >>> r = requests.request('POST', 'http://python123.io/ws', json=kv)
      ```

      构造一个键值对，把它赋值给json参数，那么这个键值对就赋值到服务器的json域上了。

    + headers：字典，HTTP定制头

      实际上是HTTP头的相关域，它对应了向某一个URL访问时所发起的HTTP的头字段。可以使用这个字段来定制访问某一个URL的HTTP的协议头。

      例子

      ```python
      >>> hd = {'user-agent': 'Chrome/10'}
      >>> r = requests.request('POST', 'http://python123.io/ws', headers=hd)
      ```

      我们可以定义一个字典，去修改HTTP协议中的user-agent字段，我们把user-agent变为Chrome/10，那么在访问某一个链接时，我们可以把这样的字段赋值给headers。此时，header再去向服务器访问时，服务器看到的user-agent字段就是Chrome/10，即Chrome浏览器的第10个版本。

      也就是说我们可以模拟任何我们想模拟的浏览器向服务器发起访问。这种模拟浏览器的方法就是在header字段中来实现。

    + cookies：字典或CookieJar，Request中的cookie

      指HTTP协议中解析cookie，可以是字典或者CookieJar的形式

    + auth：元组类型，支持HTTP认证功能。

      cookies和auth字段都是Requests库中的高级功能。

    + files：字典类型，向服务器传输文件时使用的字段。

      例子：

      ```python
      >>> fs = {'file': open('data.xls', 'rb')}
      >>> r = requests.request('POST', 'http://python123.io/ws', files=fs)
      ```

      定义一个字典，用file以对应的文件为键值对。用open的方式打开这个文件，并把 这个文件与file做一个关联，同时对应到相关的URL上。

      通过这样的方法，我们可以向某一个链接提交某一个文件，特定应用时使用。

    + timeout：设定超时时间，单位为秒

      例子：

      ```python
      >>> r = requests.request('GET', 'http://www.baidu.com', timeout=10)
      ```

      当我们发起一个GET请求时，我们可以设一个timeout时间，如果在timeout时间内。我们的请求内容没有返回回来，那么它将产生一个timeout的异常。

    + proxies：字典类型，可以为我们爬取网页设定访问代理服务器，可以增加登录认证。

      例子：

      ```python
      >>> pxs = {'http': 'http://user:pass@10.10.10.1:1234'
             'http':'https://10.10.10.1:1234'	}
      >>> r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)
      ```

      这里我们增加两个代理，一个是http访问时使用的代理，在这个代理中，可以增加用户名和密码的设置，再增加一个是https的代理服务器。这样，在访问百度时，我们所使用的IP地址就是代理服务器的IP地址。

      使用这个字段可以有效地隐藏用户爬取网页的原的IP地址信息。有效地防止对爬虫的逆追踪。

    + allow_redirects：一个开关，True/False，默认为True，重定向开关

    + stream：一个开关，True/False，默认为True，获取内容立即下载开关

    + verify：True/False，默认为True，认证SSL证书开关

    + cert：保存本地SSL证书路径的字段

+ 对于**kwargs的掌握：

  params，data，json，headers需要灵活掌握并且能够在访问网页的时候适当地使用

## get()方法

 `requests.get(url, params=None, **kwargs)`

+ url：获取页面的url链接
+ params：url中的额外参数，字典或字节流格式，可选
+ **kwargs：12个控制访问的参数

## head()方法

` requests.head(url, **kwargs)`

+ url：获取页面的url链接
+ **kwargs：13个控制访问的参数

## post()方法

` requests.post(url, data=None, json=None, **kwargs)`

+ url：获取页面的url链接
+ data：字典、字节序列或文件，Request的内容
+ json：JSON格式的数据，Request的内容
+ **kwargs：11个控制访问的参数

## put()方法

` requests.put(url, data=None, **kwargs)`

+ url：获取页面的url链接
+ data：字典、字节序列或文件，Request的内容
+ **kwargs：12个控制访问的参数

## patch()方法

` requests.patch(url, data=None, **kwargs)`

+ url：获取页面的url链接
+ data：字典、字节序列或文件，Request的内容
+ **kwargs：12个控制访问的参数

## delete()方法

` requests.delete(url, **kwargs)`

+ url：删除页面的url链接
+ **kwargs：13个控制访问的参数

****

在使用后6个方法的时候，由于这些方法会常用到某些访问控制参数，所以就把这样的参数作为一个显示定义的参数量放在函数的设计里面，而那些不是特别常用的都放到了可选的访问控制参数字段里面。

****

## 最常用的方法--get()方法 

`requests.get(url, params=None, **kwargs)`

+ url：获取页面的url链接
+ params：url中的额外参数，字典或字节流格式，可选
+ **kwargs：12个控制访问的参数

在HTTP协议中，向某一个URL去提交资源的功能在服务器上是严格受控的，这里面有很大的安全问题，如果某一个URL是允许任何用户无限制地向上传输相关资源，那么就会出现很多问题，比如，我们可以用大量的垃圾信息使得服务器的资源消耗完，甚至我们可以传输一些不可控的，或恶意的内容到某一URL上，这都是对网络空间不负责任的表现。

因此，当我们使用requests库的时候，最常使用的就是get()方法，也就是说我们通过get()方法来爬取一些内容，并且部分地向服务器提交一些内容。



****

# 单元小结

## Requests库的7个方法

| 方法                | 说明                                           |
| ------------------- | ---------------------------------------------- |
| requests.requests() | 构造一个请求，支撑以下各方法的基础方法         |
| requests.get()      | 获取HTML网页的主要方法，对应与HTTP的GET        |
| requests.head()     | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| requests.post()     | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()      | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| requests.patch()    | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()   | 向HTML页面提交删除请求，对应于HTTP的DELETE     |

事实上，由于网络安全的限制，我们很难向一个URL去发起post()，put()，patch()和delete()的请求。而request()方法又是一个基础方法。

因此，真正使用Requests库，如果作为爬虫功能来讲，最常使用的功能就是get()。对于某些特别大的链接，我们使用head()方法来获得它的资源概要。

因此，对于Requests库来讲，重点掌握get()和head()两个方法就可以。

## 爬取网页的通用代码框架

```python
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
```

通过try和except来实现的代码组织。

***网络连接有风险，异常处理很重要***

一定要用try和except方式来保证连接它的异常能够被有效处理。

在通用代码框架中，一行核心代码是：

`r.raise_for_status()`

也就是response对象的raise_for_status()函数，这个方法的作用是：如果返回的对象，它的状态码不是200，就是说信息没有正确获得，它将产生一次异常。所以，except就能捕获到所有网络连接错误时的异常。