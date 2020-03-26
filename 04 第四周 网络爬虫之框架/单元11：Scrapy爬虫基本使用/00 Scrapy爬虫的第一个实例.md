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



 

