import cv2 as cv
from scan import scanner

#TODO: ADJUST LIMITS
BOTTLE_LIMIT = 3000
CAN_LIMIT = 9000

cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    display = hsv.copy()
    res = scanner(hsv)
    soda_name = max(res, key = res.get)
    if(res[soda_name] > CAN_LIMIT):
        soda_type = soda_name + " can"
    elif(res[soda_name] > BOTTLE_LIMIT): 
        soda_type = soda_name + " bottle"
    else:
        soda_type = "Unknown"

    cv.putText(display, soda_type, (0, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, 
                (0, 255, 0), 2)
    cv.putText(display, "Area: " + str(res[soda_name]), (0, 40), cv.FONT_HERSHEY_COMPLEX, 0.5, 
                (0, 255, 0), 2)
    cv.imshow('Display', display)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()