import cv2 
import uuid

def takeSingleImage():     
    # Capturing video
    webcam = cv2.VideoCapture(0) 

    # reading frames
    ret, frame = webcam.read()

    # Checking if frame captured or not
    print (ret)

    # releasing the webcam
    webcam.release()

    # displaying image
    cv2.imshow("my image", frame)

    # stopping the output
    cv2.waitKey(1000) #ms to display window, before it is automatically closed

    # releasing all windows

    cv2.destroyAllWindows()
    
    return frame

