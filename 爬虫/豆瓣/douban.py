import requests

class Douban(object):
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.url = f'https://movie.douban.com/typerank?type_name={self.name}&type={self.type}&interval_id=100:90&action='
        self.headers = {"user-agent":
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
                        }
    def save(self,res,name):
        with open(f'douban_{name}.html', 'w', encoding='utf-8') as f:
            f.write(res)
    def request(self,):
        res = requests.get(url=self.url, headers=self.headers).content.decode('utf-8')
        return res
    def run(self):
        res = self.request()
        self.save(res,self.name)

if __name__ == '__main__':
    name = input("请输入类型名：")
    type = input("请输入类型号：")
    douban = Douban(name,type)
    douban.run()
