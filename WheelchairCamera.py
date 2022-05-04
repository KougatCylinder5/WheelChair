import cv2
import time
import numpy
import pyautogui as GUI


vid = cv2.VideoCapture(0)
if(not vid.isOpened()):
    print("Camera Failed to Load... Exiting")
    time.sleep(2) # 
    exit() # exit program
width, height = GUI.size()
UI = numpy.zeros((height,width,3), numpy.uint8)
#UI[round(width/3):round((width/3)*2),round(height/3):round((height/3)*2)] = [0,0,255]
leftArrow = numpy.array([[width/9,height/1.5],[width/ 20, height/2],[width/9,height/3],[width/ 20, height/2],[width/ 4, height/2]],numpy.int32) 
# co-ordinates for the arrow
leftArrow = leftArrow.reshape((-1, 1, 2)) # reshapes the arrow co-ordinates so that ploylines can accept it

rightArrow = numpy.array([[width/1.12,height/1.5],[width/ 1.05, height/2],[width/1.12,height/3],[width/ 1.05, height/2],[width/ 1.35, height/2]],numpy.int32) 
rightArrow = rightArrow.reshape((-1, 1, 2)) # reshapes the arrow co-ordinates so that ploylines can accept it
# co-ordinates for the arrow

UI[0:height,0:round(width/3)] = [50,50,50]
UI[0:height,round(width/3) * 2:width] = [50,50,50]
cv2.polylines(UI,[leftArrow],False,(0,0,255),10)
cv2.polylines(UI,[rightArrow],False,(0,255,0),10)

cv2.namedWindow('Video') # create window for video
cv2.namedWindow('Wheelchair Controller',cv2.WINDOW_FULLSCREEN)
while True:
    cv2.imshow('Wheelchair Controller', UI)
    cv2.moveWindow('Wheelchair Controller',-20,0)
    ret, frame = vid.read() # read the camera
    frame = frame[::2,::2] # reduce the size of the camera by a power of two
    frame = numpy.array(frame, dtype = 'uint8') # reformat the array after the slicing
    HSV = cv2.cvtColor(frame.copy(),cv2.COLOR_BGR2HSV) # convert a copy of the camera image to HSV using frame.copy()
    point = cv2.inRange(HSV,(110,120,90),(120,250,180)) # search for colors in-range of the zone
    center = cv2.moments(point) # find the white pixels labeled from cv2.inRange()
    try: # catch to prevent divid/0 errors
        x = int(center['m10']/center['m00']) # find the center x 
        y = int(center['m01']/center['m00']) # fidn the center y
        cv2.circle(frame,(x,y),10,(255,255,255),-1) # put a circle on the spot (removed later)
        x0 = (x - len(frame[0])/2) * 0.5 # split the found point in half, so that it becomes negative on the left and positive on the right
        y0 = (y - len(frame)/2) * 0.5 # same as above
        if(abs(x0) > 15 or abs(y0) > 15):
            GUI.moveRel(-x0,y0) # move the mouse by the (x0,y0)
    except:
        pass # pass the exception so that it doesn't error
    cv2.imshow('Video',frame) # show the frame
    if(cv2.waitKey(1) == ord('`')): # exit key
        cv2.destroyAllWindows() # clean up
        break # 