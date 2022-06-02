#!/bin/sh

colmap stereo_fusion \
    --workspace_path $DATASET_PATH/dense \
    --workspace_format COLMAP \
    --input_type geometric \
    --output_path $DATASET_PATH/dense/fused.ply \
    --StereoFusion.mask_path $DATASET_PATH/dense/mask \
    --StereoFusion.num_threads 10

