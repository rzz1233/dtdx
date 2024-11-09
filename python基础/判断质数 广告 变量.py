# 用户输入一个数，判断这个数是否是质数。
a = int(input("请输入："))
b = True
for i in range(2,a):
    if a%i==0:
        b = False
if b == False or a<1:
    print(a,"不是质数",sep="")
else:
    print(a,"是质数",sep="")


# 判断这个广告是否合法
str1 = input("请输入广告标语：")
list = ["最","第一","国家级","稀缺"]
# print(len(list))
for i in list:
    if i in str1:
        print("广告不合法")
        break
else:
    print("广告合法")

# 输入一个变量，判断变量是否合法
import keyword
bl =input("请输入一个变量名：")
list1 = keyword.kwlist
str1 = "0123456789"
list2 = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
        '1','2','3','4','5','6','7','8','9','0']
if bl in list1:
    print("变量不能是关键字")
for i in range(0,len(str1)):
    if bl[0] == str1[i]:
        print("变量第一个字符不能是数字")
for a in range(0,len(bl)):
    if bl[a] not in list2 :
        print("不合法")
        break
else:
    print("合法")





