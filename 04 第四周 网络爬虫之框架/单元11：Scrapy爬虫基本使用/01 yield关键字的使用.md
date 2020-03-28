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

