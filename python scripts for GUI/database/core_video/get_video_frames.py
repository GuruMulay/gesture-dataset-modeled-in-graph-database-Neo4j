import cv2
import cv2.cv as cv
import numpy as np
import os
import shutil



'''
Input: Video
Output: Frames written in specified folder path
'''

def get_video_frames(path, folder_name = 'Frames'):
    #make destination folder if it doesnt exist
    if not os.path.exists(folder_name): os.makedirs(folder_name)
    des_path = folder_name + '/'

    cap = cv2.VideoCapture(path)
    success, frame = cap.read(cv.CV_IMWRITE_JPEG_QUALITY)  # handle of the Video Capture is required for obtaining frame.

    count = 1  #initialize count to write frame number
    while success:
        image_path = des_path + str(count) + '.jpg'
        cv2.imwrite(image_path, frame)  # save frame as JPEG file
        count += 1
        success, frame = cap.read(cv.CV_IMWRITE_JPEG_QUALITY)  # to read the last frame

    cap.release()


'''
Input: Input filename and start and end frame
Output: Frames for specified range
'''
def get_frame_range(filename, start_frame, end_frame, folder_name='temp_frames'):
        # make destination folder if it doesnt exist, delete and recreate if already exists
        if os.path.exists(folder_name): shutil.rmtree(folder_name)
        os.makedirs(folder_name)
        des_path = folder_name + '/'

        if(start_frame>=end_frame):
            print "Cannot proceed, end frame less than start frame!"
            return -1

        cap = cv2.VideoCapture(filename)
        success, frame = cap.read(cv.CV_IMWRITE_JPEG_QUALITY)  # handle of the Video Capture is required for obtaining frame.

        count = 1  # initialize count to write frame number
        while success and (count!=start_frame) :
            success, frame = cap.read(cv.CV_IMWRITE_JPEG_QUALITY)  # to read the last frame
            count += 1

        print 'Count phase 1:', count
        #count= start_frame
        while success and (count!=(end_frame+1)):
            image_path = des_path + str(count) + '.jpg'
            cv2.imwrite(image_path, frame)  # save frame as JPEG file
            success, frame = cap.read(cv.CV_IMWRITE_JPEG_QUALITY)  # to read the last frame
            count += 1

        print 'Count phase 2:', count
        cap.release()


