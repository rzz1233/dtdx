import re  # 引入正则表达式库，用于从 HTML 页面提取特定的内容
import requests  # 引入 requests 库，用于发送 HTTP 请求
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.64 Safari/537.36"
}

# 创建一个 session 对象，用于保存和发送后续请求，这样可以保持登录状态
session = requests.session()

# GitHub 登录页面的 URL，首先访问这个页面获取隐藏的表单字段
base_url = 'https://github.com/login'

# GitHub 提交登录表单的 URL，通过 POST 请求提交登录信息
login_url = 'https://github.com/session'

# GitHub 登录后的主页 URL，用于确认是否登录成功
main_url = 'https://github.com/'

# 发送 GET 请求获取登录页面的内容，并解码成 UTF-8 格式的字符串
base_res = session.get(url=base_url, headers=headers).content.decode('utf-8')

html = etree.HTML(base_res)
token = html.xpath('//input[@name="authenticity_token"]/@value')[0]

timestamp = html.xpath('//input[@name="timestamp"]/@value')[0]
timestamp_secret = html.xpath('//input[@name="timestamp_secret"]/@value')[0]


# # 使用正则表达式从 HTML 中提取隐藏的 `authenticity_token` 字段，它是 GitHub 防止 CSRF 攻击的重要参数
# pattern1 = r'<input type="hidden" data-csrf="true" name="authenticity_token" value="(.*?)"'
#
# # 使用正则表达式从 HTML 中提取隐藏的 `timestamp_secret` 字段，这是 GitHub 登录表单中的一个隐藏时间戳
# pattern2 = r'<input class="form-control" type="hidden" name="timestamp_secret" value="(.*?)"'
#
# # 使用正则表达式从 HTML 中提取隐藏的 `timestamp` 字段，表示表单提交时的时间戳
# pattern3 = r'<input class="form-control" type="hidden" name="timestamp" value="(.*?)"'
#
# # 提取 authenticity_token 的值
# token = re.findall(pattern1, base_res)[0]
#
# # 提取 timestamp 的值
# timestamp = re.findall(pattern3, base_res)[0]
#
# # 提取 timestamp_secret 的值
# timestamp_secret = re.findall(pattern2, base_res)[0]

# 构建登录请求的表单数据，包括用户名、密码、隐藏字段和其他参数
data = {
    'commit': 'Sign in',  # 提交按钮的值
    'authenticity_token': token,  # CSRF 防护令牌，从页面提取
    'add_account': '',  # 该字段为空，通常用于与其他账户关联登录
    "login": "2214902667@qq.com",  # 用户的 GitHub 登录邮箱
    "password": "221266ren",  # 用户的登录密码
    'webauthn-conditional': 'undefined',  # 由 GitHub 页面生成的安全字段
    'javascript-support': 'true',  # 表示浏览器支持 JavaScript
    'webauthn-support': 'supported',  # 表示浏览器支持 WebAuthn（用于身份验证）
    'webauthn-iuvpaa-support': 'supported',  # 表示浏览器支持身份验证附加协议
    'return_to': 'https://github.com/login',  # 登录成功后跳转的页面
    'allow_signup': '',  # 是否允许自动注册，这里为空
    'client_id': '',  # 客户端 ID，这里为空
    'integration': '',  # 集成字段，这里为空
    'required_field_6208': '',  # 表单中的一个隐藏字段，实际登录中未被使用
    'timestamp': timestamp,  # 提取的时间戳
    'timestamp_secret': timestamp_secret  # 提取的时间戳密钥
}

# 发送 POST 请求到登录表单提交 URL，提交用户的登录信息
session.post(url=login_url, headers=headers, data=data)

# 登录成功后，使用 session 发送 GET 请求到 GitHub 主页，检查是否登录成功
main_res = session.get(url=main_url, headers=headers).content.decode('utf-8')

# 打印主页的 HTML 内容，如果包含用户信息则表示登录成功
print(main_res)
