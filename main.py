"""
Main file that takes an image from the webcam and analyzes its color 
(brand) using scan.py and type with detector.py. Returns the name of 
the soda bottle or can.
"""

import cv2 as cv
from scan import scanner
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
if __name__ == "__main__":
    frame = takeImage()
    saved_frame = detector.save(frame)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    areas = scanner(hsv)
    soda_name = max(areas, key = areas.get)
    container_type = detector.detect_type(saved_frame)
    obj = soda_name + ' ' + container_type
    print(obj)
    cv.destroyAllWindows()