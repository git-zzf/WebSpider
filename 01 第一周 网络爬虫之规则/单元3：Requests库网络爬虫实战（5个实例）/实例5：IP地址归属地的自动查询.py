import requests
url = "http://ip138.com/iplookup.asp?ip="
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url + '55.55.55.55'+'&action=2',headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[7000:7500])
except:
    print("爬取失败")
