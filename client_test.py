import requests
import base64
url = 'http://127.0.0.1:3000/'
# url = "http://c1acefa7189a.ngrok.io/" # colab

with open("banhxeo.jpg", 'rb') as fimg: 
    encoded_string = base64.b64encode(fimg.read())
    base64_string = encoded_string.decode('utf-8')

# my_img = {'image': open('1.png', 'rb')}
# my_img = {'image': open('banhmi.jpg', 'rb')}
# type dectection hoặc classify
mydata = {'img_encoded': 'base64_string', 'lang': 'custom', 'type': 'classify'}
r = requests.post(url, json=mydata)
# r = r.json()
# convert server response into JSON format.
# print(r)
with open("tmp.res", "w") as f:
    f.write(r['predicted'])