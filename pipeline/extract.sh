#!/bin/sh

#CURPATH=$(pwd)

colmap feature_extractor \
   --database_path "$DATASET_PATH/database.db" \
   --image_path "$DATASET_PATH/images" \
   --ImageReader.camera_model "THIN_PRISM_FISHEYE" \
   --ImageReader.camera_params "1414.519041, 1416.511288, 2028.000000, 1520.000000, -0.015719, 0.173639, -0.002911, 0.001838, -0.388817, 0.593049, -0.010704, -0.001051" \
   --ImageReader.single_camera_per_folder true \
   --ImageReader.camera_mask_path mask.ppm \
   --SiftExtraction.max_image_size 4056


#   --ImageReader.camera_model "OPENCV_FISHEYE" \
#   --ImageReader.camera_params "967.7111499920471, 967.741935483871, 2028, 1520, 0, 0, 0, 0" \
#   --ImageReader.camera_model "THIN_PRISM_FISHEYE" \
#   --ImageReader.camera_params "967.726543, 967.726543, 2028.000000, 1520.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000" \
#   --ImageReader.camera_model "FULL_OPENCV" \
#   --ImageReader.camera_params "967.726543, 967.726543, 2028.000000, 1520.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000" \


