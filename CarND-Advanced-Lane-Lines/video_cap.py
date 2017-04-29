import numpy as np
import cv2
import PIL
from time import sleep
import os

fps = 25
delay = int(1000/fps)
i = 0

hardfolder = "C:\Car-ND-Projects\CarND-Advanced-Lane-Lines\harder_challenge\\"

dirs = os.listdir(hardfolder)

if len(dirs) ==0:
    cap = cv2.VideoCapture("C:\Car-ND-Projects\CarND-Advanced-Lane-Lines\harder_challenge_video.MP4")
    
    while(cap.isOpened() and i <2000):
        ret, frame = cap.read()
                 
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',frame)
        path = hardfolder + str(i) + ".jpg"
        if ret:
            cv2.imwrite(path,frame)
        else:
            break
        
        i += 1
                                       
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
