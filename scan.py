import cv2 as cv
import numpy as np

#TODO: ADD SUPPORT FOR FANTA
SODA_COLOR_RANGES = np.array([
                            [[[0,100,20], [10,255,255]]],
                            [[[25, 52, 72], [102, 255, 255]]],
                            [[[29, 46, 41],[38, 100, 100]]]
                        ])
SODA_NAMES = ['Coke', 'Sprite', 'Fanta']
MIN_CAP_AREA = 500

def filter(img, colors):
    full_mask = 0
    #loop through the array of colors (2D)
    for color in colors:
        full_mask += cv.inRange(img, color[0], color[1]) #inRange(src, lower, uppper)
    res = cv.bitwise_and(img, img, mask = full_mask)
    return res

# take in filtered image
# draw contours
# return data
def trace(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    total_area = 0
    for contour in contours:
        area = cv.contourArea(contour)
        if area > MIN_CAP_AREA:
            total_area += area
    return total_area


# filter the image and collect the data
# return the data of the brand (color) with the largest area
def scanner(frame):
    #list of brand name has to be coordinated with allColors
    img_areas = {}
    for i in range(len(SODA_NAMES)):
        img_filtered = filter(frame, SODA_COLOR_RANGES[i])
        img_areas[SODA_NAMES[i]] = trace(img_filtered)
    return img_areas