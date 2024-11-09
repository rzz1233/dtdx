class Example:
    class_variable = 1
    # 类方法：使用 @classmethod 装饰器，第一个参数为 cls，表示类本身。可以通过类或实例调用，通常用于工厂方法。
    @classmethod
    def class_method(cls):
        print(f"Class variable is: {cls.class_variable}")

    # 静态方法 可以通过类或实例调用，但不访问实例或类的属性。
    @staticmethod
    def static_method():
        print(f"This is a static method.")
example = Example()
# 调用类方法和静态方法
Example.class_method()  # 输出: Class variable is: 0

Example.static_method() # 输出: This is a static method.
example.static_method() # 输出: This is a static method.
