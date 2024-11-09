import scrapy
from myspider.items import MyspiderItem

class XsSpider(scrapy.Spider):
    name = "xs"
    allowed_domains = ["www.chinazxjy.cn"]
    start_urls = ["http://www.chinazxjy.cn/jyzs.htm"]

    def parse(self, response):
        # with open('demo1.html', 'wb') as f:
        #     f.write(response.body)
        item = MyspiderItem()
        data_list = response.xpath('//*[@id="body"]/div[6]/div/div[2]/div[2]/ul/li')
        for i in data_list:
            item['title'] = i.xpath('./a/h2/text()').extract_first()
            item['content'] = i.xpath('./a/p/text()').extract_first().strip()
            print(item,type(item))
            yield item

