import requests

url = "https://www.baidu.com"
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"


}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
print(response.text)

# print(response.content.decode('utf-8'))#字节解码

print(response.request.headers) #请求响应头
print(response.status_code) #状态码


# data = response.text
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(data)
