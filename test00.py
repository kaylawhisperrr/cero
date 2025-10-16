import requests
def simple_request():


    url = "http://httpbin.org/json"  # 测试用的API
    response = requests.get(url)
    
    print("状态码:", response.status_code)
    print("响应头:", response.headers)
    print("响应内容:")
    print(response.text)
    
    return response


# 2. 访问真实网页
def visit_webpage():
    # 选择一个简单的网站
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': 'semester.id=487; JSESSIONID=C17FB4CF71685E0CAD03DDDA786ABF49; Hm_lvt_2358de8fcde33676f65b406ffd4460cc=1748608783; SERVERNAME=c1; iPlanetDirectoryPro=PLneo6NETae29mSdTfhjjT',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'https://jwfw.fudan.edu.cn/'
    }
    url = "https://jwfw.fudan.edu.cn/eams/home.action"
    #semester.id=487; JSESSIONID=C17FB4CF71685E0CAD03DDDA786ABF49; Hm_lvt_2358de8fcde33676f65b406ffd4460cc=1748608783; SERVERNAME=c1; iPlanetDirectoryPro=PLneo6NETae29mSdTfhjjT
    response = requests.get(url, headers = headers)
    
    if response.status_code == 200:
        print("成功获取页面!")
        print("=" * 50)
        print(response.text)
        
    else:
        print(f"请求失败，状态码: {response.status_code}")

if __name__ == "__main__":
    print("=== 基础请求测试 ===")
    simple_request()
    
    print("\n=== 网页内容获取 ===")
    visit_webpage()