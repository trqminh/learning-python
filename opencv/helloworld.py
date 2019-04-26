import cv2
import numpy as np

img = cv2.imread('blackhole.jpg')

#
# cv2.line(img, (0, 0), (1500, 1500), (255, 255, 255))
# cv2.rectangle(img, (15,15), (4000, 4000), (255, 255, 255), 5)

#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not
# find this necessary, but you may:
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img, [pts], True, (0,255,255), 3)

print(type(img))
print(img.shape[0], img.shape[1], img.shape[2])
print(img[2,3][1], img[2,3,:])

img_gray = np.copy(img)

h = img_gray.shape[0]
w = img_gray.shape[1]

for i in range(h):
  for j in range(w):
    img_gray[i,j,:] = 3 * [np.sum(img_gray[i,j], axis=0) // 3]



cv2.imshow('image',img)
cv2.imshow('grayscale image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



