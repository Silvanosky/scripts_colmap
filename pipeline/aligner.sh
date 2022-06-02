#!/bin/sh

colmap model_aligner \
    --input_path $DATASET_PATH/sparse \
    --output_path $DATASET_PATH/sparse_geo \
    --ref_images_path imagesGPS.txt \
    --ref_is_gps 1 \
    --alignment_type enu \
    --robust_alignment 1 \
    --robust_alignment_max_error 1.0
