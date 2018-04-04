import dfsdir
import sys
import numpy as np
import cv2
from os import listdir,makedirs
from os.path import isfile,join,isdir,basename

def err(s):
    print s
    sys.exit()

def error_help():
    print "use -h for help"
    sys.exit()

def isimage(s):
    return s.endswith(".jpg") or s.endswith(".png") or s.endswith(".jpeg")

def help():
    print "Usage: python neg.py [arguments]"
    print "needed arguments:"
    print "-dir [dirname] : directory to dfs for jpg or png or jpeg images"
    print "-out [outdirname] : directory where images will be written to"
    print "-bg [bg file name] : name of bg file to output"
    print "optional flags:"
    print "-gray : turn images to grayscale"
    print "-resize [box size] : number of pixels for each square side"
    sys.exit()

def nothing(s):
    return


def gray_and_resize(s):
    global outfolder,to_gray
    img=cv2.imread(s)
    if(img is None):
        return
    if(not to_gray is None):
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if(not resize_s is None):
        img=cv2.resize(img,(resize_s,resize_s))
    cv2.imwrite(join(outfolder,basename(s)),img)

def write_to_file(s):
    global outfile,outfolder
    outfile.write(join(outfolder,basename(s))+"\n")

def action_file(s):
    if(not isimage(s)):
        return
    gray_and_resize(s)
    write_to_file(s)

def dowork():
    global dirname,outfolder,bg,resize_s,to_gray,outfile
    if(dirname is None or outfolder is None or bg is None):
        error_help()
    if(not isdir(dirname)):
        err("no such dir")
    if(isdir(outfolder)):
    	ok=None
    	while(ok != "Y" and ok!= "N" and ok != "y" and ok != "n"):
    	    ok=raw_input("folder "+outfolder+" already exists. Want to delete it?\n")
        if(ok == "N" or ok == "n"):
            return
    if(isfile(bg)):
    	ok=None
    	while(ok != "Y" and ok != "N" and ok != "y" and ok != "n"):
    	    ok=raw_input("file "+bg+" already exists. Want to delete it?\n")
        if(ok == "N" or ok == "n"):
            return
    outfile=open(bg,"w")
    try:
        makedirs(outfolder)
    except:
        print "writing on existing folder"
    dfsdir.dfs_dir(dirname,nothing,action_file)
    outfile.close()
    print "Done"


def get_args():
    l=len(sys.argv)
    j=1
    global dirname,outfolder,bg,to_gray,resize_s,outfile
    while(j < l):
        inp=sys.argv[j]
        if(inp == "-gray"):
            to_gray=1
            j=j-1
        elif(inp == "-out" and outfile is None):
            if(j < l-1):
                outfolder=sys.argv[j+1]
            else:
                error_help()
        elif(inp == "-dir" and dirname is None):
            if(j < l-1):
                dirname=sys.argv[j+1]
            else:
                error_help()
        elif(inp == "-bg" and bg is None):
            if(j < l-1):
                bg=sys.argv[j+1]
            else:
                error_help()        
        elif(inp == "-resize" and resize_s is None):
            if(j < l-1):
                resize_s=int(sys.argv[j+1])
            else:
                error_help()
        elif(inp == "-h"):
            help()
        else:
            print inp
            error_help()
        j=j+2        


dirname=None
outfolder=None
bg=None
resize_s=None
to_gray=None
outfile=None
get_args()
dowork()






