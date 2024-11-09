from selenium import webdriver
import time
web = webdriver.Chrome(executable_path="../数据清洗/chromedriver.exe")
import tujian
from PIL import Image
from selenium.webdriver import ActionChains


web.get("https://login.jiayuan.com/")
time.sleep(1)
web.find_element_by_xpath('//*[@id="login_email"]').send_keys("17835397996")
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="login_password"]').send_keys("lwq516289196")

web.find_element_by_xpath('//*[@id="login_btn"]').click()

# 验证码图像部分
verfity = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[6]')
time.sleep(1)
# 全页面截图
web.save_screenshot("login.png")
# 获取验证码位置和大小进行截图裁剪
left = verfity.location["x"]
right = left + verfity.size['width']
top = verfity.location["y"]
bottom = top + verfity.size['height']

im = Image.open("login.png")
mg = im.crop((left,top,right,bottom))
mg.save("yz.png")


result = tujian.get_image_axis("yz.png")
for p in result.split("|"):
    x = int(p.split(",")[0])
    y = int(p.split(",")[1])
    time.sleep(1)
    # 模拟点击验证码
    ActionChains(web).move_to_element_with_offset(verfity,xoffset=x,yoffset=y).click().perform()
time.sleep(0.5)
web.find_element_by_xpath('/html/body/div[3]/div[2]/div[6]/div/div/div[3]/a').click()
time.sleep(10)
print(web.get_cookies())
web.quit()











