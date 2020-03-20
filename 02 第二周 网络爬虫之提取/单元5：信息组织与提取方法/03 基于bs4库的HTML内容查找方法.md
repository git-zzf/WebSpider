# 基于bs4库的HTML内容查找方法

回顾demo.html

```python
>>> import requests
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> r.text      
>>> demo = r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'
```

BeautifulSoup库提供了一个方法:

`<>.find_all(name, attrs, recursive, string, **kwargs)`

这个方法可以在soup的变量中查找相关信息，有5个参数。可以返回一个列表类型，储存查找的结果



## find_all()函数的5个参数

### name：对标签名称的检索字符串

例子：

**查找所有a标签：**

```python
>>> soup.find_all('a')
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
```

输出了一个列表类型，列表中包含了在这个文件中出现的所有a标签



**查找a标签和b标签，注意这里a和b要用方括号，以列表形式给到函数：**

```python
>>> soup.find_all(['a','b'])
[<b>The demo python introduces several python courses.</b>, <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
```



**如果给到的参数是True则显示当前soup的所有标签信息：**

```python
>>> for tag in soup.find_all(True):
    print(tag.name)
    
html
head
title
body
p
b
p
a
a
```

这里打印了所有的标签



**查找所有以b开头的标签，包括b和body标签，这样就需要使用一个第三方库，正则表达式库：**

```python
>>> import re
>>> for tag in soup.find_all(re.compile('b')):
    	print(tag.name)
        	
body
b
```

`re.compile('b')` 返回的是以b开头的所有的信息，作为查找的要素

结果打印了以b开头的b和body标签



### attrs：对标签属性值的检索字符串，可标注属性检索

例子：

**查找p标签中包含course字符串的信息：**

```python
>>> soup.find_all('p', 'course')
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]
```

返回了一个列表类型，给出了带有course属性值的p标签



**我们也可以直接对属性做相关的约定，查找所有id属性等于link1作为查找元素：**

```python
>>> soup.find_all(id = 'link1')
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
```



**查找id属性为link的元素：**

```python
>>> soup.find_all(id = 'link')
[]
```

返回结果为空，表示在demo的HTML文件中，并不包含id值为link的属性标签，意味着在对属性赋值进行查找的时候，必须精确地赋值这个信息，如果我们想查找属性的部分信息，比如查找link以及link1，link2的内容，那么就仍然需要用到正则表达式的支持。

```python
>>> import re
>>> soup.find_all(id = re.compile('link'))
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
```

这样就看到了结果，结果中包含以link开头，但不完全是link的标签信息。

正则表达式和搜索关键词一样，是搜索词的一部分，如果不使用正则表达式，那就需要完整准确地给出我们要搜索的信息，而使用正则表达式后，只需要给出一部分信息就可以了。



### recursive：是否对子孙全部检索，默认True

例子：

```python
>>> soup.find_all('a')
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
>>> soup.find_all('a', recuresive = False)
[]
```

当查找a标签的时候，找到了信息，然而把recursive定为False后返回了空列表，说明从soup根节点开始，它的儿子节点层面上没有a标签，a标签出现在之后的子孙节点上。



### string：<>...</>中字符串区域的检索字符串

对标签中间的字符串进行检索的参数

例子：

```python
>>> soup
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
>>> soup.find_all(string = "Basic Python")
['Basic Python']
```

在soup里检索Basic Python字符串，必须精确地输入字符串内容才能检索到。使用正则表达式可以使用部分关键词检索。

```python
>>> import re
>>> soup.find_all(string = re.compile("python"))
['This is a python demo page', 'The demo python introduces several python courses.']
```



### find_all()函数的简写形式

由于find_all()方法特别常用，所以有两种等价形式

对于标签可以使用`<tag>(...)`等价于`<tag>.find_all(..)`

对于`soup(..)`等价于`soup.find_all(..)`



### find_all()函数的7个拓展方法

| 方法                        | 说明                                                    |
| --------------------------- | ------------------------------------------------------- |
| <>.find()                   | 搜索且只返回一个结果，字符串类型，同.find_all()参数     |
| <>.find_parents()           | 在先辈节点中搜索，返回列表类型，同.find_all()参数       |
| <>.find_parent()            | 在先辈节点中返回一个结果，字符串类型，同.find()参数     |
| <>.find_next_siblings()     | 在后续平行节点中搜索，返回列表类型，同.find_all()参数   |
| <>.find_next_sibling()      | 在后续平行节点中返回一个结果，字符串类型，同.find()参数 |
| <>.find_previous_siblings() | 在前序平行节点中搜索，返回列表类型，同.find_all()参数   |
| <>.find_previous_sibling()  | 在前序平行节点中返回一个结果，字符串类型，同.find()参数 |

