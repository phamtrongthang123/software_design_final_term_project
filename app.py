# helper
import torch.nn.functional as F
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
from models import * 

def get_model(model_type):
    if model_type == "cifar10":
        net = cifar10.model.Net()
        net.load_state_dict(torch.load(CIFAR10_MODEL_PATH,map_location=torch.device('cpu')))
        return net

# main app
from flask import Flask, render_template, request,jsonify
from PIL import Image  
import PIL

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello bạn hiền!'

@app.route('/cifar_classifier', methods=['POST'])
def results():
    
    if request.method == 'POST':
        
        img_file = request.files['image']
        img = Image.open(img_file.stream)
        # if cifar 10
        img = img.convert("RGB")
        # try:
        #     img.save('./imgs/requested_img.jpg')
        # except: 
        #     try:
        #         img.save('./imgs/requested_img.png')
        #     except: 
        #         return jsonify({"msg": "It's not an img file :D"})
        
        # input preprocessing
        transform = transforms.Compose(
                        [transforms.Resize((32,32)),
                        transforms.ToTensor(),
                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        transform_img = transform(img)
        # model processing
        model = get_model("cifar10")                 
        outputs = model(transform_img[None])
        _,predicted = torch.max(outputs, 1)
        classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
        
        model_result = {'size': [img.width, img.height], "predicted": classes[predicted]}        
        return jsonify(model_result)

app.run("localhost", "3000", debug=True)