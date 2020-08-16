import cv2
import numpy as np


img = cv2.imread("opencv_sample.png")
img_gray = cv2.imread("opencv_sample.png", 0)

#factor = 500//img.shape[0]
#img_resize = cv2.resize(img, (img.shape[0]*factor,img.shape[1]*factor))
red_channel = img[:,:,2]
blue_channel = img[:,:,0]
green_channel = img[:,:,1]
#cv2.imshow("red_channel", red_channel)
#cv2.imshow("blue_channel", blue_channel)
#cv2.imshow("green_channel", green_channel)
#gray_wrong = (red_channel+green_channel+blue_channel)//3
gray_wrong = red_channel//3 +green_channel//3 +blue_channel//3
gray_cal = ((0.3*red_channel) + (0.59*green_channel) + (0.11*blue_channel)).astype("uint8")
gray_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_draw = img.copy()
cv2.rectangle(img_draw, (100,200), (200,300), (100,10,255), -1)
cv2.circle(img_draw, (300,300), 100, (0,255,100), -1)
cv2.line(img_draw, (100,200), (300,300), (255,0,0))
cv2.arrowedLine(img_draw, (100,200), (50,50), (0,0,255), 10, 5)
cv2.putText(img_draw, "OpenCV Class", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.putText(img_draw, "OpenCV Class", (200,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2)

edge = cv2.Canny(img, 0, 255)
def change_thres(val):   #simple thresholding
    thres = cv2.getTrackbarPos('Threshold:', "thres")
    bw = np.where(img_gray>thres,255, 0).astype('uint8')
    cv2.imshow("thres", bw)

def change_edge(val):
    minv = cv2.getTrackbarPos('min thres:', "edge")
    maxv = cv2.getTrackbarPos('max thres:', "edge")
    edge = cv2.Canny(img, minv, maxv)
    cv2.imshow("edge", edge)

#bw = np.where(img_gray>150,255, 0).astype('uint8')
ret, bw = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
a_thres_5 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
a_thres_20 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
a_thres_50 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 501, 5)

cv2.imshow("img", img)

#cv2.imshow("img_draw", img_draw)
#cv2.imshow("edge", edge)
cv2.imshow("thres", bw)
cv2.imshow("a_thres_5", a_thres_5)
cv2.imshow("a_thres_20", a_thres_20)
cv2.imshow("a_thres_50", a_thres_50)
cv2.createTrackbar('min thres:', "edge", 0, 255, change_edge)
cv2.createTrackbar('max thres:', "edge", 255, 255, change_edge)
cv2.waitKey(0)




























# End
