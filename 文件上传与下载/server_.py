import socket, json, os

IP = "192.168.111.36"
PORT = 8081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))
server_socket.listen()

client_socket, addr = server_socket.accept()

data = client_socket.recv(1024).decode("utf-8")

data1 = json.loads(data)

#上传文件
if data1.get("opt") == "upload":
    os.chdir(r'D:\program\spt2405\文件上传与下载\上传到服务器的文件')
    #服务器文件名去重，新增
    if data1.get("file_name") in os.listdir():
        n = 1
        file_name = str(n)+"_" + data1.get("file_name")
        while file_name in os.listdir():
            n += 1
            file_name = str(n)+"_" + data1.get("file_name")
    else:
        file_name = data1.get("file_name")
    '''{'opt':'upload','file_name': 'pm_.py', 'file_data': 'import re\n\n# 从开头开始匹配，成功返回Match对象，否则就是None\n# pattern = "www"\n# string = "oksawwWswwhjgdkaswWwo"\n# res = re.match(pattern,string)\n# 从开头开始匹配，到结尾结束，成功返回Match对象，否则就是None\n# res1 = re.fullmatch(pattern,string)\n\n# 从字符串开头位置开始匹配，返回第一次拿到的Match对象，没有匹配结果，就是None\n# res1 = re.search(pattern,string,re.I)\n# 返回一个所有满足条件的结果的列表，如果都不匹配，返回空列表\n# res1 = re.findall(pattern,string)\n\n\npattern = r"1[3456789]\\d{9}"\n\nstring = "中奖号码是：1593455839，联系电话是：1552574887 1530357557"\n\n# res1 = re.sub(pattern,"1XXXXXXXXXX",string,count=2)\n\nres1 = re.split(pattern, string)\n\nprint(res1)'}'''

    os.chdir(r'D:\program\spt2405\文件上传与下载')
    with open("./上传到服务器的文件/"+file_name, "w",encoding="utf-8") as f:
        f.write(data1.get('file_data'))
#下载文件
elif data1.get("opt") == "download":
    '''{'opt':'download','file_name': 'pm_.py', 'file_data': None}'''
    with open("./上传到服务器的文件/"+data1.get("file_name"), "r",encoding="utf-8") as f:
        res = f.read()
    data1["file_data"] = res

    client_socket.send(json.dumps(data1).encode("utf-8"))

# if __name__ == '__main__':
    client_socket.close()

    server_socket.close()
