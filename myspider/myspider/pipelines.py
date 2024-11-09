# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
from pymysql import connect
from .settings import database
#信思智学
class MyspiderPipeline:
    def __init__(self):
        self.conn = connect(host=database["IP"], port=database["PORT"], user=database["USER"], password=database["PASSWORD"],database="spider")

    def process_item(self, item, spider):
        if spider.name == 'xs':
            title = item["title"]
            content = item["content"]
            cur = self.conn.cursor()
            sql = f'insert into xs(title, content) values("{title}","{content}")'
            cur.execute(sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        if spider.name == 'xs':
            self.conn.close()

#安居客
class HomePipeline:
    def __init__(self):
        self.file = None
    def open_spider(self,spider):
        if spider.name == 'home':
            self.file = open('home.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'home':
            item = dict(item) #将item强转为字典（只能在scrapy中使用）
            data = json.dumps(item, ensure_ascii=False) + ",\n"
            self.file.write(data)
        return item

    def close_spider(self, spider):
        if spider.name == 'home':
            self.file.close()


class GushiPipeline:
    def __init__(self):
        self.conn = connect(host=database["IP"], port=database["PORT"], user=database["USER"], password=database["PASSWORD"],database="spider")

    def process_item(self, item, spider):
        if spider.name == 'gushi':
            title = item["title"]
            content = item["content"]
            fanyi = item["fanyi"]
            cur = self.conn.cursor()
            sql = f'insert into gushi(title, content,fanyi) values("{title}","{content}","{fanyi}")'
            cur.execute(sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        if spider.name == 'gushi':
            self.conn.close()

#安居客
import pandas as pd
import os
from myspider.items import AjkpiderItem

class AjkPipeline:
    def __init__(self):
        self.items = []  # 用于存储抓取的数据

    def open_spider(self, spider):
        if spider.name == 'home2':
            self.file_path = 'taiyuan.xlsx'

    def process_item(self, item, spider):
        if spider.name == 'home2':
            self.items.append(dict(item))  # 将抓取的 item 添加到列表中
        return item

    def close_spider(self, spider):
        if spider.name == 'home2':
            # 如果文件存在，则读取现有数据
            if os.path.exists(self.file_path):
                existing_data = pd.read_excel(self.file_path).to_dict(orient='records')
                self.items.extend(existing_data)  # 合并新旧数据

            # 保存所有数据到 Excel 文件
            df = pd.DataFrame(self.items)
            df.to_excel(self.file_path, index=False)
            self.log(f"数据已保存到 {self.file_path}")

    def log(self, message):
        print(message)  # 您可以根据需要修改日志输出方式


class CaiPipeline:
    def __init__(self):
        self.items = []  # 用于存储抓取的数据

    def open_spider(self, spider):
        if spider.name == 'cai':
            self.file_path = 'chuancai.xlsx'

    def process_item(self, item, spider):
        if spider.name == 'cai':
            self.items.append(dict(item))  # 将抓取的 item 添加到列表中
        return item

    def close_spider(self, spider):
        if spider.name == 'cai':
            # 如果文件存在，则读取现有数据
            if os.path.exists(self.file_path):
                existing_data = pd.read_excel(self.file_path).to_dict(orient='records')
                self.items.extend(existing_data)  # 合并新旧数据

            # 保存所有数据到 Excel 文件
            df = pd.DataFrame(self.items)
            df.to_excel(self.file_path, index=False)
            self.log(f"数据已保存到 {self.file_path}")

    def log(self, message):
        print(message)  # 您可以根据需要修改日志输出方式

