import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url): #获取网页内容，使用requests库
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    

def fillUnivList(ulist, html): # 提取网页信息，保存到列表中，使用BeautifulSoup库
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:  # 在tbody的儿子标签中搜索tr标签
        if isinstance(tr, bs4.element.Tag): # 由于tr可能出现在字符串里，我们只需要搜索标签中的tr
                tds = tr('td')  # 查找td标签，等价于tr.find_all('td')，返回列表类型tds
                ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num): # 打印信息
    print("{:^10}\t{:^12}\t{:^9}\t".format("排名", "学校名称", "分数")) # {:^10}\t的意思是设定一个槽，宽10，居中显示，后面跟一个tab
    for i in range(num):
            u = ulist[i]
            print("{:^10}\t{:^12}\t{:^9}\t".format(u[0], u[1], u[2]))
        
        
def main():
    url = "http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
