# Arithmetic Operation on Images
# Pixel values are directly added / subtarcted for 2 images
# make sure that the 2 images are of same size

import cv2 
import numpy as np 
     
image1 = cv2.imread('input1.png') 
image2 = cv2.imread('input2.png')
  
# 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
weightedSum = cv2.addWeighted(image1,0.5,image2,0.4, 0)
  
cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0) 
cv2.destroyAllWindows() 





