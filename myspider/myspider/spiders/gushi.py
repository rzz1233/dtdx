import scrapy
from ..items import GushipiderItem

class GushiSpider(scrapy.Spider):
    name = "gushi"
    # allowed_domains = ["shici.tqzw.net.cn"]
    start_urls = ["https://shici.tqzw.net.cn/gushi/songcisanbaishou/index.html"]

    def parse(self, response):
        data_list = response.xpath('//div[@class="gs-sons"]')
        for i in data_list:
            item = GushipiderItem()
            item['title'] = i.xpath('./div/div[1]/h3/a/text()').extract_first()
            item['content'] = i.xpath('./div/div[3]/div[@class="gs-conview-def"]/p/text()').extract()
            item['content'] = ' '.join(item['content'])
        #深层地址
            deep_url = response.urljoin(i.xpath("./div/div[1]/h3/a/@href").extract_first())
            print("deep_url", deep_url)
            yield scrapy.Request(
                url=deep_url,
                callback=self.deep_cont,
                meta={"item": item}
            )

        #翻页
        next_page = response.xpath('//div[@class="gs-pages"]//li[last()-1]/a/@href').extract_first()
        next_page = response.urljoin(next_page)
        yield scrapy.Request(url=next_page,
                             callback=self.parse)

    def deep_cont(self, response):
        #将meta传参处理
        item = response.meta["item"]
        #提取剩余字段数据
        item["fanyi"] = response.xpath('//div[@class="gs-works-text showmore"]/p/text()').extract_first()
        #返回引擎
        yield item


