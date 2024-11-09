from lxml import etree
import requests

url = "https://m.shicimingju.com/book/sanguoyanyi.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
}

response = requests.get(url=url, headers=headers).content.decode("utf-8")
html = etree.HTML(response)  #将字符串转化为Element对象

elements = html.xpath('//*[@id="main"]/div/div[3]/ul/li/a/text()')
print(elements)
for i in elements:
    # print(i)
    dic = {}
    list = i.split("·")
    dic[list[0]] = list[1]
    print(dic)



# //*[@id="main"]/div/div[3]/ul/li[2]/a