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
