import cv2 as cv
img=cv.imread("img1.jpg")
img=cv.resize(img, (0,0),fx=0.5,fy=0.5)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
