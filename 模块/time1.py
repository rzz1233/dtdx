import time
from datetime import datetime
# print(time.localtime())
# print(time.asctime())
# print(time.time())
# print(time.strftime("%x %X"))
# print(datetime.now())


love = datetime(2023,3,12)
print(love)
today = datetime.now()
print(today)
days = today - love
print("❤：",days)
