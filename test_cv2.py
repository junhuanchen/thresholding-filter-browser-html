import cv2
img = cv2.imread("/home/dls/dl.jpeg")
# print(dir(cv2))
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

tmp = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)

cv2.imwrite("tmp.bmp", tmp)

import numpy as np
lower_bound = np.array([(60 * 255) // 100, 0, 0])
upper_bound = np.array([255, 255, 255])

cv2.imwrite("lab.bmp", lab)

print(lab)

mask = cv2.inRange(lab, lower_bound, upper_bound)

cv2.imwrite("mask.bmp", mask)
