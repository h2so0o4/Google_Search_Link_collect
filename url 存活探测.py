import requests
import urllib3

urllib3.disable_warnings() #忽略https证书告警
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
results = []
with open("urls.txt","r") as f:
    for line in f:
        line = line[:-1]
        try:
            res = requests.get(line, headers=headers,verify=False,timeout=0.1)
            if res.status_code == 200:
                results.append(line)
        except:
            pass

with open("urls.txt", "w") as f:
    for i in results:
        f.write(i + "\n")


