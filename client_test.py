import requests

url = 'http://127.0.0.1:3000/'
# my_img = {'image': open('1.png', 'rb')}
my_img = {'image': open('banhmi.jpg', 'rb')}

r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())