import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def Canny(image):
    gray = cv.cvtColor(lane_image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cany = cv.Canny(blur, 50, 150)
    return cany
img=cv.imread("/home/suman/PycharmProjects/suman/test.jpg")
lane_image=np.copy(img)
cany= Canny(lane_image)
plt.imshow(cany)
plt.show()
cv.waitKey(0)
cv.destroyWindow()