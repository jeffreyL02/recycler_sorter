import cv2 as cv
from scan import scanner
from time import sleep
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