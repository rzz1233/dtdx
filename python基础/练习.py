#2 +4 +6 +8 +....+ 64
# sum = 0
# for i in range(2,65,2):
#     sum += i
# print(sum)

#1/2 + 1/4 + 1/8+....+ 1/64
# sum = 0
# for i in range(1,7):
#         sum += 1/2**i
# print(sum)

#输出1~100之间所有和7 关联的数据
# for i in range(1,100):
#     if i%7==0 or i//10==7 or i%10==7:
#         print(i,end=" ")

#输出100~1001之间的水仙花数
# for i in range(100,10001):
#     a = i%10
#     b = i//10%10
#     c= i//100%10
#     d = i//1000
#     if a**3+b**3+c**3==i:
#         print(i)
#输出100~10001之间的水仙花数
# for i in range(100 ,10002):
#     s = str(i)
#     if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
#         print(i)

#回文数
while True:
    s = input("请输入:")
    if s==s[::-1]:
        print(s,"是回文数")
    else:
        print(f"{s}不是回文数")
