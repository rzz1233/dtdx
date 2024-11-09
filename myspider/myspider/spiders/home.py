import scrapy
from myspider.items import HomespiderItem

class HomeSpider(scrapy.Spider):
    name = "home"
    allowed_domains = ["bj.zu.anjuke.com"]
    start_urls = ["https://bj.zu.anjuke.com/?from=HomePage_TopBar"]

    def parse(self, response):
        # with open('demo1.html', 'wb') as f:
        #     f.write(response.body)
        item = HomespiderItem()
        data_list = response.xpath('//*[@id="list-content"]/div')
        for data in data_list:
            item['title'] = data.xpath('./div[1]/h3/a/b/text()').extract_first()
            item['address'] = data.xpath('./div[1]/address/a/text()').extract_first()
            item['price'] = data.xpath('./div[2]/strong/text()').extract_first()
            print(item)
            yield item



