from hashlib import md5,sha512

buf = "123456"
obj = md5()
obj.update(buf.encode("utf-8"))
miwen = obj.hexdigest()
print(miwen)


buf = "123456"
obj = sha512()
obj.update(buf.encode("utf-8"))
miwen = obj.hexdigest()
print(miwen)