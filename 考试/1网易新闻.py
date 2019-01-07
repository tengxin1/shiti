import requests
from lxml import etree

url = 'https://news.163.com/'
resp = requests.get(url)

if resp.status_code != 200:
    raise Exception("请求失败")
html_content = resp.text

pattern1 = '//div[@class="mt35 mod_hot_rank clearfix"]/ul/li/a/text()'

tree = etree.HTML(html_content)
new1 = tree.xpath(pattern1)
for i in new1:
    print(i)