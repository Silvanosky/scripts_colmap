#!/usr/bin/python3
import os
import shutil
import sys

if len(sys.argv) < 3:
    print("[Source image dir] [Destination dir]")
    exit()

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
        #sympath = dstDir + "/" + root + "/" + file
        rpath = os.path.relpath(path, start=os.path.dirname(dstDir))
        print(rpath)
        dstFile = dstDir + "/" + filename
        print("SymLink to " + dstFile)
        os.symlink(rpath, dstFile)
