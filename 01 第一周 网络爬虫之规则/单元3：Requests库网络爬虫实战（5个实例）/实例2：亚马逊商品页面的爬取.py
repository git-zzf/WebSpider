import requests
url = "https://www.amazon.cn/dp/B01FLG4O04"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[2000:3000])
except:
    print("爬取失败")
