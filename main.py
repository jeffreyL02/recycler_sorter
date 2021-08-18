"""
Main file that takes an image from the webcam and analyzes its color 
(brand) using scan.py and type with detector.py. Returns the name of 
the soda bottle or can.
"""

import serial
from identify import identifyObject

RESTART_KEY = "RESTART"
DETECTION_KEY = "DETECT"

"""
Takes and saves an image. Image scanned for colors to determine the 
brand. Saved image passed into rekognition to detect can or bottle. Finds
the name of the obj in image (e.g. sprite can, coke bottle, etc.)
"""
if __name__ == "__main__":
    print("Rect")
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    executing = False
    key = ""
    while not executing: 
        if ser.in_waiting > 0:
            key = ser.readline().decode('utf-8').rstrip()
        if key == "1": 
            executing = True
    
    while executing:
        """
        process:

        from pi to arduino send 19

        1. arduino waits for button to be pressed to start

        1. barrier released for obj and closes right after

        from arduino to pi send 27

        2. run obj detection on obj and send name to arduino

        from pi to arduino send 35

        3. release Release for obj and closes right after while corresopnding flap flips for a period of time and flip it back
        
        
        4. repeat  
        """
        """ Identify Object """
        key = ""
        while(True):
            if ser.in_waiting > 0:
                key = ser.readline().decode('utf-8').rstrip()
            if key == DETECTION_KEY:
                obj = identifyObject()
                break
        print(obj)
        ser.write(bytes(obj, 'utf-8')) 
        
       
                
        