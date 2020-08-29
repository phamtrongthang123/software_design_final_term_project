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

class ModelFactory():
    def __init__(self):
        self.models = {'cifar10':cifar10.model.Net(), 
                    'classify': vietfood_mobilenet.model.Net(), 
                    'detection': vietfood_yolo.model.Net()}
        self.models['cifar10'].load_state_dict(torch.load(CIFAR10_MODEL_PATH,map_location=torch.device('cpu')))
        self.models['cifar10'].eval()
        self.models['classify'].load_dict(MOBILENET_MODEL_PATH)
        self.models['classify'].set_eval()
        

    def getModelByState(self, state_name):
        return self.models[state_name]