# 用POST來爬蟲高鐵的票價吧!
    學習參考: https://www.youtube.com/watch?v=Ef0kh6NPiBE&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=6
    台灣高鐵: https://www.thsrc.com.tw/

## 先查看台灣超鐵的網站，右鍵檢查查看XHR的Search
    透過Network可以查看到有一隻search的程式，專門用來傳遞參數並回傳的結果的程式
    我們可以看到查詢的主要程式連結及傳遞的form data資料

## 高鐵基本票價爬蟲
    import requests
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

    prettycontent = json.dumps(content, indent=4) # indent 表示空格數量
    print(prettycontent)

## 將資料儲存到data.json裡面，使用json套件的loads及dumps的轉換
    json.loads能將資料轉換成<dict>
    json.dumps能將資料轉換成<str>
    
    f = open("data.json","w+",encoding="utf-8")
    f.write(prettycontent)
    f.close()
