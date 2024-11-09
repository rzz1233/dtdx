import hashlib
#MD5
pw = "hello"
m5 = hashlib.md5()
m5.update(pw.encode('utf-8'))
buf = m5.hexdigest()
print(buf)
#SHA1
sh1 = hashlib.sha1()
sh1.update(pw.encode('utf-8'))
buf1 = sh1.hexdigest()
print(buf1)