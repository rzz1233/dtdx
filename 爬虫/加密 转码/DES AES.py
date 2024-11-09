from Crypto.Cipher import AES,DES
import base64

#
# s = "我喜欢杨幂"
#
# aes = AES.new(b'lvweiqiangairose',mode=AES.MODE_CBC,IV=b"0102030405060708")
# print(aes)
# bs = s.encode("utf-8")
#
# que = 16 -(len(bs) %16)
# bs += (que* chr(que).encode("utf-8"))
# res = aes.encrypt(bs)
# bs64_str = base64.b64encode(res)
# miwen = bs64_str.decode("utf-8")
# print(miwen)

# 解密 加密不能用同一个实例化对象
miwen = "CeFpds9Z1KJ6k4fJ1oCwLA=="
aes = AES.new(b'lvweiqiangairose',mode=AES.MODE_CBC,IV=b"0102030405060708")

bs = base64.b64decode(miwen)
res = aes.decrypt(bs).decode("utf-8")
print(res)