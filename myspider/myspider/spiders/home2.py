import scrapy
from myspider.items import AjkpiderItem
import pandas as pd
class Home2Spider(scrapy.Spider):
    name = "home2"
    start_urls = ["https://ty.fang.anjuke.com/loupan/all"]

    def parse(self, response):
        data_list = response.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div')

        for data in data_list:
            item = AjkpiderItem()
            item['title'] = data.xpath('./div/a[1]/span/text()').extract_first(default='无标题')
            item['price'] = data.xpath('./a[2]/p/span/text()').extract_first(default='无价格')
            item['address'] = data.xpath('./div/a[2]/span/text()').extract_first(default='无地址').replace('\xa0', ' ')
            item['status'] = data.xpath('./div/a[4]/div/i[1]/text()').extract_first(default='无状态')
            item['size'] = data.xpath('./div/a[3]/span[@class="building-area"]/text()').extract_first(default='无面积')
            item['huxing'] = data.xpath('./div/a[3]/span[1]/text()').extract_first(default='无户型')
            # print(item)
            yield item


        # 翻页
        next_page = response.xpath('//*[@id="container"]/div[2]/div[1]/div[4]/div/a[8]/@href').extract_first()  # 这里更新为你的翻页XPath
        print(next_page)
        if next_page:  # 确保找到下一页链接
            next_page = response.urljoin(next_page)  # 处理相对链接
            yield scrapy.Request(url=next_page, callback=self.parse)  # 发起新的请求

        # 将数据保存到 Excel 文件
        # df = pd.DataFrame(items)
        # df.to_excel('home2-6.xlsx', index=False)