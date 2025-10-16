

from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import os
import time

driver = webdriver.Edge()

driver.get('https://www.bilibili.com/')
input("请手动完成登录，然后按回车...")

# 步骤2：登录成功后，立即获取cookies
cookies = driver.get_cookies()  # 获取当前已设置的所有cookies
print(f"获取到 {len(cookies)} 个cookies")

# 步骤3：保存cookies供以后使用
with open("bilibili_cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

driver.quit()

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