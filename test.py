import os
import cv2

file_list = os.listdir("/home/linhan/sort/mot_benchmark/train/ADL-Rundle-6/img1")
file_list.sort()

for file in file_list:
    path = "/home/linhan/sort/mot_benchmark/train/ADL-Rundle-6/img1" + os.path.sep + file
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow("img", img)
    cv2.waitKey(1)
