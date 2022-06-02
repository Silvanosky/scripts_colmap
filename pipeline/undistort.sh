#!/bin/sh

mkdir $DATASET_PATH/dense

colmap image_undistorter \
    --image_path $DATASET_PATH/images \
    --input_path $DATASET_PATH/sparse_geo \
    --output_path $DATASET_PATH/dense_geo \
    --output_type COLMAP \
    --max_image_size 4056
