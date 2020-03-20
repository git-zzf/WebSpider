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