# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# def moveZeroes(nums):
#     k = 0  # 指向下一个非零元素的位置
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             # 将非零元素交换到 nums[k] 位置
#             nums[k] = nums[i]
#             # 如果 i != k，说明元素发生了交换，此时需要把 nums[i] 置为 0
#             if i != k:
#                 nums[i] = 0
#             k += 1
#     return nums
#
# # 示例测试
# nums = [0, 1, 0, 3, 12]
# print(moveZeroes(nums))  # 输出: [1, 3, 12, 0, 0]





# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。
# 然后返回 nums 中与 val 不同的元素的数量。
# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
#
# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。
def removeElement(nums, val):
    k = 0  # k 用来记录非 val 元素的数量
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # 将非 val 元素放到 nums[k] 位置
            k += 1  # 增加非 val 元素的数量
    return k

# 示例测试
nums = [3, 2, 2, 3, 4]
val = 3
k = removeElement(nums, val)
print(k)  # 输出: 3
print(nums[:k])  # 输出: [2, 2, 4]，前 k 个元素为不等于 3 的元素

