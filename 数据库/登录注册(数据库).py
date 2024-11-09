from pymysql import *
import hashlib
conn = connect(host="127.0.0.1",port=3306,user="root",password="221266",database="student",charset="utf8")
cursor = conn.cursor()

#关闭数据库
def del_db():
    cursor.close()
    conn.close()
# 加密
def md5(pw):
    m5 = hashlib.md5()
    m5.update(pw.encode('utf-8'))
    res = m5.hexdigest()
    return res
#增加数据
def insert_db(user,pw):
    pwd= md5(pw)
    cursor.execute("insert into login VALUES (%s,%s)", (user,pwd))
    conn.commit()

# 用户名检查
def check_user(user):
    for char in user:
        if char.isdigit() or char.isalpha() or char == '_':
            continue
        else:
            return False
    return True

#注册
def register():
    user = input("请输入要注册的用户名：")
    pw = input("密码：")

    cursor.execute("select * from login where user = %s",user)
    res = cursor.fetchone()
    if check_user(user):
        if res:
            print("该用户已经存在")
        else:
            insert_db(user,pw)
            print("注册完成")
    else:
        print("用户名只能为字母、下划线和数字")


#登录
def login():
    user_name = input("请输入用户名：")
    cursor.execute("select * from hei where user = %s", user_name)
    res = cursor.fetchone()
    if res:
        print("该用户已在黑名单")
    else:
        i = 3
        print(f"你有{i}次机会")
        while i>0:
            pw = input("请输入密码：")
            pwd = md5(pw)
            cursor.execute("select * from login where user = %s",(user_name))
            res = cursor.fetchone()
            if res:
                if pwd == res[1]:
                    print("登录成功")
                    break
                else:
                    print("密码错误")
                    i -= 1
                    print(f"你还有{i}次机会")
            else:
                print("该用户不存在")
                break
        if i == 0:
            add_heimingdan(user_name)
            print("你被加入黑名单")
#加入黑名单
def add_heimingdan(user):
    cursor.execute("select * from hei where user = %s", user)
    res = cursor.fetchone()
    if res:
        print("该用户已经在黑名单中，无需加入")
    else:
        cursor.execute("insert into hei VALUES (%s)", (user))
        conn.commit()
        print("添加成功")
#删除黑名单
def del_heimingdan(user):
    cursor.execute("select * from hei where user = %s", user)
    res = cursor.fetchone()
    if res:
        cursor.execute("delete from hei where user = %s",user)
        conn.commit()
        print("删除成功")
    else:
        print("该用户不在黑名单中，无需删除")
#查看黑名单
def check_heimingdan():
    cursor.execute("select * from hei")
    res = cursor.fetchone()
    print("黑名单：")
    for i in res:
        print(f"\t\t{i}")
#管理员身份
def manage():
    name = input("请输入管理员的用户名：")
    pw = input("请输入密码：")
    cursor.execute("select * from manage where name = %s",name)
    res = cursor.fetchone()
    if res:
        if pw == res[1]:
            root()
        else:
            print("密码错误")
    else:
        print("该用户不是管理员")
#进入管理员身份
def root():
    while True:
        print('-' * 50)
        print('欢迎进入管理员功能:')
        print('请选择功能：\n'
              '\t\t1.添加黑名单用户\n'
              '\t\t2.删除黑名单用户\n'
              '\t\t3.查看黑名单用户\n'
              '\t\tq.退出')
        print('-' * 50)
        choice = input("请输入你的操作:")
        if choice == '1':
            user_h = input("请输入你要加入黑名单的用户：")
            add_heimingdan(user_h)
        elif choice == '2':
            user_h_del = input("请输入你要删除的黑名单用户：")
            del_heimingdan(user_h_del)
        elif choice == '3':
            check_heimingdan()
        elif choice == 'q':
            break
        else:
            print("没有该操作")
def main():
    while True:
        print("**" * 50)
        print("\t\t欢迎进入注册登录查找界面：\n"
              "\t\t\t1. 注册\n"
              "\t\t\t2. 登录\n"
              "\t\t\t3. 进入管理员身份\n"
              "\t\t\tq. 退出")
        print("**" * 50)
        choice = input("请输入你的操作：")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            manage()
        elif choice == "q":
            break
        else:
            print("没有该操作")
    del_db()

if __name__ == '__main__':
    main()
