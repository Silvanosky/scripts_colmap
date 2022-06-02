#/bin/sh

folder=batch_1_1
mkdir ${folder}_ppm

cd $folder

for f in $(echo *)
do
 echo "Processing $f"
 # do something on $f
 dcraw -v -o 1 -W -T $f
done
mv *.ppm "../${folder}_ppm"
