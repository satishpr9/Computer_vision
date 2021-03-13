import cv2

#read image
img = cv2.imread("/home/satish/Pictures/Elon_Musk_2015.jpg",1)

#show the image 

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )  
scale=20
print("Origin Dimension:", img.shape)

width=int(img.shape[1]*scale/100)
height=int(img.shape[0]*scale/100)
dim=(width,height)

resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# print("Resized Dimension:", resized)

cv2.imshow('image',resized) 

angel90=90

center=(width/2,height/2)
scle=1.0
M=cv2.getRotationMatrix2D(center,angel90,scle)
angel90=cv2.warpAffine(resized,M,(height,width))

cv2.imshow("Rotate90=",angel90)

angle180=180

M=cv2.getRotationMatrix2D(center,angle180,scle)
angle180=cv2.warpAffine(resized,M,(height,width))

cv2.imshow("Rotate180:",angle180)


angle270=270
M=cv2.getRotationMatrix2D(center,angle270,scle)
angle270=cv2.warpAffine(resized,M,(height,width))

cv2.circle(resized,(80,80),55,(0,255,0),-1)
cv2.imshow("Color Image:",resized)
cv2.imshow("Rotate270:",angle270)


cv2.waitKey(0)

#save the image 
# elon=cv2.imwrite("/home/satish/Elon_Musk.jpg",img)

# elon=img[100,100]



# height, width, number of channels in image  
# height = img.shape[0]  
# width = img.shape[1]  
# channels = img.shape[2]  
# size1 = img.size  
  

# print('Image Height       : ',height)  
# print('Image Width        : ',width)  
# print('Number of Channels : ',channels)  
# print('Image Size  :', size1) 

# print("Save The File ",elon)


