# Robots协议

Robots Exclusion Standard 网络爬虫排除标准

+ **作用**：网站告知网络爬虫哪些页面可以抓取，哪些不行

+ **形式**：在网站根目录下的robots.txt文件

## 案例：京东的Robots协议

```robots.txt
https://www.jd.com/robots.txt
User-agent: * 对于所有的网络爬虫都要遵守
Disallow: /?* 任何爬虫都不允许访问以问号开头的路径
Disallow: /pop/*.html 任何爬虫都不允许访问pop/*.html
Disallow: /pinpai/*.html?* 任何爬虫都不允许访问符合这个通配符的网页
User-agent: EtaoSpider 以下4个网络爬虫不允许爬取京东的任何资源
Disallow: / 根目录
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```

## Robots协议基本语法

``` 
#注释，*代表所有，/代表根目录
User-agent: *
Disallow: /
```

User-agent 表明哪些爬虫，针对所有爬虫，使用*

Disallow 不允许爬虫访问的资源的目录

# 其他案例

```robots.txt
http://www.baidu.com/robots.txt
User-agent: Baiduspider
Disallow: /baidu
Disallow: /s?
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Googlebot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: MSNBot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Baiduspider-image
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: YoudaoBot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou web spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou inst spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou spider2
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou blog
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou News Spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou Orion spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: ChinasoSpider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sosospider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh


User-agent: yisouspider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: EasouSpider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: *
Disallow: /
```

```robots.txt
http://news.sina.com.cn/robots.txt
User-agent: *
Disallow: /wap/
Disallow: /iframe/
Disallow: /temp/
```

```robots.txt
http://www.qq.com/robots.txt
User-agent: *
Disallow:  
Sitemap: http://www.qq.com/sitemap_index.xml
```

```robots.txt
http://news.qq.com/robots.txt
User-agent: *
Disallow:  
Sitemap: http://www.qq.com/sitemap_index.xml
Sitemap: http://news.qq.com/topic_sitemap.xml
```

```robots.txt
http://www.moe.edu.cn/robots.txt (无robots协议)
```

```robots.txt
https://www.nike.com/robots.tx (结尾有意思)
```

robots协议规定，如果一个网站不提供robots.txt文件，那就说明这个网站允许所有爬虫不限制地爬取其内容