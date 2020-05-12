#get方法
import requests
url="https://www.baidu.com"
response=requests.get(url)
print(response)
#post方法
data={
    'from':'zh',
    'to':'en',
    'query':'人生苦短,我用python'
}
response2=requests.post(url,data=data)
print(response2)
