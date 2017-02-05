import cv2
import numpy as np
#from time import time

#Mehtod to find the pixle position of the center of the 2 rectangles
def find_center(img):
    
    #finding the contors
    ret,thresh = cv2.threshold(img,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #Array to be filled with the center points of all the contors
    center_x = []
    center_y = []
    
    #Loop to find all the center points of the contors
    for cnt in contours:
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        center_x.append(cx)
        center_y.append(cy)
    
    #averaging the points to find a center
    avgx= (center_x[0]+center_x[1])/2
    avgy= (center_y[0]+center_y[1])/2
    return avgx, avgy

#Setting up video capture from the webcam
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    
    #cur_time = time()
    
    #getting the current frame so it can be maipulated
    a, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = np.asarray(hsv,  np.uint8)
    #adding some blurs to decrease noise and increase accuracy
#    for i in range(2):
#   	 hsv = cv2.GaussianBlur(hsv,(5,5),0)
   

    cv2.imshow('w',hsv)
    
    # Threshold the HSV image to get only white colors
    #range = 20
    #mask = cv2.inRange(hsv, np.array([65-range,50,50]), np.array([65+range,255,255]))
    mask = cv2.inRange(hsv, np.array([0,0,0]), np.array([0,0,255])
    
    #Showing the mask for testing
    cv2.imshow('1', mask)
    
    #got from hsv -> bgr ->gray
    gray = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    #Tring to find the center
    #if no rectangele, then the program doesn't crash
    try:
      	avgx, avgy = find_center(gray)
      	print avgx
        
        #put a circle on the frame
        #cv2.circles(frame, (avgx, avgy), 4, (0, 0, 2555), 2)
        print "rectangele found"
        #cv2.imshow('frame',frame)
        
    except:
        
        #print "no Rectangles found"
        pass
    cv2.imshow('s', frame)
    #Wait for the q to be presses      
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break
    #print time()-cur_time
    
#kill everything
cv2.destroyAllWindows()
   
   
