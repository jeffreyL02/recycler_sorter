import cv2 as cv
from scan import scan_brand
import detector

"""
Take a single image from the webcam and return it
"""
def takeImage():     
    webcam = cv.VideoCapture(0) 
    _, image = webcam.read()
    webcam.release()
    cv.destroyAllWindows()
    return image
    
"""
Takes and saves an image. Image scanned for colors to determine the 
brand. Saved image passed into rekognition to detect can or bottle. Finds
the name of the obj in image (e.g. sprite can, coke bottle, etc.)
"""
def identifyObject():
    frame = takeImage()
    saved_frame = detector.save(frame)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    brand_similarities = scan_brand(hsv)
    soda_name = max(brand_similarities, key = brand_similarities.get)
    container_type = detector.detect_type(saved_frame)
    obj = '' # Name to fully identify obj in picture taken
    if container_type == 'Tin':
        container_type = 'Can'
    if container_type == 'Unknown':
        obj = container_type + '\n'
    else:
        obj = soda_name + " " + container_type + '\n'
    cv.destroyAllWindows()
    return obj