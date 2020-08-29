import torch.nn.functional as F
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
import io
import os
from PIL import Image
import cv2
import numpy as np
from base64 import b64decode, b64encode
from .utils import *
from .darknet import Darknet
import cv2 
import matplotlib.pyplot as plt
import uuid 
import base64

class Net():
    def __init__(self):
        cfg_file_vn = './models/vietfood_yolo/cfg/yolov3-5c-5000-max-steps.cfg'
        weight_file_vn = './models/vietfood_yolo/weights/yolov3-5c-5000-max-steps_last.weights'
        namesfile_vn = './models/vietfood_yolo/data/obj.names'

        m_vn = Darknet(cfg_file_vn)
        m_vn.load_weights(weight_file_vn)
        self.class_names_vn = load_class_names(namesfile_vn)

        self.m_vn = m_vn
        
    def load_dict(self,path_dict): 
        self.net.load_state_dict(torch.load(path_dict,map_location=torch.device('cpu')))
        

    def inferenceVNFood(self, original_image):
        resized_image= cv2.resize(original_image, (self.m_vn.width, self.m_vn.height),interpolation=cv2.INTER_AREA)
        nms_thresh = 0.4
        iou_thresh = 0.6
        boxes = detect_objects(self.m_vn, resized_image, iou_thresh, nms_thresh)
        url = plot_boxes(original_image, boxes, self.class_names_vn, plot_labels = True)
        objects = print_objects(boxes, self.class_names_vn)
        plt.imshow(original_image)
        name = os.path.join('./imgs/', 'result.png')
        im = plt.savefig(name)
        return name

    def predict(self,img):
        name_res = self.inferenceVNFood(np.array(img))
        with open(name_res, 'rb') as fimg: 
            encoded_string = base64.b64encode(fimg.read())
            base64_string = encoded_string.decode('utf-8')
        model_result = {'type': 'detection', 'size': [img.width, img.height], "predicted": base64_string}        
        return model_result