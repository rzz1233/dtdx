# 生成器是通过普通函数定义，但使用 yield 关键字代替 return。每次调用 yield 时，函数暂停执行，并返回一个值给调用者。
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# for value in my_generator():
#     print(value)  # 输出: 1, 2, 3



# 生成器实现一个斐波那契数列生成器。
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a  #yield：yield 是一个类似于 return 的关键字
        a, b = b, a + b
        count += 1

# 使用生成器
for num in fibonacci_generator(10):
    print(num,end=" ")

