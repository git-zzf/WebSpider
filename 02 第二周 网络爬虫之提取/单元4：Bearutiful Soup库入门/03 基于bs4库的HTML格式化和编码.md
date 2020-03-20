# 基于bs4库的HTML格式化和编码

如何能让HTML页面更加友好地显示？

## bs4库的prettify()方法

```python
>>> import requests
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> demo = r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'
```

首先获取demo

然后使用prettify来打印

```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.prettify()
'<html>\n <head>\n  <title>\n   This is a python demo page\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The demo python introduces several python courses.\n   </b>\n  </p>\n  <p class="course">\n   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\n   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">\n    Basic Python\n   </a>\n   and\n   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">\n    Advanced Python\n   </a>\n   .\n  </p>\n </body>\n</html>'
```

打印的结果中每个标签的后面都加了一个换行符\n，使用print函数把相关信息打印出来。

```python
>>> print(soup.prettify())
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```

我们发现现在soup的变量变得非常清晰。每一个标签以及相关内容都分行显示。

Prettify这个方法可以为HTML文本的标签以及内容增加换行符，它也可以对每一个标签来做相关的处理。例如，对a标签进行prettify的处理：

```python
>>> print(soup.a.prettify())
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
 Basic Python
</a>
```



## 编码

在bs4库中，将任何读入的HTML文件或字符串都转换成'utf-8'编码，'utf-8'编码可以很好地支持中文。由于Python3.x系列默认编码是'utf-8'因此，在做相关解析的时候，使用bs4库没有障碍。

```python
>>> soup = BeautifulSoup("<p>中文</p>", "html.parser")
>>> soup.p.string
'中文'
>>> print(soup.p.prettify())
<p>
 中文
</p>
```

