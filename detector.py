"""
Module that saves an image temporarily in the temp folder to be used for 
AWS Rekognition. Specifically finds if the object is a bottle or can
"""

import cv2 as cv
from os import remove
import boto3
import uuid

CLIENT = boto3.client('rekognition')
# Tin included due to inconsistecy of identification. Tin is used to 
# identify the obj as a can in addition to the label 'Can'
RELEVANT_LABELS = ['Tin', 'Can', 'Bottle']
PHOTO_LOCATION = './temp/{}.jpg'

"""
photo: photo taken by webcam to be saved into temp filder

Saves passed photo with a unique ID and returns its name
"""
def save(photo):
    img_name = PHOTO_LOCATION.format(str(uuid.uuid4()))
    cv.imwrite(img_name, photo)
    return img_name

"""
saved_photo: saved photo's file path (taken from temp)

Takes in a saved photo from temp and passes it to rekognition in order to
find labels. Relevant labels are kept in order to classify bottle, can, 
or undetermined and label with the most confidence is kept.
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
        # 0 index used since detect_labels() sorts label from highest
        # confidence to lowest
        return res['Labels'][0]['Name']