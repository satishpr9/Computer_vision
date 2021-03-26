import cv2
import numpy as np

frameWidth=300
frameHeight=300
cap=cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4,frameHeight)

def WebCam_Images(imgArray,scale,labels=[]):
    sizeW=imgArray[0][0].shape[1]
    sizeH=imgArray[0][0].shape[0]

    rows=len(imgArray)
    cols=len(imgArray[0])
    rowsAvailable=isinstance(imgArray[0],list)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(0,rows):
            for y in range(0,cols):
                imgArray[x][y]=cv2.resize(imgArray[x][y],(sizeW,sizeH),None, scale, scale)
                if len(imgArray[x][y].shape)==2:
                    imgArray[x][y]=cv2.cvtColor(imgArray[x][y],cv2.COLOR_GRAY2BGR)
        imageBlank=np.zeros((height,width,3), np.uint8)
        hor=[imageBlank]*rows
        hor_con=[imageBlank]*rows
        for x in range(0,rows):
            hor[x]=np.hstack(imgArray[x])
            hor_con[x]=np.concatenate(imgArray[x])
        ver=np.vstack(hor)
        ver_con=np.concatenate(hor)
    else:
        for x in range(0,rows):
            imgArray[x]=cv2.resize(imgArray[x],(sizeW,sizeH),None,scale,scale)
            if len(imgArray[x].shape)==2:
                imgArray[x]=cv2.cvtColor(imgArray[x],cv2.COLOR_GRAY2BGR)
        hor=np.hstack(imgArray)
        hor_con=np.concatenate(imgArray)
        ver=hor
    if len(labels)!=0:
        ImgWidth=int(ver.shape[1]/cols)
        ImgHeight=int(ver.shape[0]/rows)
        print(eachImgHeight)
        for d in range(0,rows):
            for c in range(0,cols):
                cv2.rectangle(ver,(c*ImgWidth,ImgHeight*d),(c*ImgWidth+len(tables[d][c])*13+27,30+ImgHeight*d),(255,255,255),cv2.FILLED)
    return ver


while True:
    success, img=cap.read()
    kernel=np.ones((5,5),np.uint8)
    print(kernel)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny=cv2.Canny(imgBlur,100,200)
    imgDilation=cv2.dilate(imgCanny,kernel, iterations=2)
    imgEroded=cv2.erode(imgDilation,kernel,iterations=2)
    StackedImages=WebCam_Images(([img,imgGray,imgBlur],
    [imgCanny,imgDilation,imgEroded]),0.6)

    cv2.imshow("Stacked Images",StackedImages)
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break