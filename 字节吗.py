#把这个字符串变为字节类型
str = 'hello world'

str1 = b'hello world'  #加b后变成字节类型
print(str1,type(str1))
str2 = 'hello world'.encode('utf-8')  #encode 方法主要用于将字符串转换为指定的字节编码格式
print(str2,type(str2))
str3 = '你好'.encode('utf-8')
print(str3,type(str3))


str4 = str3.decode('utf-8')   #decode 方法用于将字节数据转换回字符串
print(str4,type(str4))

