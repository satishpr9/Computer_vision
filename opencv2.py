import numpy as np
import cv2
video_path="/home/satish/Videos/VID_20210225_140522.mp4"
video_path1="/home/satish/Downloads/videoplayback1.mp4"

cap1=cv2.VideoCapture(0)
cap= cv2.VideoCapture(video_path)
cap3=cv2.VideoCapture(video_path1)
while cap.isOpened():
    #create a variable ret to assign true or false
    ret,frame=cap.read()
    ret2,frame2=cap1.read()
    ret3,frame3=cap3.read()
    if ret:
        image= cv2.resize(frame,(320,120))
        camera_frame=cv2.resize(frame2,(320,120))
        video_camera=cv2.resize(frame3,(320,120))
        #for multiple video in one window
        frame_2=np.hstack((image,camera_frame))
        frame_4=np.hstack((image,video_camera))
        frame_5=np.vstack((frame_2,frame_4))
        cv2.imshow("Video",frame_5)
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break    

cap.release()
cv2.destroyAllWindows()