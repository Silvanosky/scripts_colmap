#!/bin/sh

OUTPATH=sparse_hier

#mkdir bundle_adj

#colmap bundle_adjuster
#    --database_path database.db \
#    --image_path images \
#    --output_path bundle_adj \
#    --BundleAdjustment.refine_principal_point

mkdir $OUTPATH
colmap hierarchical_mapper \
    --database_path $DATASET_PATH/database.db \
    --image_path $DATASET_PATH/images \
    --output_path $DATASET_PATH/$OUTPATH
#    --Mapper.ba_refine_principal_point true

