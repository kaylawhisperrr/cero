from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import os
import time

# 第二次：使用保存的cookies自动登录
print("=== 第二次运行：使用cookies自动登录 ===")
driver2 = webdriver.Edge()
driver2.get('https://www.bilibili.com/video/BV18W411u7Pq/?spm_id_from=333.1387.favlist.content.click&vd_source=d052560f62aee54572b5f015f5161c82')  # 先访问域名

# 从文件加载cookies
with open("specfbilibili_cookies.pkl", "rb") as f:
    saved_cookies = pickle.load(f)

# 将cookies添加到新浏览器实例
for cookie in saved_cookies:
    driver2.add_cookie(cookie)

driver2.refresh()  # 刷新页面，应用cookies
# 现在应该已经是登录状态了！
time.sleep(5)

#发送弹幕
danmu_box = driver2.find_element(By.CSS_SELECTOR, "input[placeholder = '发个友善的弹幕见证当下']")
driver2.execute_script("arguments[0].click();", danmu_box)
danmu_box.send_keys("时代的眼泪" + Keys.RETURN)
time.sleep(10)
print('弹幕发送成功🍻')
