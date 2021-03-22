import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def Canny(image):
    gray = cv.cvtColor(lane_image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cany = cv.Canny(blur, 50, 150)
    return cany
def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
    return line_image
def region_interest(image):
    height=image.shape[0]
    polygons=np.array([[(200,height),(1100,height),(500,250)]])
    mask=np.zeros_like(image)
    cv.fillPoly(mask,polygons,255)
    masked_image=cv.bitwise_and(image,mask)
    return masked_image
img=cv.imread("/home/suman/PycharmProjects/suman/test.jpg")
lane_image=np.copy(img)
cany= Canny(lane_image)
# cv.namedWindow('cany', cv.WINDOW_NORMAL)
# cv.resizeWindow('cany',1000,800)
# cv.imshow('cany',cany)
theline=region_interest(cany)

lines=cv.HoughLinesP(theline,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(lane_image,lines)
combo=cv.addWeighted(lane_image,0.8,line_image,1,1)
cv.imshow('Result',combo)
# plt.imshow(cany)
#
# plt.show()
cv.waitKey(0)
cv.destroyWindow()