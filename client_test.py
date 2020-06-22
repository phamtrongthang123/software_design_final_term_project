import requests

url = 'http://0.0.0.0:3000/cifar_classifier'
# my_img = {'image': open('1.png', 'rb')}
my_img = {'image': open('leuleu.jpg', 'rb')}

r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())