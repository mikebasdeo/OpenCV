import cv2
import numpy as np
import matplotlib.pyplot as plt



# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

img = cv2.imread('mri.jpg', cv2.IMREAD_GRAYSCALE)

print('test')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
