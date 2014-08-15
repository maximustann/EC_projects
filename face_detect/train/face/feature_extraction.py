#!/usr/bin/env python
import sys
import Image
import os
import numpy
import csv
import otsu

def feature_percentage(row_start, row_end, col_start, col_end, img):
    count = 0.0
    for i in xrange(row_start, row_end):
        for j in xrange(col_start, col_end):
            if img[i][j] == 0:
                count += 1
    return float("{0:.2f}".format(round(count / ((row_end - row_start) * (col_end - col_start)), 2)))

def feature_extract(img):
    '''
        define feature's start point and end point
    '''
    feature_list = []
    #left_eye
    row_start = 0
    row_end = row_start + 7
    col_start = 0
    col_end = col_start + 7
    left_eye = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(left_eye)

    #forehead
    row_start = 0
    row_end = row_start + 2
    col_start = 6
    col_end = col_start + 5
    forehead = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(forehead)

    #right_eye
    row_start = 0
    row_end = row_start + 7
    col_start = 12
    col_end = col_start + 7
    right_eye = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(right_eye)

    #nose_bridge
    row_start = 2
    row_end = row_start + 9
    col_start = 8
    col_end = col_start + 2
    nose_bridge = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(nose_bridge)

    #left_cheek
    row_start = 7
    row_end = row_start + 6
    col_start = 0
    col_end = col_start + 6
    left_cheek = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(left_cheek)

    #right_cheek
    row_start = 7
    row_end = row_start + 6
    col_start = 12
    col_end = col_start + 7
    right_cheek = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(right_cheek)

    #nose
    row_start = 11
    row_end = row_start + 2
    col_start = 6
    col_end = col_start + 6
    nose = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(nose)

    #mouth
    row_start = 14
    row_end = row_start + 2
    col_start = 4
    col_end = col_start + 10
    mouth = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(mouth)
    return feature_list

def write_file(filename, data):
    title = ['left_eye', 'forehead', 'right_eye', 'nose_bridge', \
            'left_cheek', 'right_cheek', 'nose', 'mouth']
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(title)
        writer.writerows(data)

    f.close()

def cal_imgs():
    
    data = []
    for i in xrange(1, 2429):
        if i < 10:
            no = "0000" + str(i)
        elif i >= 10 and i < 100:
            no = "000" + str(i)
        elif i >= 100 and i < 1000:
            no = "00" + str(i)
        elif i >= 1000 and i < 2429:
            no = "0" + str(i)
        filename = "face" + no + ".pgm"
        im = Image.open(filename)
        imarray = numpy.array(im)
        
        width = im.size[0]
        height = im.size[1]
        my_im = Image.new("L", (width, height))
        my_im_array = numpy.array(my_im)

        threshold = otsu.otsu(imarray, height, width)

        otsu.scan_image(imarray, my_im_array, height, width, threshold)

        data.append(feature_extract(my_im_array))
    write_file("face_dataset.csv", data)

if __name__ == "__main__":
    cal_imgs()

