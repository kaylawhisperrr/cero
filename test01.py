import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Cookie': 'abRequestId=42a71580-9070-5fbb-aedc-c948234e8db2; a1=199e21ce1e71zryp7f0v79jyhj7wpwn2333duf8li50000121671; webId=802789da2c29ace9c6ee1046752f7cd8; gid=yjjdJyf8K2q2yjjdJySdyqiYdWyuFvUWi8hWq13jVvxVWf28EUEIJ7888yJyKWy8qj4fqq24; acw_tc=0a00d7a117605295358082190e0d05090c0e63813ca1b7212ce263f51087b5; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; sec_poison_id=eedb1f1a-04d6-44f3-afd8-c12dfe89b614; webBuild=4.82.0; xsecappid=xhs-pc-web; web_session=040069b0deb046584624c5c4da3a4b1950f2ed; unread={%22ub%22:%2268de18190000000004021e9d%22%2C%22ue%22:%2268ee35440000000007030e80%22%2C%22uc%22:22}; loadts=1760529603763',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
}

url = "https://www.xiaohongshu.com/user/profile/60cd5c7c0000000001001182?xsec_token=AB-flV8tnjpVCnqq4VKacszyhqkV_04iPXQiaK6xK2PqA=&xsec_source=pc_feed"

response = requests.get(url, headers=headers)

print("状态码:", response.status_code)
print("响应长度:", len(response.text))

# 保存完整响应到文件
with open('my_info.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("完整响应已保存到 my_info.html")