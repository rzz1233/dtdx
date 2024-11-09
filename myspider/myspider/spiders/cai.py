import scrapy
from myspider.items import CaipiderItem


class CaiSpider(scrapy.Spider):
    name = "cai"
    start_urls = ["https://www.douguo.com/caipu/%E5%B7%9D%E8%8F%9C"]
    url = 'https://www.douguo.com'

    def parse(self, response):
        data_list = response.xpath("//div[@class='cook-info']")
        for data in data_list:
            item = CaipiderItem()
            item['name'] = data.xpath('./a/text()').get(default='N/A')  #取第一个匹配的内容，并在没有找到任何匹配时返回一个默认值
            item['sort'] = "川菜"  # 可以考虑动态提取
            item['shicai'] = data.xpath('./p/text()').get(default='N/A').strip()

            # 深层地址
            relative_url = data.xpath("./a/@href").get(default='N/A')
            # deep_url = response.urljoin(relative_url)
            deep_url = self.url + relative_url if relative_url else None

            if deep_url:
                print("deep_url:", deep_url)
                yield scrapy.Request(
                    url=deep_url,
                    callback=self.deep_cont,
                    meta={"item": item}
                )

        # 翻页
        next_page = response.xpath("//a[@class='anext']/@href").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def deep_cont(self, response):
        # 将meta传参处理
        item = response.meta["item"]
        # 提取剩余字段数据
        # 提取步骤信息
        steps_raw = response.xpath("//div[@class='stepinfo']/text()").getall()  #提取所有匹配的内容并返回一个列表
        # 清理和拼接步骤信息
        steps = [step.strip() for step in steps_raw if step.strip()]  # 去除空白的步骤
        item['zuofa'] = steps
        print(item)
        # 返回引擎
        yield item
