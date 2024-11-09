from urllib.parse import urlencode,unquote

base_url = "https://www.baidu.com/s?"

parmam_dic = {
    "wd":"杨幂"
}
# 编码
result = urlencode(parmam_dic)
print(result)
url = base_url + result
print(url)

