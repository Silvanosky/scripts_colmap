#!/bin/sh

colmap patch_match_stereo \
    --workspace_path $DATASET_PATH/dense_geo \
    --workspace_format COLMAP \
    --PatchMatchStereo.geom_consistency true \
    --PatchMatchStereo.max_image_size 2000
