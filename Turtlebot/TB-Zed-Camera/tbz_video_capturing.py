#!/usr/bin/env python3

import os
import cv2
import numpy
import pyzed.sl as sl

# Open the ZED Camera
cam = sl.Camera()
image = sl.Mat()
depth = sl.Mat()

# Initial Parameters
init = sl.InitParameters()
init.camera_resolution = sl.RESOLUTION.HD1080
init.depth_mode = sl.DEPTH_MODE

# Get Camera Status
status = cam.open(init)
if status != sl.ERROR_CODE.SUCCESS:
	print(repr(status))
	exit(1)

runtime = sl.RuntimeParameters()
print('ZED Camera is Recording, use Ctrl-C to stop.')
frames_recorded = 0

image_dir = '/home/admin/Documents/ZED/original/'
process_dir = '/home/admin/Documents/ZED/preprocessed/'

# Live Video Capturing
while True:
	if frames_recorded >= 999:
                cam.close()
		exit(1)
	# Get new frame from camera
	if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS:

		cam.retrieve_image(image, sl.VIEW.LEFT)
		cam.retrieve_image(depth, sl.VIEW.DEPTH)

		image_ocv = image.get_data()
		depth_ocv = depth.get_data()

		cv2.imwrite(os.path.join(image_dir, f'image_{frames_recorded:03}.png'), image_ocv)
		cv2.imwrite(os.path.join(image_dir, f'depth_{frames_recorded:03}.png'), depth_ocv)

		dim = (2048, 1024)

		image_rs = cv2.resize(image_ocv, dim, interpolation = cv2.INTER_AREA)
		depth_rs = cv2.resize(depth_ocv, dim, interpolation = cv2.INTER_AREA)

		cv2.imwrite(os.path.join(process_dir, f'image_{frames_recorded:03}.png'), image_rs)
		cv2.imwrite(os.path.join(process_dir, f'depth_{frames_recorded:03}.png'), depth_rs)

		frames_recorded += 1