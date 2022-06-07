# code by Tanmaywankhede07
import os
import cv2
from time import sleep
from threading import *
from pathlib import Path


class image1(Thread):
    def run(self):
        dir_path = "/home/tanmay/Desktop/mutlithreading/input1"
        output_path = "/home/tanmay/Desktop/mutlithreading/output1"
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,path)):
                eachimg_path =dir_path+'/'+path
                img = cv2.imread(str(eachimg_path))
                dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
                cv2.imwrite(os.path.join(output_path,str(path)),dst)
        sleep(1)

class image2(Thread):
    def run(self):
        dir_path = "/home/tanmay/Desktop/mutlithreading/input2"
        output_path = "/home/tanmay/Desktop/mutlithreading/output2"
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,path)):
                eachimg_path =dir_path+'/'+path
                img = cv2.imread(str(eachimg_path))
                dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
                cv2.imwrite(os.path.join(output_path,str(path)),dst)
        sleep(1)


t1 = image1()
t2 = image2()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Task Has been performed!!, Check the output file")
print("ouputfile is at the location where this code is saved.")
