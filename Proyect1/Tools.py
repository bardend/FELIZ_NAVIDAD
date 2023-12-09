import numpy as np
import matplotlib.pyplot as plt
import cv2
from KMeans import *

"""
 Open CV for segmentation
The HSV model can be better than RGB model because is more robust for handling diferent lighting conditions
If something is red, it can be bright red or dark red , for RGB bright red and dark can be quite diferent 
                                                        for HSV have similar hues.  
kernel 	= np.ones( (3,3), np.uint8 )
Dilation : 
This can used to connect pixels that belongs to the same object 
dilated = cv2.dilate(postThresholdImage, kernel, iterations=1)
eroded 	= cv2.erode(dilated, kernel, iterations=1)
"""

def segment(img, k):

    pixel = img.reshape((-1,3)) 
    pixel_val = np.float32(pixel)

    kmean = K_Means(k)
    kmean.fit(pixel_val)
    centers = np.uint8(kmean.get_centroids())
    label = kmean.get_labels()

    segment_im = centers[label]
    segment_im = segment_im.reshape(img.shape)
    return segment_im
