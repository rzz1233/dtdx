# 二分查找（前提：lst 已排序）
# def binary_search(lst, target):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
# list = [1,2,3,4,5,6,7,8,9]
# target = 9
# print(binary_search(list, target))


def select_sort(lis, n):
    left,right = 0, len(lis)-1
    while left <= right:
        mid = (left+right)//2
        if lis[mid] == n:
            return mid
        elif lis[mid] < n:
            left = mid+1
        else:
            right = mid-1
    return -1
list = [1,2,3,4,5,6,7,8,9]
n = 9
print(select_sort(list, n))
