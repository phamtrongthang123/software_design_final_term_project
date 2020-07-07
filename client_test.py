import requests

url = 'http://127.0.0.1:3000/cifar_classifier'
# my_img = {'image': open('1.png', 'rb')}
my_img = {'image': open('palm.jpg', 'rb')}

r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())