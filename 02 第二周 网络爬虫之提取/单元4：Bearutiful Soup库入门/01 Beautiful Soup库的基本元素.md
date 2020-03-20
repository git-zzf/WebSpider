# Beautiful Soup库的基本元素

## BeautifulSoup类

### HTML文件

```html
<html>
    <body>
        <p class = "title">
            ...
        </p>
    </body>
</html>
```

HTML文件的源代码是由一组尖括号构成的标签组织起来的，每一对尖括号形成了一个标签，标签之间存在上下级关系，形成了标签树。

Beautiful Soup库是解析、遍历、维护“标签树”的功能库。只要提供的文件是标签类型，Beautiful Soup库都可以对它做很好的解析。

看下每个标签的具体格式。

以p标签为例

```html
<p class = "title">
    ...
</p>
```

一对尖括号和一对尖括号中间有斜线形成了一个标签对，Tag。

其中第一个尖括号中的第一个单词p就是这个标签的名称，Name。一般标签的名称是成对出现的，在最开始和最后都出现标明这个标签的范围。

在第一对尖括号中，除了名字之外，存在了一个相关的域，这个域叫属性域，Attributes。这里面包含0个或多个属性，属性用来定义标签的特点。这里有一个属性叫class，属性的内容是title。任何一个属性有它属性的特性和它的值。所以属性是由键和值，键值对构成的。

这样的格式构成了标签的基本结构。



### Beautiful Soup库的引用

Beautiful Soup库也叫beautifulsoup4库或bs4。

我们在使用它的时候需要采用一些引用方式。

最常用的是

```python
from bs4 import BeautifulSoup
```

这个引用方式说明我们从bs4库中引入了一个类型，这个类型叫BeautifulSoup。

BeautifulSoup中的B和S要大写，因为Python是一个大小写敏感的语言。

如果我们要对Beautiful Soup库中的一些基本变量进行判断的时候，我们也可以直接引用

```python
import bs4
```



### 如何理解BeautifulSoup这个类

Beautiful Soup库本身解析的是HTML和XML文档，文档和标签树是一一对应的，经过了BeautifulSoup类的处理，我们可以使得每一个标签树（字符串），我们将这个标签树转换成一个BeautifulSoup类 ，BeautifulSoup类就是能代替标签树的一个类型。

所以HTML文档，标签树，BeautifulSoup类三者是等价的。

在这个基础上，我们可以通过BeautifulSoup类使得标签树形成了一个变量，而对这个变量的处理就是对标签树的处理。

这里可以使用如下代码：

```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<html>data</html>", "html.parser")
>>> soup2 = BeautifulSoup(open("D://demo.html"), "html.parser")
```

首先import BeautifulSoup类型。

定义一个变量soup，给入一个HTML代码，指定HTML格式的parser来解析。

同时也可以通过打开文件的方式，为BeautifulSoup类提供XML或HTML的文档内容。

简单来说，可以把BeautifulSoup类对应一个HTML/XML文档的全部内容。



### 解析器

| 解析器           | 使用方法                         | 条件                 |
| ---------------- | -------------------------------- | -------------------- |
| bs4的HTML解析器  | BeautifulSoup(mk, 'html.parser') | 安装bs4库            |
| lxml的HTML解析器 | BeautifulSoup(mk, 'lxml')        | pip install lxml     |
| lxml的XML解析器  | BeautifulSoup(mk, 'xml')         | pip install lxml     |
| html5lib的解析器 | BeautifulSoup(mk, 'html5lib')    | pip install html5lib |

事实上无论哪种解析器，都可以有效解析HTML和XML文档。

****

## BeautifulSoup类的基本元素

| 基本元素        | 说明                                                      |
| --------------- | --------------------------------------------------------- |
| Tag             | 标签，最基本的信息组织单元，分别用<>和</>表明开头和结尾   |
| Name            | 标签的名字，<p>...</p>的名字是'p'，格式：<tag>.name来获取 |
| Attributes      | 标签的属性，字典形式组织，格式：<tag>.attrs               |
| NavigableString | 标签内非属性字符串，<>...</>中字符串，格式：<tag>.string  |
| Comment         | 标签内字符串的注释部分，一种特殊的Comment类型             |



### 分析demo.html 

1. #### 获取标签Tag的方法

```python
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> r.text      
>>> demo = r.text
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.title
<title>This is a python demo page</title>                     
>>> tag = soup.a
>>> tag
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
```

title标签就是在浏览器左上方显示信息的地方的内容

a标签是链接标签

用soup.a获得a标签

Tag标签是什么类型：

```python
>>> type(tag)
<class 'bs4.element.Tag'>
```

tag是`<class 'bs4.element.Tag'>`类型



2. #### 获取标签名字Name的方法

```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.a.name
'a'
>>> soup.a.parent.name
'p'
>>> soup.a.parent.parent.name
'body'
```

a标签的名字，a标签父亲的名字（包含a标签的上一层标签）



3. #### 获取tag标签的属性Attributes

```python
>>> tag = soup.a
>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
```

返回的是一个字典，给出了，属性名字和属性的值的对应关系。

我们可以采用字典的方式对每一个属性做信息的提取。

获取class属性的值：

```python
>>> tag.attrs['class']
['py1']
```

返回一个列表类型，第一个元素是['py1']。

获得a标签的链接属性的值：

```python
>>> tag.attrs['href']
'http://www.icourse163.org/course/BIT-268001'
```

标签属性Attributes的类型：

```python
>>> type(tag.attrs)
<class 'dict'>
```

标签属性是字典类型



4. #### NavigableString 类型

尖括号中间的内容

```python
>>> soup.a
>>> soup.a.string
'Basic Python'
>>> soup.p
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>> soup.p.string
'The demo python introduces several python courses.'
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>
```

NavigableString是一个bs4库定义的NavigableString类型

注意，在查看p标签的时候：

```python
>>> soup.p
<p class="title"><b>The demo python introduces several python courses.</b></p>
```

还输出了一个b标签。但是当打印`soup.p.string`的时候，并不包含b标签

这说明：NavigableString是可以跨越多个标签层次的。



5. #### Comment 类型

注释，表示如果HTML页面中有注释的部分，该如何处理

实例：

```python
>>> newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
```

在这个例子中，有一个b标签，里面有一个注释。使用`<!` 表示一个注释的开始。p标签中的信息并不是一个注释。

看下b标签的string：

```python
>>> newsoup.b.string
'This is a comment'
>>> type(newsoup.b.string)
<class 'bs4.element.Comment'>
```

b标签打印出了注释内容，类型是`<class 'bs4.element.Comment'>`，是comment类型。

看下p标签：

```python
>>> newsoup.p.string
'This is not a comment'
>>> type(newsoup.p.string)
<class 'bs4.element.NavigableString'>
```

p标签不是comment类型，是字符串，类型是NavigableString类型 

这里需要注意的是：

**使用b.string和p.string都产生了一段字符串，不过两个字符串没有区别，无法判断哪个是标签，注释的<!标识被去掉了。在分析文档的时候，需要对其中的注释部分做相关的判断，判断的依据就是它的类型。不过这种情况在实际分析文本中并不常用。**

