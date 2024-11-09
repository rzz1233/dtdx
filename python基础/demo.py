# print("hello world")
# 关键字
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# 复数
a = 1-1j
print(a.real)  #打印实部
print(a.imag)  #打印虚部

import sys
#整数取值范围
print(-sys.maxsize-1)
print(sys.maxsize)

#类型
print(type(""))
print(type({1:1,1:5}))  #字典类型
print(type([]))
print(type((1,2)))
print(type(1))
print(type(set()))
print(type({1,2}))  #集合整型



# a=int(input("请输入："))
# b=int(input("请输入："))
# c=int(input("请输入："))
#
# if a>=b:
#     if a>=c:
#         print("最大是：",a)
#     else:
#         print("最大是：",c)
# else:
#     if b >= c:
#         print("最大是：", b)
#     else:
#         print("最大是：", c)

print(~3)
print(~(-3))
#-(n+1)按位取反
str = ""