from pymysql import connect
class STU(object):
    def __init__(self):
    # 1.创建connection 连接
        self.conn = connect(host="127.0.0.1", port=3306, user='root', password='221266',database='student', charset='utf8')

        # 2.获取cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for item in self.cursor.fetchall():
            print(item)

    def show_all(self):
        sql = "select * from people;"
        self.execute_sql(sql)

    def insert_mes(self):
        shuju1 = int(input("请输入增加的学号："))
        shuju2 = input("请输入增加的姓名：")
        shuju3 = int(input("请输入增加的成绩："))
        # sql = "insert into people VALUES (%s,%s,%s)",(shuju1,shuju2,shuju3)
        self.cursor.execute("insert into people VALUES (%s,%s,%s)",(shuju1,shuju2,shuju3))
        self.conn.commit()

    def del_mes(self):
        date = int(input("请输入要删除的学号："))
        # sql = "delete from people where id = date"
        self.cursor.execute("delete from people where id = (%s)",(date))
        self.conn.commit()

    @staticmethod
    def print_list():
        print("---学生---")
        print("1: 查询所有的学生信息")
        print("2: 增加数据信息")
        print("3: 删除数据信息")
        return input("请输入功能对应的序号：")
    def run(self):
        while True:
            num = self.print_list()
            if num == "1":
                self.show_all()
            elif num == "2":
                self.insert_mes()
            elif num == "3":
                self.del_mes()
            else:
                print("输入有误，请重新输入...")


def main():
    #1.创建一个学生对象
    stu = STU()
    #2.调用这个对象的run 方法，让其运行
    stu.run()

if __name__ == '__main__':

    main()
