#!/usr/bin/env python
# coding=utf-8
from gevent import monkey
monkey.patch_all()  # 确保在所有模块加载之前执行
import time
import os
import csv
import logging
from pprint import pprint
from collections import Counter

import requests
import matplotlib.pyplot as plt
import jieba
import pymysql
from gevent import monkey
from gevent.pool import Pool
from queue import Queue
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import sys

# 增加递归深度限制
sys.setrecursionlimit(3000)

# Make the standard library cooperative.
monkey.patch_all()

def get_logger():
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    logger = logging.getLogger("monitor")
    logger.setLevel(LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

START_URL = (
    "http://search.51job.com/list/010000%252C020000%252C030200%252C040000"
    ",000000,0000,00,9,99,Python,2,{}.html? lang=c&stype=1&postchannel=00"
    "00&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lon"
    "lat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&"
    "address=&line=&specialarea=00&from=&welfare="
)


LOG_LEVEL = logging.INFO
POOL_MAXSIZE = 4  # 控制线程池容量

logger = get_logger()

class JobSpider:
    def __init__(self):
        self.count = 1
        self.company = []
        self.desc_url_queue = Queue()
        self.pool = Pool(POOL_MAXSIZE)

    def job_spider(self):
        urls = [START_URL.format(p) for p in range(1, 16)]
        for url in urls:
            logger.info("爬取第 {} 页".format(urls.index(url) + 1))
            html = requests.get(url, headers=HEADERS).content.decode("gbk")
            bs = BeautifulSoup(html, "lxml").find("div", class_="dw_table").find_all(
                "div", class_="el"
            )
            for b in bs:
                try:
                    href, post = b.find("a")["href"], b.find("a")["title"]
                    locate = b.find("span", class_="t3").text
                    salary = b.find("span", class_="t4").text
                    item = {
                        "href": href, "post": post, "locate": locate, "salary": salary
                    }
                    self.desc_url_queue.put(href)
                    self.company.append(item)
                except Exception:
                    pass
        logger.info("队列长度为 {} ".format(self.desc_url_queue.qsize()))

    def post_require(self):
        max_retries = 3
        retries = 0
        while not self.desc_url_queue.empty():
            url = self.desc_url_queue.get()
            resp = requests.get(url, headers=HEADERS)
            if resp.status_code == 200:
                logger.info("爬取第 {} 条岗位详情".format(self.count))
                html = resp.content.decode("gbk")
                self.desc_url_queue.task_done()
                self.count += 1
            else:
                retries += 1
                if retries < max_retries:
                    time.sleep(0.5)
                    self.desc_url_queue.put(url)
                continue

            try:
                bs = BeautifulSoup(html, "lxml").find(
                    "div", class_="bmsg job_msg inbox"
                ).text
                s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
                    "\t", ""
                ).strip()
                with open(
                    os.path.join("data", "post_require_new.txt"), "a", encoding="utf-8"
                ) as f:
                    f.write(s)
            except Exception as e:
                logger.error(e)
                logger.warning(url)

    def execute_tasks_in_batches(self):
        while not self.desc_url_queue.empty():
            for _ in range(min(POOL_MAXSIZE, self.desc_url_queue.qsize())):
                self.pool.apply_async(self.post_require)

    def run(self):
        self.job_spider()
        self.execute_tasks_in_batches()
        self.desc_url_queue.join()  # 主线程阻塞,等待队列清空

if __name__ == "__main__":
    spider = JobSpider()
    start = time.time()
    spider.run()
    logger.info("总耗时 {} 秒".format(time.time() - start))
