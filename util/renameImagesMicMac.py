#!/usr/bin/python3
import os
import shutil
import sys

if len(sys.argv) < 3:
    print("[Source image dir] [Destination dir] [Optional .camera folder]")
    exit()

cameraExport = ""
if len(sys.argv) == 4:
    print("Filtering by camera exportation")
    cameraExport = sys.argv[3]

srcDir = sys.argv[1]
asrcDir = os.path.abspath(srcDir)

dstDir = sys.argv[2]
adstDir = os.path.abspath(dstDir)

if not os.path.exists(srcDir):
    print("Image directory :" + srcDir + " does not exist.")
    exit()

for root, dirs, files in os.walk(srcDir):
    path = root.split(os.sep)
    for file in files:
        path = root + "/" + file
        print(path)
        filename = path.replace(srcDir + "/", "")
        print(filename)
        filename = filename.replace("/", "-")
        print(filename)
        if cameraExport != "" and not os.path.exists(cameraExport + "/" + filename + ".camera"):
            print("Skip image: " + filename + " because not oriented.")
            continue

        #sympath = dstDir + "/" + root + "/" + file
        dstFile = dstDir + "/" + filename
        rpath = os.path.relpath(path, start=os.path.dirname(dstFile))
        print(rpath)
        print("SymLink to " + dstFile)
        os.symlink(rpath, dstFile)
