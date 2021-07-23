import cv2 as cv
from os import remove
import boto3
import uuid

CLIENT = boto3.client('rekognition')
RELEVANT_LABELS = ['Tin', 'Can', 'Bottle']
PHOTO_LOCATION = './temp/{}.jpg'

"""

"""
def save(photo):
    img_name = PHOTO_LOCATION.format(str(uuid.uuid4()))
    cv.imwrite(img_name, photo)
    return img_name

"""

"""
def detect_type(saved_photo):
    type = ''
    with open(saved_photo, 'rb') as image:
        res = CLIENT.detect_labels(Image={'Bytes': image.read()})
    try:
        remove(saved_photo)
    except: 
        pass
    for label in list(res['Labels']):
        if label['Name'] not in RELEVANT_LABELS:
            res['Labels'].remove(label)
    if len(res['Labels']) == 0:
        return 'Unknown'
    else:
        return res['Labels'][0]['Name']