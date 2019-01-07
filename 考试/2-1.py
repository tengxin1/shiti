import urllib.request

response = urllib.request.urlopen('https://www.zcool.com.cn/work/ZMzI2MTMwNDQ=.html')
print(response)
print(response.code)
html_content = response.read()
print(html_content)
print(html_content.decode(encoding='utf-8'))