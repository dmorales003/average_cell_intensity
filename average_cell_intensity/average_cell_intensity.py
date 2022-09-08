import csv
from tqdm import tqdm
from segment import segmentCells
from parse import image_list, sample_meta
from display import show_cells, save_cells
from calculate import mask_out_and_average

mask_directory = '/Users/dmorales/Documents/data/microscopy/2022_08_23_jeanette/result/masks/'
image_directory = '/Users/dmorales/Documents/data/microscopy/2022_08_23_jeanette/result/normalized/'
export_directory = '/Users/dmorales/Documents/data/microscopy/2022_08_23_jeanette/result/export/'

def main():
    with open(export_directory+'export.csv','a+',newline='') as file:
        write = csv.writer(file)
        data = ['sample', 'number', 'channel', 'cell_no', 'area', 'average']
        write.writerow(data)
        masks = image_list(mask_directory, 'mask')
        for image in tqdm(masks):
            suffix, sample, number = sample_meta(image)
            contours, hierarchy = segmentCells(mask_directory + image)
            for channel in ['C1','C2']:
                raw = '-'.join([channel]+suffix)
                #show_cells(raw, contours, hierarchy) # show boundaries from segmentation
                save_cells(image_directory+raw, contours, hierarchy, export_directory+'masked-'+raw)
                output = mask_out_and_average(image_directory+raw, sample, number, channel, contours, hierarchy)
                for entry in output:
                    write.writerow(entry)
    file.close()

if __name__ == '__main__':
    main()