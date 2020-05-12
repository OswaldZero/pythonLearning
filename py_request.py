#与其相同的还有urllib/urllib2/selenium
import requests
url="http://www.baidu.com"
response=requests.get(url)
response.encoding="utf-8"#解决乱码问题
print(response.text)
#获取其他属性
print(type(response.request.headers,response.request.headers))#获取请求头
print(type(response.headers),response.headers)#获取响应头
print(type(response.cookies),response.cookies)#获取响应cookies
print(type(response.url),response.url)#获取响应url
print(type(response.request.url),response.request.#获取请求url
