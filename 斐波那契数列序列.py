# 递归：
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#
# print(fibonacci_recursive(10))

# 迭代
# def fibonacci_iterative(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
#
# print(fibonacci_iterative(1))


# 生成器
def fibonacci_generator(n):
    a,b = 0,1
    count = 0
    while count <= n:
        yield a
        a,b = b,a+b
        count += 1

for i in fibonacci_generator(10):
    print(i)

