import os
import sys

if(not len(sys.argv)==3):
    print("Usage: filelistgetter directory_path 拡張子")
    sys.exit(0)
else:
    directory=os.listdir(sys.argv[1])
    for filelist in directory:
        print(filelist)