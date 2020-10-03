import requests
import json

url = "https://www.thsrc.com.tw/TimeTable/Search"

headers = {
"User-Agent":"Googlebot"
}

basicdata = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": "BanQiao",
    "EndStation": "XinZhu",
    "OutWardSearchDate": "2020/10/04",
    "OutWardSearchTime": "15:00",
    "ReturnSearchDate": "2020/10/05",
    "ReturnSearchTime": "15:00"
}

res = requests.post(url, headers = headers, data = basicdata)
content = json.loads(res.text)
# print(type(content)) # <class 'dict'>
# print(content) # True

prettycontent = json.dumps(content, indent=4) # indent 表示空格數量
print(prettycontent)
# x = content["data"]["DepartureTable"]["Title"]["StartStationName"]
# print(x)

f = open("data.json","w+",encoding="utf-8")
f.write(prettycontent)
f.close()
