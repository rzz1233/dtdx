import random
a = random.randint(1, 10)
while True:
    i = int(input("请输入："))
    if i>a:
        print("猜大了")
    elif i<a:
        print("猜小了")
    else:
        print("猜对了")
        break
