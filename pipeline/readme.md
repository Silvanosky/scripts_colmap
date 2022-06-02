# Colmap pipeline

## Sparse
Order :
- extract.sh (Extract feature from image)
- match.sh (match features with each others)
- sparse.sh (mapper - bundle adjustement and autocalib to generate first cloud point)

## Dense
- undistort.sh (generate images undistroted)
- stereo\_match.sh (generate depthmap of images)
- Need to add masks for each image (genereate_mask.py, maskfolder.py)
- stereo_fusion.sh (fusion each depth map)
- mesh_\*.sh (generate mesh with poisson or delaunay)
