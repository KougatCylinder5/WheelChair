import cv2
import time

vid = cv2.VideoCapture(0)
if(not vid.isOpened()):
    print("Camera Failed to Load... Exiting")
    time.sleep(2)
    exit()
cv2.namedWindow('Video')
while True:
    ret, frame = vid.read()
    cv2.imshow('Video',frame);
    if(cv2.waitKey(1) == ord('`')):
        cv2.destroyAllWindows()
        break
        