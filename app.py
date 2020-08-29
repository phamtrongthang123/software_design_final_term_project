# helper
import torch.nn.functional as F
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
from PIL import Image
from io import BytesIO
import base64
from models import * 
from FlaskModel import FlaskModel

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
flaskModel = FlaskModel()  

@app.route('/')
def hello_world():
    return 'Hello bạn hiền!'


import json
@app.route('/', methods=['POST'])
def results():
    
    if request.method == 'POST':
        # convert bytes to dict if not python (send file instead data)
        cur_lang = 'python'
        try: 
            dict_str = request.data.decode("UTF-8")
            request.data = json.loads(dict_str)
            cur_lang = request.data['lang']
        except:
            pass            

        # each type of lang has difference way to read img, cpp case is decode base64, python send file in request instead data as cpp
        # but current i dont know how to wrap lang into data field.
        if cur_lang == 'python':
            img_file = request.files['image']
            img = Image.open(img_file.stream)
        elif cur_lang == 'cpp':
            img = Image.open(BytesIO(base64.b64decode(request.data['img_encoded'])))
        else: 
            img = Image.open(BytesIO(base64.b64decode(request.data['img_encoded'])))
        
        img = img.convert("RGB")        
        
                     
        model_result = flaskModel.predict(img)
        return jsonify(model_result)

# app.run("localhost", "3000", debug=True)
app.run("0.0.0.0", "3000", debug=True)