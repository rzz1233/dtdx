from collections import Counter

text = "apple orange banana apple apple orange"
# words = text.split()
counter = Counter(text)
print(counter)
# 输出：Counter({'apple': 3, 'orange': 2, 'banana': 1})
