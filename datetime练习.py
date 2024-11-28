from datetime import datetime, timedelta
def get_time_in_range(start_time, end_time):
    # 定义时间格式
    time_format = "%Y/%m/%d %H:%M:%S"

    # 将字符串时间转换为 datetime 对象
    start = datetime.strptime(start_time, time_format)   #用于将字符串（str）转换为 datetime 对象
    end = datetime.strptime(end_time, time_format)

    # 存储结果
    time_list = []

    # 从 start 开始，循环到 end，步长为 1 小时
    current_time = start
    while current_time < end:
        # 将当前时间格式化为字符串，按小时表示
        time_list.append(current_time.strftime("%Y/%m/%d/%H/"))   #strftime用于将 datetime 对象格式化为字符串
        # 增加 1 小时
        current_time += timedelta(hours=1)  #timedelta 可以与 datetime 对象进行加减运算

    return time_list

# 测试
start_time = "2018/11/12 21:01:01"
end_time = "2018/11/13 01:01:01"
result = get_time_in_range(start_time, end_time)
print(result)