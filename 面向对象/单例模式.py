
# 单例模式（Singleton Pattern）是一种设计模式，它的目的是确保一个类只有一个实例，并提供一个全局访问点。
# 单例模式在需要一个对象被共享使用、避免资源浪费或者需要控制实例的数量时非常有用。
class Singleton(object):
    # 记录第一个被创建对象的引用
    _instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # 如果没有实例，就创建一个新的  以后每次创建 Singleton 对象时，都会返回已存在的 _instance。
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Singleton.init_flag:
            print("初始化音乐播放器")

        Singleton.init_flag = True

# 测试单例模式
obj1 = Singleton()
obj2 = Singleton()
print(obj1)
print(obj2)
print(obj1 is obj2)  # 输出: True

# ，Singleton 类使用 __new__ 方法确保只有一个实例存在。当第一次创建 Singleton 对象时，
# _instance 是 None，于是创建一个新的实例。以后每次创建 Singleton 对象时，都会返回已存在的 _instance。
