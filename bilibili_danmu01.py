

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


# 主线任务2——发弹幕——搜索爱情公寓，在“爱情公寓爆笑合集77，休息下饭熬夜必备”视频开头发送弹幕：时代的眼泪
search_box = driver.find_element(By.CLASS_NAME, "nav-search-content")
search_box.send_keys("爱情公寓" + Keys.RETURN)

card_goal = driver.find_element(By.CSS_SELECTOR, '#i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div > div.video.i_wrapper.search-all-list > div > div:nth-child(3) > div > div.bili-video-card__wrap > div.bili-video-card__info > div > a > h3')

card_goal.click()

time.sleep(5)

