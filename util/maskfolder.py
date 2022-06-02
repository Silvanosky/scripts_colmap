#!/usr/bin/env python
import os
import shutil
import sys

if len(sys.argv) < 4:
    print("[mask file] [Source image dir] [dest mask directory]")
    exit()

maskfile = sys.argv[1]
srcDir = sys.argv[2]
dstDir = sys.argv[3]

if not os.path.exists(maskfile):
    print("File mask :" + maskfile + " does not exist.")
    exit()

os.makedirs(dstDir, exist_ok=True)

nmaskpath = dstDir + "/" + maskfile
shutil.copy(maskfile, nmaskpath)
print("Copy " + maskfile + " to " + nmaskpath)

amaskpath = os.path.abspath(nmaskpath)
for root, dirs, files in os.walk(srcDir):
    path = root.split(os.sep)
    os.makedirs(dstDir + "/" + root, exist_ok=True)
    for file in files:
        sympath = dstDir + "/" + root + "/" + file
        rpath = os.path.relpath(amaskpath, start=os.path.dirname(sympath))
        print("SymLink to " + sympath)
        os.symlink(rpath, sympath)
