from selenium import webdriver
import time
wed =webdriver.Chrome(executable_path="../数据清洗/chromedriver.exe")
wed.get("https://www.baidu.com")
wed.find_element_by_id("kw").send_keys("杨幂") #输入框输入
wed.find_element_by_id("su").click()


time.sleep(5)
wed.quit()