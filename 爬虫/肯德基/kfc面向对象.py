import requests
import json

class KFC(object):
    def __init__(self):
        self.headers = {
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
                 }
        self.url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
        self.data = {
                "cname": input("请输入城市："),
                "pageIndex": 1
            }
    def save(self,str_dic):
        with open(f"kfc{self.data['cname']}.txt", "a", encoding="utf-8") as f:
            f.write(str_dic + "\n")
    def get_data(self):
        while True:
            try:
                resp = requests.post(url=self.url, headers=self.headers, data=self.data).json()  # 把转换为python的数据类型
                res_list = resp['Table1']
                if not res_list:
                    print("爬取完成")
                    break
                else:
                    for res in res_list:
                        print(res)
                        str_dic = json.dumps(res, ensure_ascii=False)
                        self.save(str_dic)

                    print(f"第{self.data['pageIndex']}页已经爬取完成")
                self.data['pageIndex'] += 1
            except Exception as e:
                print("发生错误")
                break

if __name__ == '__main__':
    kfc = KFC()
    kfc.get_data()

