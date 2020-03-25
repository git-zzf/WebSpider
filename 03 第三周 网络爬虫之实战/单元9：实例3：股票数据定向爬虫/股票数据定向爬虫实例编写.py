import unicodedata
import requests
import re
import traceback
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('爬取失败')
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


"""视频的例子使用百度股票，已经无法查看网页
def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets=name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()
            print('存储失败')
            continue"""


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock
        # print(url)
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('table', attrs={'class': 'quote'})
            if isinstance(stockInfo, bs4.element.Tag):
                name = stockInfo.find('a', attrs={'target': '_blank'}).parent
            else:
                continue
            name_text = name.text.split()[0]
            infoDict.update({'股票名称': name_text})
            if isinstance(stockInfo, bs4.element.Tag):
                keyList = stockInfo.find_all('tr')
            else:
                continue
            del keyList[0]

            for i in range(len(keyList)):
                data = keyList[i].find_all('td')
                key1 = unicodedata.normalize('NFKC', data[0].text.split(':')[0])
                val1 = data[0].text.split(':')[1]
                key2 = unicodedata.normalize('NFKC', data[1].text.split(':')[0])
                val2 = data[1].text.split(':')[1]
                infoDict[key1] = val1
                infoDict[key2] = val2
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度: {:.2f}%'.format(count*100/len(lst)), end='')
        except:
            count = count + 1
            print('\r当前速度: {:.2f}%'.format(count*100/len(lst)), end='')
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'http://so.cfi.cn/so.aspx?txquery='
    output_file = 'E://Notes/WebSpider/03 第三周 网络爬虫之实战/单元9：实例3：股票数据定向爬虫/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


if __name__ == "__main__":
    main()
