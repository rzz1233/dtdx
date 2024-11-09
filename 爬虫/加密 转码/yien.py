import requests
from Crypto.Cipher import AES,DES
import binascii

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"

}

url = "https://www.endata.com.cn/API/GetData.ashx"

data = {
    "year": "2024",
    "MethodName": "BoxOffice_GetYearInfoData"
}

data = requests.post(url=url,headers=headers,data=data).text
print(data)


def fn(n1,n2,n3):
    if 0 == n2:
        return n1[n3:]
    res = n1[:n2]
    res += n1[(n2+n3):]
    return res

a = int(data[-1],16) + 9
b = int(data[a],16)
data = fn(data,a,1)
a = data[b:b+8]
data = fn(data,b,8)
b = a.encode("utf-8")
a = a.encode("utf-8")

ds = binascii.a2b_hex(data)

des = DES.new(b,mode=DES.MODE_ECB)
result = des.decrypt(ds).decode("utf-8")
print(result)

