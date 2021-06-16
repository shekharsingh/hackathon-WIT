'''
Filename: objDetect.py
Path: hackathon-WIT/objectExtract
Created Date: Tuesday, June 15th 2021, 10:56:42 pm
Author: Vaishnavi S

Copyright (c) 2021
'''

import pixellib
import cv2
import matplotlib.pyplot as plt 
from pixellib.instance import instance_segmentation
from pixellib.instance import custom_segmentation


segment_image = instance_segmentation()

segment_image.load_model("https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.2/mask_rcnn_coco.h5")
segment_image.segmentImage("Input.jpg", extract_segmented_objects=True, save_extracted_objects=True, show_bboxes=True,  output_image_name="output.jpg")
image=cv2.imread("output.jpg")
plt.imshow(image)

# code for camera video object detect
# capture = cv2.VideoCapture(0)
# segment_camera = custom_segmentation()
# segment_camera.load_model("mask_rcnn_coco.h5")
# segment_camera.process_camera(capture, frames_per_second= 10, output_video_name="output_video.mp4", show_frames= True,
# frame_name= "frame", check_fps = True)
