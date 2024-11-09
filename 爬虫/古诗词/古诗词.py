import requests
from 爬虫.古诗词.古诗词 import chaojiying
import re


session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    # "cookie": "gswZhanghao=516289196%40qq.com; login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1725862025,1726643376; HMACCOUNT=F480386DC69D99E4; ticketStr=200382928%7cgQF48DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyOXczQlJvbGVkN2kxM1c5aWhEMUIAAgT6fOpmAwQAjScA; ASP.NET_SessionId=upwolx4q2qvrjwrfrogha4rd; codeyz=f0d58ff3692695fd; gsw2017user=2731982%7cE6D7ECFD9BEC9B137376EB112B158718%7c2000%2f1%2f1%7c2000%2f1%2f1; wxopenid=defoaltid; gswZhanghao=516289196%40qq.com; gswEmail=516289196%40qq.com; wsEmail=516289196%40qq.com; idsShiwen2017=%2c7731%2c21234%2c52821%2c; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1726643501"


}
base_url = "https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx"
            # https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx

login_url = "https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx"


base_res = session.get(url=base_url,headers=headers).content.decode("utf-8")
# print(base_res)
parte = r'<img id="imgCode" style="cursor: pointer; float:left; margin-left:5px; margin-top:1px;" width="60" height="27" src="(.*?)"'
base_data = re.findall(parte,base_res)[0]
print(base_data)


img_url = "https://www.gushiwen.cn/"+ base_data

patr2 = '<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"'
VIEWSTATE = re.findall(patr2,base_res)[0]
print(VIEWSTATE)


img_resp = session.get(url=img_url,headers=headers).content
with open("img_code.png","wb") as f:
    f.write(img_resp)


img_code = chaojiying.get_code('./img_code.png')

data = {
    "__VIEWSTATE": VIEWSTATE,
    "__VIEWSTATEGENERATOR": "C93BE1AE",
    "from": "http://www.gushiwen.cn/user/collect.aspx",
    "email": "516289196@qq.com",
    "pwd": "516289196",
    "code": img_code,
    "denglu": "登录"

}

session.post(url=login_url,headers=headers,data=data)



url = "https://www.gushiwen.cn/user/collect.aspx"

res = session.get(url=url,headers=headers).content.decode("utf-8")
print(res)
