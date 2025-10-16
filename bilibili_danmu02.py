from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pickle
import os
import time

def setup_driver():
    """设置Edge浏览器选项"""
    options = Options()
    # 添加一些选项来减少错误和提升稳定性
    options.add_argument('--disable-features=msEdgeVbsEnclave')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Edge(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

print("\n=== 第二次运行：使用cookies自动登录 ===")
driver2 = setup_driver()   #WTH 怎么没用这个函数也能成功？


try:
    # 先访问首页
    driver2.get('https://www.bilibili.com/')
    
    # 删除所有现有cookies
    driver2.delete_all_cookies()  #最好加上，清空了"新开的这个浏览器窗口"里所有B站的登录状态，为重新添加保存的cookies做准备
    
    # 加载保存的cookies
    with open("bilibili_cookies.pkl", "rb") as f:
        saved_cookies = pickle.load(f)
    
    print(f"加载了 {len(saved_cookies)} 个cookies")
    
    # 添加cookies


    for cookie in saved_cookies:
        try:
            # 确保cookie格式正确
            if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie['sameSite'] = 'Lax'
            driver2.add_cookie(cookie)
        except Exception as e:
            print(f"添加cookie时出错: {e}")
            continue

  
    # 刷新页面应用cookies
    driver2.refresh()
    
    # 等待页面加载
    time.sleep(5)
    
    # 验证登录状态
    try:
        # 检查是否有用户头像等登录标识
        user_elements = driver2.find_elements(By.CLASS_NAME, "header-avatar")
        if user_elements:
            print("✅ 自动登录成功！")
        else:
            print("❌ 自动登录可能失败，请检查cookies是否有效")
    except:
        print("⚠️ 无法确定登录状态，但页面已刷新")
    
    # 保持浏览器打开一段时间以便观察
    input("按回车关闭浏览器...")
    
finally:
    driver2.quit()