#!/bin/sh

echo $#
if (( "$#" < "2" )); then
    echo "[INPUT] [OUTPUT]";
    exit 1;
fi

if [ -z ${DATASET_PATH+x} ]; then
    echo "DATASET_PATH is unset";
    exit 1
else
    echo "DATASET_PATH is set to '$DATASET_PATH'";
fi

INPUT_PATH=$1
OUTPUT_PATH=$2

cd $DATASET_PATH
echo "==========================="
echo "Export COLMAP Features from $DATASET_PATH/database.db -> HomolColmap"
echo "==========================="
colmap_export_features --database_path $DATASET_PATH/database.db --SH Colmap

echo "==========================="
echo "Export COLMAP Reconstruciton from $INPUT_PATH -> $OUTPUT_PATH"
echo "==========================="
colmap_export_Rt --input_path $INPUT_PATH --output_path $OUTPUT_PATH

echo "==========================="
echo "Import COLMAP camera orientations in Ori-Colmap"
echo "==========================="
cd $OUTPUT_PATH
mm3d TestLib Str2MM ".*camera" Ori-Colmap
mv Ori-Colmap ../
