[TOC]



# 实例1：京东商品页面的爬取

```python
>>> import requests
>>> r = requests.get("链接地址")
>>> r.status_code
200
>>> r.encoding
'gbk'
>>> r.text[:1000]
```

## 全代码

```python
import requests
url = "https://item.jd.com/100009177368.html"
try:
	r = requests.get("url")
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
    print("爬取失败")
```



****

# 实例2：亚马逊商品页面的爬取

## 直接爬取

```python
>>> import requests
>>> r = requests.get("https://www.amazon.cn/dp/B01FLG4O04")
>>> r.status_code
503
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = r.apparent_encoding
>>> r.text
```

返回的503，说明遇到了问题

网站可以通过判断头来判断访问是谁发起的，网站处理的是通过浏览器访问的请求，如果是对于爬虫的请求，网站可以拒绝

## 查看头信息

通过r.request.header查看发给亚马逊的头部是什么内容

```python
>>> r.request.headers
{'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
```

在User-Agent中写着python-requests，说明我们的爬虫告诉亚马逊，这次访问是由程序产生的。亚马逊就可以使这样的访问变成错误。

## 更改头信息

```python
>>> kv = {'user-agent':'Mozilla/5.0'} 
```

重新定义user-agent的内容，使它等于Mozilla/5.0，这时候的user-agent可能是一个浏览器，可能是火狐，可能是Mozilla或者是IE10。因为Mozilla/5.0是一个很标准的浏览器身份标识的字段。

```python
>>> kv = {'user-agent':'Mozilla/5.0'} 
>>> url = "https://www.amazon.cn/dp/B01FLG4O04"
>>> r = requests.get(url, hearders = kv)
>>> r.status_code
200
```

这时候返回变成了200，说明现在获得了产品页面

```python
>>> r.request.headers
{'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
```

这时候的user-agent已经被改成了Mozilla/5.0

```python
>>> r.text
```

这时候可以看到商品信息了

****

## 全代码

```python
import requests
url = "https://www.amazon.cn/dp/B01FLG4O04"
try:
    kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get("url", heards = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
except:
    print("爬取失败")
```

****

实际中遇到验证码检测



****

# 实例3：百度/360关键词提交

*向百度和360搜索引擎提交关键词并获得搜索结果*

## 搜索引擎关键词提交接口

百度的关键词接口：

`http://www.baidu.com/s?wd=keyword`

360的关键词接口：

`http://www.so.com/s?q=keyword`

只要替换keyword就可以提交关键词了

## 实现

```python
>>> import requests
```

### 修改URL

使用params字段修改url。首先构造一个键值对，搜索"python"

```python
>>> kv = {'wd':'Python'}
>>> r = requests.get("http://www.baidu.com/s", params = kv)
>>> r.status_code
```

返回200，说明请求已经被提交了url

### 查看URL

现在可以查看，提交给百度的url是什么

使用response对象中包含的request信息

```python
r.request.url
```

看到现在的url已经是符合百度关键词接口的url了

+ 实际返回了百度安全验证

kv键值对wd:Python中的wd是搜索引擎的表示，Python是关键词

### 查看内容

看下返回内容的长度

```python
len(r.text)
```

返回302829，也就是返回了300多k的信息。

+ 实际返回1519

****

## 全代码

### 百度

```python
import requests
keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
```

实际中遇到百度安全验证

### 360

```python
import requests
keyword = "Python"
try:
    kv = {'q': keyword}
    r = requests.get("http://www.so.com/s", params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
```



****

# 实例4：网络图片的爬取和储存

## 网络图片链接的格式

`http://www.example.com/picture.jpg`

前面是URL，结尾是picture.jpg

### 例子：国家地理	

`http://www.nationalgeographic.com.cn/`

选择一个图片web页面：

`http://www.nationalgeographic.com.cn/photography/photo_of_the_day/3921.html`

这张图片是这样的格式：

`http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg`

如果一个URL链接是以.jpg结尾说明它就是一个图片链接，而且它是一个文件，所以我们需要用程序把它爬取并保存下来。

## 实践

### 获取图片

```python
>>> import requests
```

需要描述把图片保存在本机的什么位置

假设保存到E盘，保存为abc.jpg这个文件

这个名字后期会做相关处理

```python
>>> path = "E:/Notes/WebCrawler/第一周 网络爬虫之规则/单元3：Requests库网络爬虫实战（5个实例）/实例4图片/abc.jpg"
```

给出查到的网络图片的地址

```python
>>> url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
```

用get请求来捕获url

```python
>>> r = requests.get(url)
>>> r.status_code
200
```

显示200说明保存成功

### 保存图片

图片是一个二进制格式，保存二进制格式文件为图片

```python
>>> with open(path, 'wb') as f:
    	f.write(r.content)
```

打开一个文件，即我们要存储的abc.jpg并且把它定义为一个文件标识符f

任何我们将返回的内容写到这个文件中

response对象返回的内容中，r.content表示返回内容的二进制形式。所以我们可以用f.write(r.content)将返回的二进制形式写到文件中。

最后, 我们将文件关闭

```python
>>> f.close()
```

去E盘看下这个文件

<img src="E:/Notes/WebSpider/01 第一周 网络爬虫之规则/单元3：Requests库网络爬虫实战（5个实例）/实例4图片/abc.jpg" style="zoom: 25%;" />

****

## 图片爬取全代码

```python
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "E:/Notes/WebCrawler/第一周 网络爬虫之规则/单元3：Requests库网络爬虫实战（5个实例）/实例4图片/" 
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
              
```

`path = root + url.split('/')[-1]`表示本地目录加上正斜杠分割的最后一部分，即文件名，这样就不用加文件名了，保存的文件名称就是原名称。

地址用/分割就可以了，不需要//

```python
if not os.path.exists(root):
        os.mkdir(root)
```

查看根目录是否存在，如果不存在，建立一个目录。

```python
if not os.path.exists(path):
        r = requests.get(url)
        withopen(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
```

接下来查看文件是否存在，如果不存在，就通过request下载文件，如果存在，就打印”文件已存在“

### 代码的可靠和稳定性

要考虑可能出现的问题，并能做相关处理



****

# 实例5:  IP地址归属地的自动查询

## 通过iP138网站查询

接口形式：

`http://m.ip138.com/ip.asp?ip=ipaddress`

## 实现

```python
>>> import requests
>>> url = "http://ip138.com/iplookup.asp?ip="
>>> kv = {'user-agent':'Mozilla/5.0'}
>>> r = requests.get(url + '202.204.80.112'+'&action=2',headers = kv)
>>> r.status_order
>>> r.text[7000:7500]
```

查询最后500个字节

## 全代码

```python
import requests
url = "http://ip138.com/iplookup.asp?ip="
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url + '202.204.80.112'+'&action=2',headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[7000:7500])
except:
    print("爬取失败")

```

网站以文本框提交按钮的形式，都是以链接的形式提交的。只要通过浏览器的解析，知道向后台提交的链接形式，就可以用Python代码模拟。

实际中需要伪装头信息

55.55.55.55 美国   弗吉尼亚美国陆军部队IP地址



****

# 单元小结

## 5个requests库的爬取实例

实例1：京东，直接爬取

实例2：亚马逊，模拟浏览器

实例3：百度/360搜索关键字提交

实例4：图片爬取

实例5:  IP地址归属地查询，利用网站接口查询