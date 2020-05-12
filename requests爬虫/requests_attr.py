import requests
url="https://www.baidu.com"
response=requests.get(url)
response.encoding='utf-8'

print(type(response.request.headers),'response.request.headers=')
print(type(response.headers),'response.headers')
print(type(response.cookies),'response.cookies')
print(type(response.url),'response.cookies')
print(type(response.request.url),'response.request.url')