import torch.nn.functional as F
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

class Net():
    def __init__(self):
        net = torchvision.models.mobilenet_v2()
        net.classifier = nn.Sequential(nn.Dropout(p=0.2, inplace=False), 
                                            nn.Linear(in_features=1280, out_features=500, bias=True),
                                            nn.Linear(in_features=500, out_features=100, bias=True),
                                            nn.Linear(in_features=100, out_features=5, bias=True))
        self.net = net
        
    def load_dict(self,path_dict): 
        self.net.load_state_dict(torch.load(path_dict,map_location=torch.device('cpu')))
        
    def set_eval(self):
        self.net.eval()

    def forward(self, x):        
        return self.net(x)

    def predict(self,img):
        transform = transforms.Compose([
                    transforms.Resize((224,224)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
        transform_img = transform(img)
        outputs = self.forward(transform_img[None])
        score,predicted = torch.max(F.softmax(outputs, dim=1), 1)
        classes = ("BanhXeo", "banhmi", "banhtrangtron", "goicuon", "pho")
        model_result = {'type':'classify', 'size': [img.width, img.height], "predicted": classes[predicted], "score": score.item()}        
        return model_result