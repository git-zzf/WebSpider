# Beautiful Soup库的安装

## 介绍

可以对HTML，XML格式进行解析，并且提取其中的相关信息

`https://www.crummy.com/software/BeautifulSoup/`

官网对它的描述：

+ Beautiful Soup parses anything you give it, and does the tree traversal stuff for you. 

+ Beautiful Soup可以对你提供给它的任何格式进行相关的爬取，并且进行树形解析

工作原理是把任何文档当作一锅汤，煲制这锅汤。

## 安装

管理员权限打开cmd

```cmd
>>> pip install beautifulsoup4
```

## 测试：获取网页源代码

演示HTML页面地址：

`http://python123.io/ws/demo.html`

### 手动获取源代码

右键：查看网页源代码

### 用Requests库查看源代码

```python
>>> import requests
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> r.text      
>>> demo = r.text
```

测试Beautiful Soup库

首先导入Beautiful Soup库

```python
>>> from bs4 import BeautifulSoup
```

从bs4库导入BeautifulSoup类

做汤，把html页面熬成一个Beautiful Soup能够理解的汤

```python
>>> soup = BeautifulSoup(demo, "html.parser")
```

除了给出demo变量，还需要给出一个解析demo的解释器，这里用的解释器是html.parser，即对demo进行html的解析

打印结果测试解析是否正确

```python
>>> print(soup.prettify())
```

## 如何使用BeautifulSoup库

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>', 'html.parser')
```

BeautifulSoup有两个参数，第一个是需要BeautifulSoup解析的一个html格式的信息，另一个是解析汤使用的解析器