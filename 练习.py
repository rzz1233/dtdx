# 7. 给定一组由小到大的数字0,1,2...,n，从中找出一个丢失的数字。
# 例如，给定nums = [0, 0, 1, 3, 4]返回2。

# nums = [0, 0, 1, 3, 4]

# def fun1(nums):
#     nums = list(set(nums))
#     a = len(nums)
#     num1 = a*(a+1)//2
#     num2 = sum(nums)
#     result = num1 - num2
#     return result
#
# print(fun1(nums))


#8.给定一个字符串，里边可能包含“()”、"{}"两种括号，请编写程序检查该字符串的括号是否成对出现。
# 输出：
# true：代表括号成对出现并且嵌套正确，或字符串无括号字符。
# false：未正确使用括号字符。




# 9.请编写代码实现一个【单例】类MoreFun，要求该类的__init__函数只能被调用一次

# class MoreFun(object):
#     _instance = None
#     # 记录是否执行过初始化动作
#     init_flag = False
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self):
#         if not MoreFun.init_flag:
#             print("初始化")
#
#         MoreFun.init_flag = True
#
# obj = MoreFun()
# print(obj)
# obj2 = MoreFun()
# print(obj2)




# def solution(nums,target):
#     List = []
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 List.append(i)
#                 List.append(j)
#     return List
#
#
# nums = [1,2,3,4,5]
# target = 5
# print(solution(nums,target))




# from datetime import datetime, timedelta
# def get_time_in_range(start_time, end_time):
#     time_format = "%Y/%m/%d %H:%M:%S"
#
#     start = datetime.strptime(start_time, time_format)   #用于将字符串（str）转换为 datetime 对象
#     end = datetime.strptime(end_time, time_format)
#
#     list = []
#
#     while start < end:
#
#         list.append(start.strftime("%Y/%m/%d/%H/"))
#
#         start += timedelta(hours=1)
#
#     return list
#
# # 测试
# start_time = "2018/11/12 21:01:01"
# end_time = "2018/11/13 01:01:01"
# result = get_time_in_range(start_time, end_time)
# print(result)



# 8.给定一个字符串，里边可能包含“()”、"{}"两种括号，请编写程序检查该字符串的括号是否成对出现。
# 输出：
# true：代表括号成对出现并且嵌套正确，或字符串无括号字符。
# false：未正确使用括号字符。
# def check_parentheses(s):
#     # 创建一个空栈
#     stack = []
#     # 括号映射关系，键是右括号，值是对应的左括号
#     matching_brackets = {')': '(', '}': '{'}
#
#     # 遍历字符串中的每个字符
#     for char in s:
#         # 如果是左括号，则压入栈
#         if char in '({':
#             stack.append(char)
#         # 如果是右括号，则检查栈是否为空且栈顶元素是否匹配
#         elif char in ')}':
#             # 如果栈为空或栈顶元素不匹配，返回 False
#             if not stack or stack[-1] != matching_brackets[char]:
#                 return False
#             stack.pop()  # 弹出栈顶元素
#
#     # 如果栈为空，则说明所有括号成对出现且嵌套正确，否则返回 False
#     return len(stack) == 0

# 测试
# print(check_parentheses("(){}"))  # 输出: True
# print(check_parentheses("({sss})"))  # 输出: True
# print(check_parentheses("{(})"))  # 输出: False
# print(check_parentheses("(()"))  # 输出: False
# print(check_parentheses("(){}{}"))  # 输出: True
# print(check_parentheses(""))  # 输出: True



# num1 = [1,2,3,0,0,0]
# num2 = [1,2,3]
# num1[3:] = num2
# print(num1)








def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # 初始时，nums[0] 是唯一的
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:  # 找到一个与前一个元素不同的元素
            nums[k] = nums[i]  # 更新 nums[k] 为新的唯一元素
            k += 1  # 增加唯一元素的数量

    return k

# 示例测试
nums = [1, 1, 2]
print(removeDuplicates(nums))  # 输出: 2
print(nums)  # 输出: [1, 2, _]


