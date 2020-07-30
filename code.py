import cv2
import numpy as np
import turtle as tt
tt.setworldcoordinates(0,-500,500,0)
xx=0
yy=0
def nothing(x):
    pass
cam=cv2.VideoCapture(0)
cv2.namedWindow("track")
cv2.createTrackbar('LH','track',0,255,nothing)
cv2.createTrackbar('LS','track',0,255,nothing)
cv2.createTrackbar('LV','track',0,255,nothing)
cv2.createTrackbar('UH','track',255,255,nothing)
cv2.createTrackbar('US','track',255,255,nothing)
cv2.createTrackbar('UV','track',255,255,nothing)
while True:
    _,frame=cam.read()
    frame=cv2.resize(frame,(500,500))
    frame = cv2.flip(frame, 1)
    frame1=cv2.imread('l1.png')
    frame1=cv2.resize(frame1,(500,500))
    frame1 = cv2.flip(frame1, 1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('LH','track')
    ls=cv2.getTrackbarPos('LS','track')
    lv=cv2.getTrackbarPos('LV','track')
    uh=cv2.getTrackbarPos('UH','track')
    us=cv2.getTrackbarPos('US','track')
    uv=cv2.getTrackbarPos('UV','track')
    lb=np.array([114,144,lv])
    ub=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,lb,ub)
    indices = np.where(mask == [255])
    ##print (indices)
    leng=(len(indices[0]))
    #print(leng)
    
    if((abs(xx-indices[1][int(leng/2)])>=0) and (abs(yy-indices[0][int(leng/2)])>=0)):
           
        indices[0][int(leng/2)]=(np.ceil(indices[0][int(leng/2)]/20))*20
        indices[1][int(leng/2)]=(np.ceil(indices[1][int(leng/2)]/50))*50
        coordinates = (indices[0][int(leng/2)], indices[1][int(leng/2)])
        print (coordinates)
        tt.goto(indices[1][int(leng/2)], -indices[0][int(leng/2)])
    mask1=cv2.bitwise_not(mask)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    res1=cv2.bitwise_and(frame1,frame1,mask=mask1)
    result=cv2.bitwise_or(res,res1)
   # cv2.imshow('1',frame)
    cv2.imshow('2',frame)
    cv2.imshow('3',res)

    xx=indices[1][int(leng/2)]
    yy=indices[0][int(leng/2)]
    key=cv2.waitKey(1)
    if key==27:
        break
    
cam.release()

cv2.destroyAllWindows()
tt.done()
