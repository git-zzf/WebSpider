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