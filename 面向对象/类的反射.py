class MyClass:
    def __init__(self, x):
        self.x = x

    def greet(self):
        return f"Hello, {self.x}!"

# 创建对象
obj = MyClass("World")

# 使用反射获取属性
if hasattr(obj, 'x'):
    print(getattr(obj, 'x'))  # 输出: World

# 使用反射设置属性
setattr(obj, 'x', 'Python')
print(getattr(obj, 'x'))  # 输出: Python

# 使用反射调用方法
if hasattr(obj, 'greet'):
    method = getattr(obj, 'greet')
    print(method())  # 输出: Hello, Python!

# 删除属性
delattr(obj, 'x')
print(hasattr(obj, 'x'))  # 输出: False
