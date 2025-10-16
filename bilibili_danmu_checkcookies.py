from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import os
import time




# 第二次：使用保存的cookies自动登录
print("=== 第二次运行：使用cookies自动登录 ===")
driver2 = webdriver.Edge()
driver2.get('https://www.bilibili.com/')  # 先访问域名

# 从文件加载cookies
with open("bilibili_cookies.pkl", "rb") as f:
    saved_cookies = pickle.load(f)

# 将cookies添加到新浏览器实例
for cookie in saved_cookies:
    driver2.add_cookie(cookie)

driver2.refresh()  # 刷新页面，应用cookies
# 现在应该已经是登录状态了！
time.sleep(5)

