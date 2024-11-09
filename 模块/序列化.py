import json
# JSON 序列化是将对象转换为 JSON 格式的过程。JSON（JavaScript Object Notation）是一种轻量级的数据交换格式
# ，广泛用于客户端和服务器之间的数据传输。
# JSON 序列化通常用于将编程语言中的对象或数据结构（如字典、列表等）转换成 JSON 字符串，以便进行存储或传输。
dic = {'name':'rzz','age':18}
dic1 = json.dumps(dic)

with open('test3.txt','r',encoding="utf-8") as f:
    # f.write(dic1)

    res = f.read()
    res1 = json.loads(res)
print(type(res))
print(type(res1))
