# Scrapy爬虫的常用命令

## Scrapy命令行

Scrapy是为持续运行设计的专业爬虫框架，提供操作的Scrapy命令行

在cmd中用`scrapy -h`可以看到Scrapy命令行

Scrapy库的很多的操作包括建立爬虫和运行爬虫都是通过命令行来实现的。



Scrapy命令行的格式：

```scrapy
>scrapy<command>[options][args]
```

6个常用命令：

| 命令         | 说明               | 格式                                        |
| ------------ | ------------------ | ------------------------------------------- |
| startproject | 创建一个新工程     | `scrapy startproect <name>[dir]`            |
| genspider    | 创建一个爬虫       | `scrapy genspider [options] <name><domain>` |
| settings     | 获得爬虫配置信息   | `scrapy settings [opetions]`                |
| crawl        | 运行一个爬虫       | `scrapy crawl <spider>`                     |
| list         | 列出工程中所有爬虫 | `scrapy list`                               |
| shell        | 启动URL调试命令行  | `scrapy shell [url]`                        |

在Scrapy框架下，一个工程是一个最大的单元，工程并不是爬虫，一个工程可以相当于一个大的Scrapy框架，在Scrapy框架中，可以有多个爬虫，每一个爬虫相当于框架中的一个`spiders`模块。

在6个命令中，最常用的是其中的3个命令：

1. startproject
2. genspider
3. crawl



****

Scrapy爬虫并不是给用户操作来使用的，它更多的是一个后台的爬虫框架，所以使用命令行可以方便地让程序员编写自动化的脚本，对爬虫的控制和访问以及对数据的操作会变得更加灵活。

对于程序来讲，它更关心的是一个一个的指令，所以通过命令行，指令就可以被程序接收。所以没有图形界面给用户使用。

本质上，Scrapy是给程序员用的，功能（而不是界面）更重要

