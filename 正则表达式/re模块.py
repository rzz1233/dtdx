import re

# pattern = "www"
# string = "www.com"
# #从开头开始匹配(只看开头），成功返回match对象，否则就是None
# res = re.match(pattern, string,re.I)#不区分大小写
# print(res)


# pattern = "www"
# string = "dwwwsdsfdwww.com"
# 从字符串开头位置开始匹配，返回第一次拿到的Match对象，没有匹配结果，就是None
# res1 = re.search(pattern, string)
# print(res1)

pattern = "www"
string = "dswwWdsfdwww.com"
#返回所有满足条件的组成一个列表，如果没有则返回一个空列表
res1 = re.findall(pattern, string, re.I)
print(res1)

# pattern = r"1[3456789]\d{9}"
# string = "中奖号码：18295758880，联系电话： 15525748876"
# #替换符合pattern，将其替换为repl
# res1 = re.sub(pattern,"1XXXXXXXXXX", string )
# print(res1)
#
# #将符合pattern的做为分割符，返回一个列表
# res2 = re.split(pattern, string)
# print(res2)
