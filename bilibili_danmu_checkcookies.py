
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

# 主线任务2——发弹幕——搜索爱情公寓，在“爱情公寓爆笑合集77，休息下饭熬夜必备”视频开头发送弹幕：时代的眼泪
search_box = driver2.find_element(By.CLASS_NAME,'nav-search-input' )
search_box.click()
search_box.send_keys("爱情公寓" + Keys.RETURN)
time.sleep(2)
print('搜索成功，开始寻找视频……')

try:
    print('Path 1: 点击标题')
    video_title = driver2.find_element(By.CSS_SELECTOR, '[title = "爱情公寓爆笑合集77，休息下饭熬夜必备！"]')
    driver2.execute_script("arguments[0].click();", video_title)
    time.sleep(2)
    print('Path 1 successful')
except Exception as e:
    print(f'Path 1 fails, reason as {e}')

try:
    print('Path 2: 点击图片')
    video_photo = driver2.find_element(By.CSS_SELECTOR,"img, [alt = '爱情公寓爆笑合集77，休息下饭熬夜必备！'] ")
    driver2.execute_script("arguments[0].click();", video_photo)
    time.sleep(8)
    print('Path 2 successful')
except Exception as e:
    print(f'Path 2 fails, reason as {e}')

print("=== 查看真实搜索结果 ===")

# 获取所有视频标题
video_titles = driver2.find_elements(By.CSS_SELECTOR, ".bili-video-card__info--tit")
print(f"找到 {len(video_titles)} 个视频标题:")

for i, title in enumerate(video_titles):
    title_text = title.text
    print(f"{i+1}. {title_text}")

# 方法1：点击第一个真正的视频标题（排除广告）
try:
    print('方法1: 点击第一个真正的视频标题')
    if video_titles:
        # 使用JavaScript点击，避免遮挡
        driver2.execute_script("arguments[0].click();", video_titles[0])
        time.sleep(3)
        print(f'方法1 successful - 点击了: {video_titles[0].text}')
    else:
        print('方法1: 没有找到视频标题')
except Exception as e:
    print(f'方法1 fails: {e}')

# 方法2：如果上面失败，点击视频卡片但不点击图片（避免广告）
try:
    print('方法2: 点击视频卡片区域（非图片）')
    video_cards = driver2.find_elements(By.CSS_SELECTOR, ".bili-video-card")
    print(f"找到 {len(video_cards)} 个视频卡片")
    
    if video_cards:
        # 点击卡片的信息区域，而不是图片区域
        info_area = video_cards[0].find_element(By.CSS_SELECTOR, ".bili-video-card__info")
        driver2.execute_script("arguments[0].click();", info_area)
        time.sleep(3)
        print('方法2 successful - 点击了视频信息区域')
    else:
        print('方法2: 没有找到视频卡片')
except Exception as e:
    print(f'方法2 fails: {e}')

# 方法3：通过BV号识别真正的视频链接
try:
    print('方法3: 点击包含BV号的视频链接')
    # 真正的视频链接包含BV号，广告通常没有
    video_links = driver2.find_elements(By.CSS_SELECTOR, "a[href*='/video/BV']")
    print(f"找到 {len(video_links)} 个真实视频链接")
    
    if video_links:
        driver2.execute_script("arguments[0].click();", video_links[0])
        time.sleep(3)
        print('方法3 successful - 点击了真实视频链接')
    else:
        print('方法3: 没有找到真实视频链接')
except Exception as e:
    print(f'方法3 fails: {e}')

print("\n=== 重要提示 ===")
print("搜索结果可能不包含'爱情公寓爆笑合集77'")
print("系统根据你的偏好推荐了其他内容")
print("我们点击了搜索结果中的第一个真实视频")

input("按回车关闭浏览器...")


