import requests

headers = {"user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
           }

url = "https://www.baidu.com/s?"

params = {
    "ie":"utf-8",
    "wd":input("请输入名字：")
}

res = requests.get(url=url, params=params, headers=headers).content.decode("utf-8")
print(res)