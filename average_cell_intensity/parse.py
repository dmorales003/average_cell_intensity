# collection of methods for handling images
# based on OpenCV Python Package

import os

def image_list(directory, channel='mask'):
    image_list = set()
    for root, dir, filename in os.walk(directory):
        for file in filename:
            name = file.split('-')
            if file.endswith(
                ('.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp', '.gif')
                ) and f'{channel}' in name:
                image_list.add(file)                           
    print(f'{len(image_list)} number of image sets found.')
    return list(image_list)

def sample_meta(filename):
    # file name format:
    # mask-sample6_100X_002.vsi - GFP, Cy3.tif
    parse_dash = filename.split('-')
    # ['mask','sample6_100X_002.vsi ',' GFP, Cy3.tif']
    parse_us = parse_dash[1].split('_')
    # ['sample6','100X','002.vsi']
    parse_dot = parse_us[2].split('.')
    return parse_dash[1:], parse_us[0], parse_dot[0]


def main():
    pass

if __name__ == '__main__':
    main()

