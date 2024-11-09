from bs4 import BeautifulSoup

buf = '<span class="title">肖申克的救赎</span>'

soup = BeautifulSoup(buf, 'lxml')
print(soup.span.string)


