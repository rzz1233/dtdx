import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
class Cart(object):
    def __init__(self):
        self.goodList = [{'name': '笔记本电脑', 'price': 8000}, {'name': '鼠标', 'price': 100}]
        self.cartList = []
        self.collectSet = set()
class Cart_manage(object):
    def add_cart(self,goodList,cartList,name,number):
        goods = {}
        for good in goodList:
            if name == good['name']:
                if number == "":
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] = 1
                else:
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] = int(number)
        if goods != {}:
            if cartList == []:
                cartList.append(goods)
            else:
                for cart in cartList:
                    if cart['name'] == goods['name']:
                        cart['number'] = cart['number'] + int(number)
                        break
                else:
                    cartList.append(goods)
        else:
            print("没有该商品")
    def coll_cart(self,name,goodList,collectSet):
        for good in goodList:
            if name == good['name']:
                collectSet.add(name)
        print("收藏：", collectSet)

    def del_cart(self,cartList, name):
        if len(cartList) == 0:
            print("购物车为空。")
        else:
            for cart in cartList:
                if cart['name'] == name:
                    cartList.remove(cart)

    def buy(self,name,number,cartList):
        sum = 0
        if len(cartList) == 0:
            print("购物车是空的，快去添加吧。")
        else:
            for good in cartList:
                if name == good['name']:
                    if number == "":
                        sum += good['price'] * good['number']
                    elif int(number) > 0 and int(number) <= int(good['number']):
                        sum += good['price'] * int(number)
                        a = good['number'] - int(number)
                        good['number'] = a
                        print("花费：", sum)
                        if good['number'] == 0:
                            cartList.remove(good)
                    elif int(number) > int(good['number']):
                        print("购物车中该商品没有这么多数量")
                elif name == "":
                    for good in cartList:
                        price = good["price"]
                        number = good["number"]
                        sum += price * number
                    print("花费：", sum)
                    cartList.clear()
        with open("buy1.txt", "a", encoding="utf-8") as f1:
            a = time.strftime("%Y-%m-%d %H:%M:%S")
            f1.write(f"{a}结算的商品是：{name},结算数量是{number},共计{int(sum)}元\n")
    def clear_cart(self,cartList):
        cartList.clear()

    def add_new_good(self,name,price,goodList):
        goods = {}
        try:
            if price < 0:
                raise ValueError("价格不能是负数")
        except ValueError:
            print("价格不能是负数")
            logging.error('价格不能是负数')
        goods['name'] = name
        goods['price'] = price
        if goods not in goodList:
            goodList.append(goods)
        with open("newgoods.txt", "a", encoding="utf-8") as f:
            b = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{b}添加了新商品：{goods['name']}，价格是{price}\n")

    def look_cart(self,cartList):
        print("❤" * 50)
        if len(cartList) == 0:
            print("您的购物车为空")
        else:
            print("您的购物车：")
            for a in range(len(cartList)):
                print(f"{cartList[a]['name']}：${cartList[a]['price']} 数量：{cartList[a]['number']}个")
        print("❤" * 50)
class Cart_view(object):

    def menu(self):
        print("**" * 50)
        print("\t\t购物车，有以下操作：\n"
              "\t\t\t1. 加入购物车\n"
              "\t\t\t2. 收藏商品\n"
              "\t\t\t3. 删除购物车商品\n"
              "\t\t\t4. 去结算\n"
              "\t\t\t5. 清空购物车\n"
              "\t\t\t6. 查看购物车\n"
              "\t\t\t7. 添加新商品\n"
              "\t\t\tq. 退出")
        print("**" * 50)
    def good_menu(self,goodList):
        print("<>" * 50)
        print("\t\t商品列表：")
        for i in range(len(goodList)):
            print("\t\t\t", goodList[i]['name'], "：", "$", goodList[i]['price'])
        print("<>" * 50)

    def main(self):
        cart = Cart()
        cart_manage = Cart_manage()
        while True:

            self.good_menu(cart.goodList)
            choice = input("请输入你的选择：")
            if choice == "1":
                name = input("请输入加入的商品：")
                number = input("请输入数量：")
                cart_manage.add_cart(cart.goodList,cart.cartList,name,number)

            elif choice == "2":
                name = input("请输入要收藏的商品：")
                cart_manage.coll_cart(name,cart.goodList,cart.collectSet)
            elif choice == "3":
                name = input("请选择要删除的商品：")
                cart_manage.del_cart(cart.cartList,name)
            elif choice == "4":
                name = input("请输入要结算的商品：")
                number = input("请输入要结算的商品数量：")
                cart_manage.buy(name,number,cart.cartList)
            elif choice == '5':
                cart_manage.clear_cart(cart.cartList)
            elif choice == '6':
                cart_manage.look_cart(cart.cartList)
            elif choice == '7':
                name = input("请输入要添加的新商品：")
                price = int(input("请输入要添加新商品的价格："))
                cart_manage.add_new_good(name,price,cart.goodList)
            elif choice == 'q':
                print("退出")
                break
            else:
                print("没有这个操作")
if __name__ == '__main__':
    cart_view = Cart_view()
    cart_view.menu()
    cart_view.main()
