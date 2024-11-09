import base64

buf = "hello,yangmi"
# 编码  --》 伪加密
res = base64.b64encode(buf.encode("utf-8"))
# print(res)
print(res.decode("utf-8"))

#解码
mingwen = base64.b64decode(res)
# print(mingwen)
print(mingwen.decode("utf-8"))
