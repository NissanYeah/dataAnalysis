import requests
r = requests.get('http://www.douban.com')
print(r.text)
print(r.content)