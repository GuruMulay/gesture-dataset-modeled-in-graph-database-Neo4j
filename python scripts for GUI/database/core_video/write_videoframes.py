import cv2, cv2.cv as cv
import numpy as np
import os, shutil
from dependencies.sort_files import *
from core_video.get_codec import *

'''
Input: Video Frames
Output: Video File in specified format
'''

def write_videoframes(output_file_name, folder_name = 'temp_frames', fps= 30, format = 'avi'):
    ref_file = folder_name + '/' + os.listdir(folder_name)[0]
    if (os.path.isfile(ref_file)):
        height, width = cv2.imread(ref_file).shape[:2]
        codec = get_codec(format)
        out = cv2.VideoWriter(output_file_name, codec, fps, (width, height))
        folder = sort_files(folder_name)

        for i in folder:
            pic = folder_name + '/' + str(i) + '.jpg'
            img = cv2.imread(pic)
            out.write(img)
        out.release()
        shutil.rmtree(folder_name)
    else:
        print 'Reference image file not found!'


