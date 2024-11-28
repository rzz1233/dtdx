# 将未排序的数据插入到已排序序列中的适当位置，从而得到最终的有序数组
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 待插入的元素
        j = i - 1

        # 将大于 key 的元素向右移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 插入 key 到正确位置

    return arr


arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("排序后的数组:", sorted_arr)
