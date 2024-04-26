##### Erosion of an image, corners are trimmed in erosion

import cv2
import numpy as np
  
img = cv2.imread("pika.png",1)
cv2.imshow("Original Image", img) 
  

#kernel/filter is used for erosion as an input
#uint8 - unsigned integer of 8 bit
kernel = np.ones((5, 5), np.uint8)
print(kernel)

image = cv2.erode(img, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()



