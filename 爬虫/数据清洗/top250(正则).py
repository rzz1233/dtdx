import re
import requests

url = "https://movie.douban.com/top250"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
}

response = requests.get(url=url,headers=headers).content.decode("utf-8")

# 使用正则表达式创建模式，匹配电影名称、导演和年份
obj = re.compile(r'<div class="item">.*? <span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?导演: (?P<dao>.*?)&nbsp;.*?<br>.*?(?P<year>.*?)&nbsp;',re.S)

# 通过正则表达式查找匹配结果
result = obj.finditer(response)

list = []
for data in result:
    dic = {}
    dic['name'] = data.group("name")
    dic['dao'] = data.group("dao")
    dic['year'] = data.group("year").strip()
    list.append(dic)
print(list)
print(len(list))





