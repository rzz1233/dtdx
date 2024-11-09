import socket, json, os.path
# 上传
# 操作 文件名  文件内容
def Upload(opt_dic):
    file_upload_dic = {"opt":opt_dic.get(buf),"file_name":None,"file_data":None}
    file_path = input("请输入你要上传的文件路径>>>")
    # D:\program\spt2405\正则表达式\re模块.py
    file_name = os.path.basename(file_path)

    with open(file_path,"r", encoding="utf-8") as f:
        res = f.read()

    file_upload_dic["file_name"] = file_name
    file_upload_dic["file_data"] = res

    data = json.dumps(file_upload_dic,ensure_ascii=False).encode("utf-8")

    client_socket.send(data)
# 下载
# 文件名 内容 路径
# 可以查看服务器有哪些文件下载
def Download(opt_dic):
    file_download_dic = {"opt": opt_dic.get(buf), "file_name": None, "file_data": None}
    file_name = input("请输入你要下载的文件名>>>")

    file_download_dic["file_name"] = file_name

    download_data = json.dumps(file_download_dic,ensure_ascii=False).encode("utf-8")

    client_socket.send(download_data)

    res = json.loads(client_socket.recv(1024).decode("utf-8"))

    with open("./下载到本地的文件/" + file_name, "w", encoding="utf-8") as f:
        f.write(res.get('file_data'))
def check_upload():
    os.chdir(r'D:\program\spt2405\文件上传与下载\上传到服务器的文件')
    print("服务器可下载文件:")
    for i in os.listdir():
        print(i)

if __name__ == '__main__':
    IP = "192.168.111.36"
    PORT = 8081

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((IP, PORT))

    opt_dic = {"1": "upload", "2": "download", "3": "check_upload"}
    while True:
        buf = input("请输入您的选择>>>")
        if buf == "1":
            Upload(opt_dic)
        elif buf == "2":
            Download(opt_dic)
        elif buf == "3":
            check_upload()
        elif buf == "q":
            break
