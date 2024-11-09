# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#爬虫获取到的数据要组装成Item对象(可以当成一个字典如：title和content是键)
class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

#安居客
class HomespiderItem(scrapy.Item):
    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()


class GushipiderItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    fanyi = scrapy.Field()

class AjkpiderItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    # huxing = scrapy.Field()
    size = scrapy.Field()
    address = scrapy.Field()
    status = scrapy.Field()


class CaipiderItem(scrapy.Item):
    name = scrapy.Field()
    sort = scrapy.Field()
    shicai = scrapy.Field()
    zuofa = scrapy.Field()



