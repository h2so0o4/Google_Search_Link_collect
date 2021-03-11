import re
import urllib
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings() #忽略https证书告警

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

# query为搜索内容
query = "影视inurl:php?id=3 and site:.com"
# num为一次搜索的数量
num = 50
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}&num={num}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers, verify=False)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")

    results = []

    # url在<div>标签下的<a>标签下的href值里
    for g in soup.find_all('div'):  # <div>
        anchors = g.find_all('a')  # <a href="">
        if anchors:
            for i in range(len(anchors)):
                try:
                    link = anchors[i].attrs['href']  # 提取字典内容

                    # 正则过滤URL，删除掉一些乱码
                    if re.match('/', link) == None and re.match('(.*)google.com', link) == None and link != '#':

                        # 过滤掉重复的URL
                        for i in results:
                            if i.split(".com")[0] == link.split(".com")[0] :
                                link = ""
                        results.append(link)
                except:
                    pass
            # print(anchors[0].attrs['href'])

    print(results)

    # 写入文件
    with open("urls.txt", "w") as f:
        for i in results:
            f.write(i + "\n")


