import requests
from bs4 import BeautifulSoup
import re

def fetch_and_extract_info():
    url = "https://69yun69.com/user"
    headers = {
        "Cookie": ""
    }

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return None

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有 script 标签
    script_tags = soup.find_all('script')

    # 提取 ChatraIntegration 的 script 内容
    chatra_script = None
    for script in script_tags:
        if 'window.ChatraIntegration' in str(script):
            chatra_script = script.string
            break

    if not chatra_script:
        print("未找到 ChatraIntegration 脚本信息")
        return None

    # 使用正则表达式提取需要的信息
    # 提取用户名、邮箱、到期时间和剩余流量
    user_info = {}
    user_info['到期时间'] = re.search(r"'Class_Expire': '(.*?)'", chatra_script).group(1) if re.search(r"'Class_Expire': '(.*?)'", chatra_script) else None
    user_info['剩余流量'] = re.search(r"'Unused_Traffic': '(.*?)'", chatra_script).group(1) if re.search(r"'Unused_Traffic': '(.*?)'", chatra_script) else None

    # 输出用户信息
    print(f"到期时间: {user_info['到期时间']}")
    print(f"剩余流量: {user_info['剩余流量']}")

    # 提取 Clash 订阅链接
    clash_link = None
    for script in script_tags:
        if 'index.oneclickImport' in str(script) and 'clash' in str(script):
            link = re.search(r"'https://checkhere.top/link/(.*?)\?sub=1'", str(script))
            if link:
                print(f"Clash 订阅链接: https://checkhere.top/link/{link.group(1)}?clash=1")
                print(f"v2ray 订阅链接: https://checkhere.top/link/{link.group(1)}?sub=3")
                break

# 调用函数
fetch_and_extract_info()
