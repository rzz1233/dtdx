# 通过一个“基准元素”将待排序数组分成两部分，然后分别对这两部分递归地进行快速排序。快速排序的平均时间复杂度为 O(n log n)，
# 但是在最坏情况下时间复杂度为 O(n²)。
def quick_sort(arr):
    # 基本情况：如果数组为空或只有一个元素，返回数组
    if len(arr) <= 1:
        return arr
    # 选择基准元素（这里选择第一个元素作为基准）
    pivot = arr[0]
    # 划分：将比基准小的元素放在左边，比基准大的元素放在右边
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    # 递归排序并合并结果
    return quick_sort(left) + [pivot] + quick_sort(right)

# 示例
arr = [64, 25, 12, 22, 11]
print("排序前:", arr)
sorted_arr = quick_sort(arr)
print("排序后:", sorted_arr)
