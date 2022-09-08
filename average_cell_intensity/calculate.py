import cv2
import numpy as np

def mask_out_and_average(filename, sample, number, channel, contours, hierarchy):
    data = []
    image = cv2.imread(filename,cv2.IMREAD_ANYDEPTH)
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if hierarchy[0][i][3] == -1:
            mask = np.zeros_like(image)
            cv2.drawContours(
                mask,
                contours,
                i,
                (255, 255, 255),
                -1)
            average = np.mean(image[mask == 255])
            data.append([sample, number, channel, i, area, average])
    return data

def main():
    pass

if __name__ == '__main__':
    main()