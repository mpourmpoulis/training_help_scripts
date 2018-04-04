# !/usr/bin/python

from os import listdir,makedirs
from os.path import isfile,join,isdir,basename
import sys
def my_error(message):
    print message
    sys.exit()



def dfs_dir(dirname, method_dir,method_file):
    if(not dirname.endswith("/")):
        dirname+="/";
    if(not isdir(dirname)):
        my_error("invalid dir")
    elements=listdir(dirname)
    for el in elements:
    	fullpath=join(dirname,el)
        if(isdir(fullpath)):
            method_dir(fullpath)
            dfs_dir(fullpath,method_dir,method_file)
        elif (isfile(fullpath)):
            method_file(fullpath)
        else:
            print "unknown type" + fullpath+"\n"



