import requests
import urllib3
import threading
from requests.exceptions import HTTPError

urllib3.disable_warnings()  # 忽略https证书告警
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
results = []
ts = []


def check_if_live(url: str, timeout: float) -> bool:
    try:
        res = requests.get(url, headers=headers, verify=False, timeout=timeout)
        if res.status_code == 200:
            results.append(url)
    except:
        return False
    return True


def __handler(line: str):
    check_if_live(line, 0.7)


with open("urls.txt", "r") as f:
    for line in f:
        line = line[:-1]
        t = threading.Thread(target=__handler, args=(line,))
        t.start()
        ts.append(t)

for t in ts:
    t.join()

with open("urls.txt", "w") as f:
    for i in results:
        f.write(i + "\n")
