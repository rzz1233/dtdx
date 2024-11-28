# 每一趟从待排序的元素中选出最小（或最大）的元素，与当前元素交换位置，直到整个序列有序。
def selection_sort(arr):
    # 遍历数组
    for i in range(len(arr)):
        # 找到最小的元素索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # 交换当前元素与找到的最小元素
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 示例
arr = [64, 25, 12, 22, 11]
print("排序前:", arr)
sorted_arr = selection_sort(arr)
print("排序后:", sorted_arr)
