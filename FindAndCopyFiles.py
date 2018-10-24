#Script for finding files from a source directory and copy them to a destination directory
#Names for files to be searched for must be specified in a .txt file
#This particular example is aimed towards searching for .mp3 files
#Based on DFS


import shutil
import os

src="*Your source path*"												#Directory to be searched
sourceTxt="*Path to .txt file with files name to be searched*"			#Files to be searched in the directory
dest="*Your destination path*"											#Destination folder to copy files

toSearch = []

with open (sourceDest, 'rt') as toSearch:
    for line in toSearch:
        mp3=line.rstrip()+".mp3"
        toSearch.append(mp3)

print(toSearch)
print(type(toSearch))													#returns list

folder = file = 0

try:
    os.makedirs(dest)
except:
    print("ALREADY EXISTED")
	
def checkFile (src, searchFile):
    global folder, file
    src_file = os.listdir(src)
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)
        if os.path.isdir(full_file_name):
            folder += 1
            print(full_file_name)
            checkFile(full_file_name,toSearch)
        else:
            if file_name in toSearch:
                shutil.copy(full_file_name, dest)
				print("COPIED")
                print(file_name)
            file += 1

checkFile(src,	toSearch)

print("FOLDER",folder)
print("FILE",file)