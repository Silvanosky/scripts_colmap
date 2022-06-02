#!/usr/bin/python3
import cv2
import numpy as np

#w = 4056
#h = 3040
#circle_width = 2100
#center_coordinates = (1981, 1584)
w = 4056
h = 3026

circle_width = 2640
center_coordinates = (w//2, h//2)

image = np.zeros((h, w, 3), dtype = "uint8")

color = (255, 255, 255)
image = cv2.circle(image, center_coordinates, circle_width//2, color, -1)

cv2.imwrite("mask.ppm", image)
