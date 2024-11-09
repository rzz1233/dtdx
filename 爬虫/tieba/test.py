import requests
class Tieba(object):
    def __init__(self,keyword,page):
        self.keyword=keyword
        self.page=page
        self.url = f"https://tieba.baidu.com/f?kw={keyword}&ie=utf-8"
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
                }
        self.url_list = []
    #得到url列表
    def get_url_list(self):
        for i in range(1, self.page+1):
            self.url_list.append(self.url + f"&pn={(i - 1) * 50}")
    #文件上传
    def save(self,res,i):
        with open(f"{self.keyword}_{i + 1}页.html", "w", encoding="utf-8") as f:
            f.write(res)
    def run(self):
        self.get_url_list()
        for i in range(len(self.url_list)):
            res = requests.get(url=self.url_list[i], headers=self.headers).content.decode("utf-8")
            self.save(res, i)

if __name__ == '__main__':

    tieba = Tieba("李毅",5)
    tieba.run()