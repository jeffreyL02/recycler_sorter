"""
Module that helps to analyze a given frame or picture through 
thresholding with HSV values. scanner() returns the area values of the
thresholding for each given soda brand's ranges
"""

import cv2 as cv
import numpy as np

# Only works with these brands or others with very similar colors
SODA_NAMES = ['Coke', 'Sprite', 'Fanta']
# SODA_COLOR_RANGES contains HSV values of soda brands, with respect to 
# SODA_NAMES. Need to be calibrated for different light levels
SODA_COLOR_RANGES = np.array([
                            [[[0,207,38], [179,255,193]]],
                            [[[24, 0, 33], [142, 255, 255]]],
                            [[[8, 187, 121],[30, 255, 255]]]
                        ])
# Minimum value to be considered major part of object(e.g. cap, label, 
# logo)
MIN_CAP_AREA = 500

"""
img: Image to be filtered
range: List containing a range of HSV values to mask

Returns a masked image of img with the specified color range
"""
def filter(img, range):
    full_mask = 0
    for color in range:
        full_mask += cv.inRange(img, color[0], color[1])
    res = cv.bitwise_and(img, img, mask = full_mask)
    return res

"""
img: masked image of a single hsv range

Find the area of contours of masked image and returns total area if a 
valid part of the object
"""
def findArea(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    total_area = 0
    for contour in contours:
        area = cv.contourArea(contour)
        if area > MIN_CAP_AREA:
            total_area += area
    return total_area

"""
picture: picture to be scanned for each soda brand's color range

Return a dictionary of areas corresponding to each soda brand
"""
def scanner(picture):
    #list of brand name has to be coordinated with allColors
    img_areas = {}
    for i in range(len(SODA_NAMES)):
        img_filtered = filter(picture, SODA_COLOR_RANGES[i])
        img_areas[SODA_NAMES[i]] = findArea(img_filtered)
    return img_areas