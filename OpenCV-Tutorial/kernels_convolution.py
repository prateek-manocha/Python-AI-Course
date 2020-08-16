import cv2
import numpy as np
from skimage.exposure import rescale_intensity

img = cv2.imread("opencv_sample.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Filters
horizontal = np.array([
[1,1,1],
[0,0,0],
[-1,-1,-1]
])
vertical = np.array([
[-1,0,1],
[-1,0,1],
[-1,0,1]
])
blur_3 = (1/9)*np.array([
[1,1,1],
[1,1,1],
[1,1,1]
])
blur_9 = (1/81)*np.ones((9,9))
laplacian = np.array(
[[0,1,0],
[1,-4,1],
[0,1,0]]
)
sharpen = np.array([
[0,-1,0],
[-1,4,-1],
[0,-1,0]
])
identity = np.array([
[0,0,0],
[0,1,0],
[0,0,0]
])

def convolve(img, kernel):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Initialise the variables
    (ih, iw) = gray.shape
    (kh, kw) = kernel.shape
    output = np.zeros(gray.shape)

    # pad the input image
    pad = int((kh-1)/2)
    # image = cv2.copyMakeBorder(image, top_pad, bottom_pad, left_pad, right_pad, pad_type)
    gray = cv2.copyMakeBorder(gray, pad, pad, pad, pad, cv2.BORDER_REPLICATE)

    # convolution
    for y in range(pad, ih+pad):
        for x in range(pad, iw+pad):
            roi = gray[y-pad:y+pad+1, x-pad:x+pad+1]
            dum = (roi*kernel).sum()
            output[y-pad, x-pad] = dum

    output = rescale_intensity(output, in_range=(0, 255))
    output = (output*255).astype("uint8")
    return output


cv2.imshow("orig", gray)
#horizontal = convolve(img, horizontal)
#vertical = convolve(img, vertical)
#blur = convolve(img, blur)
horizontal = cv2.filter2D(gray, -1, horizontal)
vertical = cv2.filter2D(gray, -1, vertical)
blur_9 = cv2.filter2D(gray, -1, blur_9)
laplacian = cv2.filter2D(gray, -1, laplacian)
sharpen = cv2.filter2D(gray, -1, sharpen)
identity = cv2.filter2D(gray, -1, identity)
cv2.imshow("horizontal", horizontal)
cv2.imshow("vertical", vertical)
cv2.imshow("blur", blur_9)
cv2.imshow("laplacian", laplacian)
cv2.imshow("sharpen", sharpen)
cv2.imshow("identity", identity)
cv2.waitKey(0)























# End
