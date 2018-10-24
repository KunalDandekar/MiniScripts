#Script for renaming files from a source directory
#All files from a directory are renamed
#This particular example is aimed towards renaming files in incremental order. Eg: File1, File2 and so on


import shutil
import os

src="*Your source path*"

newName = "*New name here*"
i = 1;


def renameFile(src):
    global i
    src_file = os.listdir(src)
    print(src_file)
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)
        if os.path.isdir(full_file_name):
            renameFile(full_file_name)
        else:
            print(file_name)
            os.rename(full_file_name, dest+newName+str(i)+".txt")
            i=i+1
			

renameFile(src)
