[TOC]

# Scrapy爬虫的第一个实例

网站地址：`http://python123.io/ws/demo.html`

文件名称：demo.html



## 使用Scrapy库

### 步骤一：建立一个Scrapy爬虫工程，选择一个目录，执行命令

```cmd
>>> e:
>>> cd E:\Notes\WebSpider\04 第四周 网络爬虫之框架\单元11：Scrapy爬虫基本使用
>>> scrapy startproject python123demo

New Scrapy project 'python123demo', using template directory 'c:\users\administrator\appdata\local\programs\python\python38-32\lib\site-packages\scrapy\templates\project', created in:
    E:\Notes\WebSpider\04 第四周 网络爬虫之框架\单元11：Scrapy爬虫基本使用\python123demo

You can start your first spider with:
    cd python123demo
    scrapy genspider example example.com
```

发现在目标文件夹中生成了一些文件，逐一介绍这些文件以及其中包含子目录的作用：

生成的工程目录：

`python123demo/`：外层目录

​	`scrapy.cfg`：部署Scrapy爬虫的配置文件，部署指的是把爬虫放到服务器上，并在服务器配置好相关的操作接口。对于本机使用的爬虫来说，不需要改变部署的配置文件。

​	`python123demo/`：Scrapy框架对应的所有文件所在的目录，Scrapy框架的用户自定义Python代码，包含几个`.py`文件：

​		`__init__.py`:初始化脚本，用户不需要编写

​		`items.py`：对应的是爬取项`items`类的代码模板，需要继承Scrapy库提供的`items`类（继承类），不需要用户编写。

​		`middlewares.py`：`Middlewares`代码模板（继承类），用户可以修改用来拓展`Middlewares`的功能

​		`pipelines.py`：框架中的`pipelines`模块的代码模板

​		`settings.py`：Scrapy爬虫的配置文件，修改文件来优化爬虫功能

​		`spiders/`：`Spiders`代码模板目录（继承类），存放的是`python123demo`这个工程中所建立的爬虫，其中的爬虫需要符合爬虫模板的约束。包含两个文件：

​			`__init__.py`：初始文件，无需修改

​			`__pycache__/`：缓存目录，无需修改



### 步骤二：在工程中产生一个Scrapy爬虫，通过一条命令实现，包含爬虫的名字和爬取的网站

生成一个名称为demo的spider 

```cmd
>>> e:
>>> cd E:\Notes\WebSpider\04 第四周 网络爬虫之框架\单元11：Scrapy爬虫基本使用\python123demo
>>> scrapy genspider demo python123.io
Created spider 'demo' using template 'basic' in module:
  python123demo.spiders.demo
>>>
```

现在，在`spiders/`目录下，增加了一个文件`demo.py`，除了用命令生成这个文件，也可以人工生成。

`demo.py文件`：

```python
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/']

    def parse(self, response):
        pass

```

其中有一个面向对象的类`DemoSpider`，这个类的名字可以任意命名，不过这个类需要继承于`scrapy.Spider`类，是它的子类。

`name`：当前爬虫的名字

`allowed_domain`：用户提交给命令行的域名，指的是用户在爬取网站的时候，只能爬取这个域名以下的相关链接

`start_urls`：Scrapy框架爬取的初始页面

`parse()`：解析页面的方法，现在是空的，用于处理响应，解析爬取到的内容形成字典类型，同时可以发现网络中爬取的内容中隐含的新的需要爬取的url。



### 步骤三：配置产生的spider爬虫

修改`demo.py`文件，使它能够按照要求访问我们需要的链接，并爬取其中的内容。

在这里，我们希望的解析功能是：将返回的HTML页面存成文件。

修改`demo.py`文件：

```python
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/']

    def parse(self, response):
        pass

```

不需要`allowed_domains = ['python123.io']`，注释掉这一行

```python
 # allowed_domains = ['python123.io']
```

修改`start_urls`，改为`http://python123.io/ws/demo.html`

```python
start_urls = ['http://python123.io/ws/demo.html']
```

更改爬取方法的具体功能，包含两个参数：

1. `self`：面向对象类所属关系的标记
2. `response`：从网络中返回内容的对象，在这里，需要将`response`中的内容写到一个HTML文件中。

首先，定义文件名：

```python
fname = response.url.split('/')[-1]
```

从网页地址中提取文件名字做为保存为本地的文件名。

保存返回的内容到这个文件中：

```python
with open(fname, 'wb') as f:
    f.write(response.body)
self.log('Saved file %s.' % name)
```

这一步之后，`demo.py`文件就能够爬取一个网页，并且能够将网页的内容保存为一个HTML文件

全代码：

```python
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
        f.write(response.body)
        self.log('Saved file %s.' % name)

```





### 步骤4：运行爬虫，获取网页

在命令行执行命令：

```cmd
>>> scrapy crawl demo
```

这样，`demo`爬虫被执行，捕获的页面存储在`demo.html`文件中





`demo.py`文件中的代码是简化版的代码，与之对应的完整版代码是：

```python
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    
	def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Requests(url=url, callback=self.parse)

            
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
        f.write(response.body)
        self.log('Saved file %s.' % name)

```

在完整版代码中，除了`parse()`方法之外，还有一个`start_requests()`方法，比较两个文件的这个方法：

```python
class DemoSpider(scrapy.Spider):
    name = 'demo'
    start_urls = ['http://python123.io/ws/demo.html']
```

以及

```python
class DemoSpider(scrapy.Spider):
    name = 'demo'
    
	def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Requests(url=url, callback=self.parse)
```

简化版的`demo.py`文件通过`start_urls`列表给出初始的url链接。

而Scrapy库支持另一种等价的写法也就是使用一个`start_requests()`方法，在这个方法中，首先定义了一个`urls`列表，并且对列表中的每一个列表通过`yield scrapy.Requests()`向`engine`提出了url访问请求。



****

# yield关键字的使用

*`yield`是Python3的33个关键字中的一个*

## yield关键字

`yield`--生成器

+ 生成器是一个不断产生值的函数

+ 如果一个函数包含`yield`语句，那这个函数就是一个生成器

+ 生成器每次产生一个值（`yield`语句），函数被冻结。直到函数被再次唤醒后再产生一个新的值，而生成器使用的局部变量的值和冻结之前的值是一致的。简单来说，一个函数执行到某一个位置，产生了一个值，然后被冻结，再次被唤醒的时候继续从同样的位置执行

  

## 实例：

```python
>>> def gen(n):
    for i in range (n):
        yield i**2
```

这里有一个函数`gen(n)`，它能产生所有小于n的整数的平方值。每次函数运行到`yield`语句的时候，都会返回一个迭代值（查看迭代值，需要使用for循环），然后从`yield`语句的下一行`i = i+1`继续执行。

使用`gen(n)`函数，需要使用for循环：

```python
>>> for i in gen(10):
    print(i, end=' ')

0 1 4 9 16 25 36 49 64 81 
```

`gen(n)`函数每生成一个值，`print()`函数就会打印一次，然后`gen(n)`函数再产生下一个值。



对于同样的求平方的例子，普通的写法可以是：

```python
>>> def square(n):
    ls = [i**2 for i in range(n)]
    return ls

>>> for i in square(10):
    print(i, end=' ')

0 1 4 9 16 25 36 49 64 81 
```



### 生成器和普通写法的区别

这里普通写法指的是，把所有可能的值全部计算出来，并且通过一个列表返回给上层的调用函数。

与普通写法相比，生成器的优势：

+ 更节省储存空间
+ 响应更迅速
+ 使用更灵活

对于普通方法来说，如果求平方的数量是1百万个数字，那么需要很大的内存空间来保存列表，这样的话速度就会变慢。

而使用生成器，没调用一次的时候，只产生一个值，这个值返回之后才再次调用函数，产生第二个值，所以即使`n=1M`，对于生成器来讲也只需要一个值的存储空间。

所以，在数据规模很大的时候，生成器有很明显的显示空间的优势。





## demo.py

完整版：

```python
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    
	def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Requests(url=url, callback=self.parse)

            
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
        f.write(response.body)
        self.log('Saved file %s.' % name)

```

在这段代码中，使用生成器`yield`语句，每次从列表中取出一个url链接，然后返回一个结果，再调用下一个url链接。

这样做之后，当我们有一百万个链接的时候，这样的写法可以非常有效地使用计算资源。



****

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



****

# 单元小结



## Scrapy爬虫的基本使用

+ 介绍了`Scrapy`爬虫的第一个实例及爬虫生成的目录结构
+ 讲解了`yield`关键字和生成器
+ 介绍了`Request`类，`Response`类，`Item`类，以及这些类的基本属性和方法
+ 介绍了`CSS Selector`的基本使用