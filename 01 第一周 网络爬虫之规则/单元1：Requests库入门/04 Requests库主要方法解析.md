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