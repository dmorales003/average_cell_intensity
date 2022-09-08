# segmentation algorithm of fluorescence
# channel based on watershed. threshold
# may be altered to improve segmentation

import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((3,3),np.uint8)

def test(image):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111)
    ax.imshow(image)
    plt.show()

def segmentCells(filename):
    image = cv2.imread(filename)
    image_bw = image[:,:,0]
    image_bw[image_bw < 250] = 0
    contours,hierarchy = cv2.findContours(
        image = image_bw,
        mode=cv2.RETR_CCOMP,
        method=cv2.CHAIN_APPROX_SIMPLE)[-2:]
    return contours,hierarchy

def main():
    pass

if __name__ == '__main__':
    main()