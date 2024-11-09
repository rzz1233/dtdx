import requests
import json
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
city = "太原"
data = {
    "cname": city,
    "pageIndex": 1
}


while True:
    try:
        resp = requests.post(url=url,headers=headers,data=data).json() #把转换为python的数据类型
        res_list = resp['Table1']
        if not res_list:
            print("爬取完成")
            break
        else:
            for res in res_list:
                print(res)
                str_dic = json.dumps(res,ensure_ascii=False)
                with open("kfc_taiy1.txt", "a", encoding="utf-8") as f:
                    f.write(str_dic + "\n")

            print(f"第{data['pageIndex']}页已经爬取完成")
        data['pageIndex'] += 1
    except Exception as e:
        print("发生错误")
        break




