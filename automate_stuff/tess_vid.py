# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev

from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np

import os
import cv2

# name path to image files
image_frames = 'image_frames'

def files():
    try:
        os.remove(image_frames)
    except OSError:
        pass

    if not os.path.exists(image_frames):
        os.mkdir(image_frames)
    
    src_vid = cv2.VideoCapture('test2.mp4')
    return(src_vid)

def process(src_vid):

    # 
    index = 0
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        if not ret:
            break

        # name each frame and save as png 
        name = './image_frames/frame' + str(index) + '.png'

        # save every 100th frame
        if index % 100 == 0:
            print('Extracting frames...' + name)
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    src_vid.release()
    cv2.destroyAllWindows()

def get_text():
    for i in os.listdir(image_frames):
        print(str(i))
        my_example = Image.open(image_frames + "/" + i)
        text  = pytesseract.image_to_string(my_example,lang='fra')
        print(text)


# main driver
if __name__== '__main__':
    vid = files()
    process(vid)
    get_text()
