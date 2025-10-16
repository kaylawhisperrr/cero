# 1. 导入 Selenium 的 WebDriver 模块
from selenium import webdriver
from selenium.webdriver.common.by import By
import time # 用于添加等待，方便观察

# 2. 创建一个浏览器驱动实例，这里使用 Chrome
#    这将启动一个全新的 Chrome 浏览器窗口
driver = webdriver.Edge()

# 3. 使用 get 方法打开一个网址
driver.get("https://www.baidu.com")

# 4. 找到网页上的元素并与之交互
#    通过元素的 ID 属性找到搜索框
search_box = driver.find_element(By.ID, "kw")

#    在搜索框中输入文本 "Selenium"
search_box.send_keys("Selenium")

#    通过元素的 ID 属性找到“百度一下”按钮
search_button = driver.find_element(By.ID, "su")

#    点击这个按钮
search_button.click()

# 5. 等待几秒，以便我们看到结果
time.sleep(5)

# 6. 关闭浏览器窗口
#    driver.close()  # 关闭当前标签页
driver.quit()   # 关闭整个浏览器并退出驱动