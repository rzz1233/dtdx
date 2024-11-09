from lxml import etree
import requests

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
}

response = requests.get(url=url, headers=headers).content.decode("utf-8")
html = etree.HTML(response)  #将字符串转化为Element对象
# #电影名称
# data = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
# #导演主演
# data1 = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]')
# # 清理导演和主演信息，去除多余的空格和不间断空格符号 \xa0
# directors_cleaned = [item.replace("\xa0", "").replace("\n", "").strip() for item in data1]
#
# list = list(zip(data, directors_cleaned))
#
# for name,dao in list:
#     dic = {}
#     dic["name"] = name
#     dic["directors"] = dao
#     print(dic)


elemt = html.xpath('//*[@id="content"]/div/div[1]/ol//li/div/div[2]')

for i in elemt:
    dic = {}
    # 提取电影名称，确保列表非空后再取值
    name_list = i.xpath("./div[1]/a/span[1]/text()")
    if name_list:
        dic["name"] = name_list[0]
    # 提取导演和主演信息，并进行清理
    dao_list = i.xpath("./div[2]/p[1]/text()[1]")
    if dao_list:
        # 这里确保从列表中取出字符串进行处理
        dic["dao"] = dao_list[0].strip().replace("\xa0", "").replace("\n", "").strip()
    print(dic)




# xpath 必须这样写，谁今后取到底，就给他发这个截图!!!
# elemt = html.xpath('//li[@class="item-1"]') #3条
# for i in elemt:
#     dic = {}
#     dic["title"] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()"))>0 else None
#     dic["href"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href"))>0 else None
#     print(dic)