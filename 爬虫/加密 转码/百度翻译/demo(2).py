import execjs


node = execjs.get()
etx = node.compile(open("baidu.js", encoding="utf-8").read())
t = input("请输入单词")
i = "320305.131321201"

funcName = "lv('{0}','{1}')".format(t,i)
sign = etx.eval(funcName)
print(sign)


