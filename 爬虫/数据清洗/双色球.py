from lxml import etree
import requests
import time
from selenium import webdriver

# url = "https://datachart.500.com/ssq/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
# }
#
# response = requests.get(url=url, headers=headers)
# response.encoding = response.apparent_encoding  # 自动检测并设置正确的编码
web = webdriver.Chrome(executable_path="./chromedriver.exe")
web.get('https://datachart.500.com/ssq/')
time.sleep(5)
# 获取页面源代码
res = web.page_source

# 解析 HTML
html = etree.HTML(res)  # 将字符串转化为Element对象

# elements = html.xpath('//*[@id="tdata"]/tr/td[@class="chartBall01"]')
elements = html.xpath('//*[@id="tdata"]/tr')
for i in elements:
    dic = {}
    dic['red'] = i.xpath('./td[@class="chartBall01"]/text()')
    dic['brown'] = i.xpath('./td[@class="chartBall01 chartBall07"]/text()')
    dic['bule'] = i.xpath('./td[@class="chartBall02"]/text()')
    if dic['brown'] and dic['bule']and dic['red']:
        print(dic)

time.sleep(10)
web.quit()
