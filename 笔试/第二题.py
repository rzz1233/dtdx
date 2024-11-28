import re


def reg_search(text, regex_list):
    result = {}

    # 遍历正则表达式列表
    for key, regexes in regex_list.items():
        matched = []
        for regex in regexes:
            # 用正则表达式进行匹配
            matches = re.findall(regex, text)
            if matches:
                matched = matches
                break  # 找到一个匹配规则就跳出循环

        # 将结果保存到字典中
        if matched:
            result[key] = matched if len(matched) > 1 else matched[0]

    return result


# 测试
text = """
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债
券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
日至 2027 年 6 月 1 日止。
"""

regex_list = {
    '标的证券': [r'股票代码：([\d\.A-Z]+)', r'股票简称：([\w]+)'],
    '换股期限': [r'(\d{4} 年 \d{1,2} 月 \d{1,2})', r'(\d{4} 年 \d{1,2} 月 \d{1,2})']
}
result = reg_search(text, regex_list)
print(result)
