#!/bin/sh

#CURPATH=$(pwd)

colmap exhaustive_matcher \
   --database_path $DATASET_PATH/database.db \
   --SiftMatching.guided_matching true
