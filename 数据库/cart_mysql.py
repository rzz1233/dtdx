import pymysql


# courson = pymysql.connect(host="127.0.0.1", user="root", port=3306, passwd="mysql", database="cart")

class sqlControls(object):
    courson = pymysql.connect(host="127.0.0.1", user="root", port=3306, passwd="221266", database="cart")
    cur = courson.cursor()
    print("数据库已连接")
    def __init__(self):
        pass

    def select(self):
        sql = "select * from shopping"
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_cart(self):
        sql = "select * from cart"
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_coll(self):
        sql = "select * from sc"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert(self, table,**kwargs):
        res1 = tuple(kwargs.keys())
        res2 = tuple(kwargs.values())
        sql = f"insert into {table}({','.join(res1)}) values ({', '.join(['%s'] * len(res2))})"
        print(sql)
        self.cur.execute(sql,res2)
        self.courson.commit()
    def insert1(self,num,name):
        sql = f"update cart set cart_num =%s where car_name=%s"
        self.cur.execute(sql,(num,name))
        self.courson.commit()
    def insert_coll(self,name):
        sql = "insert into sc(sc_name) values (%s)"
        print(sql)
        self.cur.execute(sql,name)
        self.courson.commit()

    def delete(self,name):
        sql = "delete from cart where car_name=%s"
        self.cur.execute(sql, name)
        self.courson.commit()

    def qingkong(self):
        sql = 'truncate cart'
        self.cur.execute(sql)
        self.courson.commit()

    def __del__(self):
        self.courson.close()
        print("数据库已关闭")



if __name__ == '__main__':
    c = sqlControls()
    # c.select()
    # c.insert()
    # c.update()
    # c.delete()