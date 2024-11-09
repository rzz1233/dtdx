import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": input("请输入要查询的单词：")
}

resp = requests.post(url=url,headers=headers,data=data).json()

data = resp["data"][0]["v"]
print(data)


