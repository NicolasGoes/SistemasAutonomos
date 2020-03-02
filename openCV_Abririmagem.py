# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import urllib
import cv2
import numpy as np 
url = "http://s0.geograph.org.uk/photos/40/57/405725_b17937da.jpg"
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)
cv2.imshow('URL Image', img)
cv2.imwrite("ab2.jpg", img)
cv2.waitKey()



