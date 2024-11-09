while True:
    choice = input("请输入你的选择（1.加密，2.解密，3.退出）：")
    if choice == "1":
        str1 = input("请输入要加密的：")
        str2 = ""
        for i in range(0,len(str1)):
            a = str(ord(str1[i]))

            str2 += a
        print("加密后为："+str2)

    elif choice == "2":
        num_input = input("输入你要解密的信息：")
        str4 = ""
        ch = int(len(num_input)/5)
        for i in range(1,ch+1):
            str3 = num_input[i*5-5:i*5]
            str4 += chr(int(str3))
        print("解密后为：",str4)
    elif choice == "3":
        break
    else:
        print("输入错误")


# list =[]
# str1 = "今天是个好日子"
# for i in range(len(str1)):
#     print(ord(str1[i]),end=' ')
#     list.append(ord(str1[i]))
# for i in list:
#     print(chr(i),end='')