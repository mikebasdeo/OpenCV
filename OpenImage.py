import cv2
import numpy as np
import matplotlib.pyplot as plt


# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

img = cv2.imread('mri.jpg', cv2.IMREAD_GRAYSCALE)

print('test')


# --------------- OPENING IMAGES

# open an image using matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([500,55], [55,500], 'c', linewidth=5)
# plt.show()

# open an image using OpenCV
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------- SAVING IMAGES

# save an image using OpenCV
cv2.imwrite('output.png', img)





