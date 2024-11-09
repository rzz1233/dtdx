from selenium import webdriver
import time

import tujian
from PIL import Image
from selenium.webdriver import ActionChains


web = webdriver.Chrome(executable_path="../数据清洗/chromedriver.exe")
web.get("https://i.qq.com/")

# 切换到登录表单所在的 iframe。
web.switch_to.frame("login_frame")

web.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="u"]').send_keys("2214902667")
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="p"]').send_keys("221266cxy")

web.find_element_by_xpath('//*[@id="login_button"]').click()

time.sleep(10)
web.quit()











