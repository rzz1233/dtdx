from Crypto.Cipher import AES
import base64
import json
import requests

# 请求的URL
url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="

# 请求头信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

# 请求参数
data = {
    "csrf_token": "fdce55e035c5cdb0e0da1f2ec3af790f",
    "encodeType": "aac",
    "ids": "[27646205]",
    "level": "standard"
}

# 将数据填充至16字节的倍数
def to_16(data):
    que = 16 - (len(data) % 16)
    data += (que * chr(que).encode("utf-8"))
    return data

# AES加密函数
def jiami(data, key):
    data_bs = data.encode("utf-8")  # 数据转为字节
    key_bs = key.encode("utf-8")    # 密钥转为字节
    aes = AES.new(key_bs, AES.MODE_CBC, iv=b"0102030405060708")  # 创建AES对象
    data_bs = to_16(data_bs)  # 填充数据
    bs = aes.encrypt(data_bs)  # 加密数据
    s = base64.b64encode(bs).decode()  # 转为Base64编码
    print(s)
    return s

# 网络请求函数
def net_music(data):
    canshu1 = "010001"  # 固定参数
    canshu2 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"  # 固定参数
    canshu3 = "0CoJUm6Qyw8W8jud"  # 密钥
    i = "qtjhUg0GPSRSaIAB"  # 随机字符串

    # 生成的密钥
    encSecKey = "dd5cb42c68fe90d111b3d29185fe389a85f9566186e9594a7ae84fafdcee8ba68d08a6f33b0a407b15f7a5f15911ef998710455b2afa55d458f55f84a0305504e775c0f39bdf5c810dd1938c1a3ee61c0af2e4b64bca3f229ec60db9ab1119ee1914b994d1d9e5706f809c7dd257104143593592d1630110170a20ea950d425f"

    encText = jiami(data, canshu3)  # 第一次加密
    encText = jiami(encText, i)      # 第二次加密

    return encSecKey, encText  # 返回加密参数

if __name__ == '__main__':
    res = net_music(json.dumps(data))  # 调用网络请求函数
    encSecKey, encText = res  # 解包返回值
    print(encSecKey)  # 打印 encSecKey
    print(encText)  # 打印 params

    # 发送POST请求并获取响应
    resp = requests.post(url=url, headers=headers, data={"params": encText, "encSecKey": encSecKey}).json()
    print(resp)  # 打印响应结果
