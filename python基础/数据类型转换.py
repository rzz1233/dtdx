# a = input("请输入：")
# print(a,type(a))
# a = int(input("请输入："))
# print(a,type(a))

# 字符串
print(int('123'))
print(float('123'))
print(bool('123'))
print(list('123'))
print(tuple('123'))
print(set('123'))
#整型
print(float(112))
print(str(123)) #万物可转字符串，只有数字是整数的字符串才能转成整数print(int("ss"))
print(bool(1))
print(bool(0))
#浮点
# 浮点型 == 整型
print(int(4.9))
# 浮点 ==> bool
print(bool(0.0))
# 浮点 ==> 字符串
print(str(4.5))#列表

#列表
print(type(str([1,2,3])))
print(dict([[1,2],[3,6]]))
print(tuple([1,2,3]))
print(set([1,2,3]))

#元组
print(list((1,2,3)))
print(set((1,2,3)))
print(dict(((1,2),(2,3))))
print(str((1,2,3)))

#字典
print(set({1:1,3:4}))
print(tuple({1:1,3:4}))
print(list({1:1,3:4}))
print(type(str({1:1,3:4})))