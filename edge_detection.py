import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Drone footage/Parking Spot Images/Good Images/quality.jpg',0)
edges = cv.Canny(img,100,200)


lines = cv.HoughLines(edges,1,np.pi/180,20)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv.line(edges,(x1,y1),(x2,y2),(0,0,255),2)

# cv.imwrite('Drone footage/Parking Spot Images/Good Images/houghlines3.jpg',edges)

kernel = np.ones((5,5), np.uint8)
img_dilation = cv.dilate(edges, kernel, iterations=1)
img_erosion = cv.erode(img_dilation, kernel, iterations=1)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_erosion,cmap = 'gray')
plt.title('Erode Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_dilation,cmap = 'gray')
# plt.title('Dilate Image'), plt.xticks([]), plt.yticks([])
plt.show()