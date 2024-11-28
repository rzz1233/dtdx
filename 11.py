# a = [1,2,3,4,5,6,7,8,9]
# a= set(a)
# print(a)
# b=[x for x in a]
# print(b)

# b=sum(a)
# print(b)

# for i in a[::-1]:
#
#     print(i)


# 列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25]，并使用列表推
# 导式提取出大于10的数，最终输出[16,25]？\

# a = [1,2,3,4,5]
# def func(x):
#     return x**2
#
# b = map(func, a)
# list1 = list(b)
#
# list2 = [x for x in list1 if x>10]
# print(list2)


# a = [[1,2,3],[4,5,6],[7,8,9]]
# b= [x for i in a for x in i]
# print(b)
#
# import numpy as np
# c = np.array(a)
# print(c)



# a = [1,2,3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9]
# c = zip(a,b)
# list = list(c)
# print(list)

# str = '方法'.encode('utf-8')
# print(str)


# str = 'adad'
#
# print(str.capitalize())  #第一个字母大写

# a = ["a",5]
# a.remove("a")
# print(a)

# a = [1,2,3]
# for i in range(0,len(a)):
#     a[i] = float(a[i])
# b = max(a)
# print(b)


# lis = [1,2,2,2,3]
# lis2 = list(set(lis))
# print(lis2)

# a = "111"
# b = "111"
# c = [1,2,3]
# d = [1,2,3]
# print(a is b)
# print(c is d)


s = "A man, a plan, a canal: Panama"
lis = []
for i in s:
    if i.isalnum():
        a = i.lower()
        lis.append(a)
str = ''.join(lis)
print(str)
if str == str[::-1]:
    print(True)
else:
    print(False)
# filtered_str = ''.join(c.lower() for c in s if c.isalnum())
# print(filtered_str)






