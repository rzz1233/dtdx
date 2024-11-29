from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# 创建 Chrome 驱动
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

data = []
columns = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]

try:

    url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
    driver.get(url)
    time.sleep(2)

    # 选择 "Bond Type" 为 "Treasury Bond"
    bond_type_select = driver.find_element("xpath", '//*[@id="Bond_Type_select"]')
    bond_type_select.click()
    time.sleep(1)
    treasury_bond_option = driver.find_element("xpath", '//*[@id="Bond_Type_select"]/option[2]')
    treasury_bond_option.click()
    time.sleep(0.5)

    # 选择 "Issue Year" 为 2023
    issue_year_select = driver.find_element("xpath", '//*[@id="Issue_Year_select"]')
    issue_year_select.click()
    time.sleep(1)
    issue_year_2023_option = driver.find_element("xpath", '//*[@id="Issue_Year_select"]/option[3]')
    issue_year_2023_option.click()
    time.sleep(1)

    # 提交搜索表单
    search_button = driver.find_element("xpath", '//*[@id="resetValue"]/div/div[8]/a[1]')
    search_button.click()
    time.sleep(1)

    # 等待表格加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    while True:

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')


        table = soup.find('table')
        rows = table.find_all('tr')

        for row in rows[1:]:  # 跳过表头行
            cols = row.find_all('td')
            if len(cols) >= 6:
                isin = cols[0].text.strip()
                bond_code = cols[1].text.strip()
                issuer = cols[2].text.strip()
                bond_type = cols[3].text.strip()
                issue_date = cols[4].text.strip()
                latest_rating = cols[5].text.strip()

                # 确保筛选条件的正确性
                if bond_type == "Treasury Bond" and "2023" in issue_date:
                    data.append([isin, bond_code, issuer, bond_type, issue_date, latest_rating])


        try:
            # 获取“下一页”按钮并检查其是否禁用
            next_button = driver.find_elements("xpath", '//*[@id="pagi-bond-market"]/li[4]')
            if next_button:
                # 检查按钮是否被禁用
                if 'disabled' in next_button[0].get_attribute('class'):
                    print("已到达最后一页，退出循环")
                    break
                else:
                    next_button[0].click()
                    time.sleep(3)  # 等待页面加载
            else:
                print("没有找到“下一页”按钮，退出循环")
                break
        except Exception as e:
            print(f"出错了: {e}")
            break

finally:
    driver.quit()

# 保存数据到 CSV 文件
df = pd.DataFrame(data, columns=columns)
# df.to_csv("treasury_bonds_2023.csv", index=False, encoding="utf-8-sig")
print("数据已成功保存到 treasury_bonds_2023.csv")
