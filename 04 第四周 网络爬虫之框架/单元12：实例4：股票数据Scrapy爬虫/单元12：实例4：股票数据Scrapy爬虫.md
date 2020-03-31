[TOC]

# “股票数据Scrapy爬虫”实例介绍

## 功能描述：

+ 技术路线：Scrapy框架
+ 目标：获取上交所和深交所所有股票的名称和交易信息
+ 输出：保存到文件中

数据网站

获取股票列表：

​	东方财富网：`http://quote.eastmoney.com/stock_list.html`

获取个股信息：

​	雪球网：`https://xueqiu.com/S/SZ000651`





## 回顾框架结构

首先需要在框架中编写一个爬虫程序，即编写一个`Spider`，它需要具备链接爬取和网页解析的功能。

同时也需要编写`PipeLines`来处理解析后的股票数据，并将这些数据存储到文件中



****

# “股票数据Scrapy爬虫”实例编写

网站：

获取股票列表：

​	东方财富网：`http://quote.eastmoney.com/stock_list.html`

获取个股信息：

​	老虎网：`https://www.laohu8.com/stock/000651`，老虎网的链接不包含两个字母股票代码

## 步骤

步骤1：建立工程和`Spider`模板

步骤2：编写`Spider`

步骤3：编写`Item Pipelines`



## 建立工程和Spider模板

```command
\>scrapy startproject GStocks
\cd BaiduStocks
\>scrapy genspider stocks baidu.com
进一步修改spiders/stocks.py文件
```



## 编写Spider

配置`stocks.py`文件

修改对返回页面的处理

修改对新增URL爬取请求的处理

```python
# -*- coding: utf-8 -*-
import scrapy


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['laohu8.com']
    start_urls = ['https://www.laohu8.com']

    def parse(self, response):
        pass

```



修改初始链接：东方财富网的股票列表

爬取股票列表，对结果做相关的解析，从股票列表的中找到每一个股票的代码并且生成与“老虎网”相关的url链接

```python
start_urls = ['http://quote.eastmoney.com/stock_list.html']
```

在`parse()`函数中定义一个`for`循环，提取网页中所有`a`标签的链接，使用`CSS Selector`来提取信息，查找标签名为`a`，标签属性是`href`的标签的信息。

```python
def parse(self, response):
    for href in response.css('a::attr(href)').extract():
        pass
```



构造`try...except`结构，如果一个链接报错，可以继续进行下一个，使程序关注在正确的链接爬取上，对于错误的链接使用`except`处理。

```python
def parse(self, response):
    for href in response.css('a::attr(href)').extract():
        try:
            pass
        except:
            pass

```



使用正则表达式查找股票列表中的股票代码，只需要数字

```python
stock = re.findall(r'\d{6}', href)[0]
```



生成老虎网对应股票的链接。

```python
url = 'https://www.laohu8.com/stock/' + stock
```



用`yield`关键字让`parse`变成一个生成器，伪装头信息成浏览器，不然会报错403

```python
yield scrapy.Request(url, headers={'User-Agent': "Mozilla/5.0"}, callback=self.parse_stock)
```

这里的第二个参数`callback`给出了处理这个`url`对应响应的处理函数，定义为`parse_stock()`

最后加上`except`部分。



### `parse()`部分全代码：

```python
	def parse(self, response):
		for href in response.css('a::attr(href)').extract():
			try:
				stock = re.findall(r'\d{6}', href)[0]
				url = 'https://www.laohu8.com/stock/' + stock
				print(url)
				yield scrapy.Request(url, headers={'User-Agent': "Mozilla/5.0"}, callback=self.parse_stock)
			except:
				continue

```



### 编写函数`parse_stock()`

作用是从老虎网提取单个股票信息的方法：

建立保存信息的字典：

```python
infoDict = {}
```



通过分析`html`页面，发现所有股票信息都存在`<div>`标签下，这个`<div>`标签的类名是：`class = "stock-info"`，所以首先找到这个标签：

```python
stockInfo = response.css('.stock-info')
```



从`html`页面中，发现股票名称保存在`h1`标签下，搜索整个`html`页面，发现`<h1>`标签只出现一次，所以可以直接定位到该标签，通过`extract()`取出标签中的信息（文本信息），因为搜索到的结果是以列表保存的，使用`[0]`把列表去掉，只留下文本：

```python
name = stockInfo.css('h1').extract()[0]
```



把所有的股票信息的标题和值都保存在列表中，股票信息标题保存在`<dt>`标签下，股票信息内容保存在`<dd>`标签下：

```python
keyList = stockInfo.css('dt').extract()
valueList = stockInfo.css('dd').extract()
```



保存股票信息，使用`for`循环把所有股票信息保存在字典中。使用正则表达式把文本信息筛选出来，[1:-5]表示选出第1个到倒数第5个的字符（结果中不包含倒数第5位置的字符），对于`value`变量也同理，如果网页中的`value`部分不存在，所以用`try...except`框架：

```python
for i in range(len(keyList)):
			key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
			try:
				value = re.findall(r'dd>.*</dd>', valueList[i])[0][3:-5]
			except:
				value = '--'
			infoDict[key] = value
```



把股票名称的信息添加到字典中：

```python
infoDict.update({'股票名称': re.findall(r'>.*</h', name)[0][1:-3]})
```



使用`yield`使得每保存一条信息就返回一次值给上层调用者：

```python
yield infoDict
```



### `parse_stock()`全代码：

```python
def parse_stock(self, response):
		infoDict = {}
		stockInfo = response.css('.stock-info')
		name = stockInfo.css('h1').extract()[0]
		keyList = stockInfo.css('dt').extract()
		valueList = stockInfo.css('dd').extract()
		for i in range(len(keyList)):
			key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
			try:
				value = re.findall(r'dd>.*</dd>', valueList[i])[0][3:-5]
			except:
				value = '--'
			infoDict[key] = value

		infoDict.update({'股票名称': re.findall(r'>.*</h', name)[0][1:-3]})
		yield infoDict
```





### `stock.py`全代码：

```python
# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
	name = 'stocks'
	start_urls = ['http://quote.eastmoney.com/stock_list.html']


	def parse(self, response):
		for href in response.css('a::attr(href)').extract():
			try:
				stock = re.findall(r'\d{6}', href)[0]
				url = 'https://www.laohu8.com/stock/' + stock
				print(url)
				yield scrapy.Request(url, headers={'User-Agent': "Mozilla/5.0"}, callback=self.parse_stock)
			except:
				continue


	def parse_stock(self, response):
		infoDict = {}
		stockInfo = response.css('.stock-info')
		name = stockInfo.css('h1').extract()[0]
		keyList = stockInfo.css('dt').extract()
		valueList = stockInfo.css('dd').extract()
		for i in range(len(keyList)):
			key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
			try:
				value = re.findall(r'dd>.*</dd>', valueList[i])[0][3:-5]
			except:
				value = '--'
			infoDict[key] = value

		infoDict.update({'股票名称': re.findall(r'>.*</h', name)[0][1:-3]})
		yield infoDict

```



## 编写Pipelines

打开`pipelines.py`

编辑`GetstocksInfoPipeline()`类，包含3个方法：



打开文件：

```python
def open_spider(self, spider):
		self.f = open('GetStockInfo.txt', 'w')
```



关闭文件：

```python
def close_spider(self, spider):
		self.f.close()
```



### `process_item()`函数

写入文件：

```python
def process_item(self, item, spider):
		try:
			line = str(dict(item)) + '\n'
			self.f.write(line)
		except:
			pass
		return item
```



全代码：

```python
class GetstocksInfoPipeline(object):
	def open_spider(self, spider):
		self.f = open('GetStockInfo.txt', 'w')


	def close_spider(self, spider):
		self.f.close()


	def process_item(self, item, spider):
		try:
			line = str(dict(item)) + '\n'
			self.f.write(line)
		except:
			pass
		return item
```





## 修改设置，调用`GetstocksInfoPipeline()`类

修改`settings.py`文件，找到`ITEM_PIPELINES`的一行，改成`Item Pipelines`的类名

```python
ITEM_PIPELINES = {
    'GetStocks.pipelines.GetstocksInfoPipeline': 300,
}
```





## 运行爬虫

在`cmd`命令中，首先切换到对应的工程目录下。

然后运行`scrapy crawl stocks`，这里`stocks`是在`stocks.py`文件中定义的`name`变量的名字。

```cmd
>>> e:
>>> cd e:/......
>>> scrapy crawl stocks
```

等待运行



## 查看结果

结果保存在工程文件夹下



****

# “股票数据Scrapy爬虫”实例优化

进一步提高Scrapy爬虫的爬取速度

依靠Scrapy框架提供的参数：

配置并发连接选项，`settings.py`文件

| 选项                           | 说明                                             |
| ------------------------------ | ------------------------------------------------ |
| CONCURRENT_REQUESTS            | `Downloader`最大并发请求下载数量，默认32         |
| CONCURRENT_ITEMS               | `Item Pipeline`最大并发ITEM处理请求数量，默认100 |
| CONCURRENT_REQUESTS_PER_DOMAIN | 每个目标域名最大的并发请求数量，默认8            |
| CONCURRENT_REQUESTS_PER_IP     | 每个目标IP最大的并发请求数量，默认0，非0有效     |

这四个并发连接配置参数可以提高性能。

`CONCURRENT_REQUESTS`：`Downloader`同时访问的连接数，并下载内容

`CONCURRENT_REQUESTS_PER_DOMAIN`和`CONCURRENT_REQUESTS_PER_IP`只能有一个参数发挥作用



****

# 单元小结

## 实现Scrapy爬虫的过程：

+ 建立工程和Spider模板
+ 编写Spider（最重要）
+ 编写Pipeline，处理提取到的信息的后续功能，比如写入文件等
+ 配置优化