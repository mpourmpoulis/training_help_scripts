import numpy as np
import cv2
from random import randint

#off by one errors for the win

def random_coord(low1,up1,low2,up2):
     return [randint(low1,up1),randint(low2,up2),randint(low1,up1),randint(low2,up2)]



def edges_of_window(window):
    x=window[0]
    y=window[1]
    dx=window[2]
    dy=window[3]
    #possible off by one error
    return [ [x,y], [x+dx,y], [x, y+dy], [x+dx,y+dy] ]

def point_is_inside_window(point,window):
    xinside=(point[0] >= window[0] and point[0] <=(window[0]+window[2]))
    yinside=(point[1] >= window[1] and point[1] <=(window[1]+window[3]))
    return xinside and yinside



def windows_have_common_pixels(rw,cord):
    rwedges=edges_of_window(rw)
    cordedges=edges_of_window(cord)
    retval=False
    for rwedge in rwedges:
        retval=retval or point_is_inside_window(rwedge,cord)
    for cordedge in cordedges:
        retval=retval or point_is_inside_window(cordedge,rw)
    return retval


def okwindow(rw,image,lcord):
    dim=image.shape
    if(rw is None):
        return False
#check later
    if((rw[0]+rw[2] > dim[0]) or (rw[1]+rw[3]>dim[1])):
        return False
    for cord in lcord:
        if(windows_have_common_pixels(rw,cord)):
            return False
    return True

def generate_random_window(image, lcord):
	rw=None
	sh=image.shape
	xmax=sh[0]
	ymax=sh[1]
	while(not okwindow(rw,image,lcord)):
	    rw=random_coord(0,xmax,0,ymax)
	return rw

def generate_windows_random(image, lcord, minsize, maxsize, numbgen):
    window_list=[]
    print "numbgen is "+str(numbgen)
    for i in range (0,numbgen):
        window_list.append(generate_random_window(image, lcord))
        print i
    #print window_list
    return window_list

def generate_windows(image, lcord, minsize, maxsize, numbgen,mode):
    if(mode == 0):
        return generate_windows_random(image, lcord, minsize, maxsize, numbgen)
    return None

def get_images_from_windows(image,windows_generated):
    list_images=[]
    for window in windows_generated:
    	#print "window is "
    	#print window
        x=window[0]
        y=window[1]
        dx=window[2]
        dy=window[3]
        list_images.append(image[x:x+dx,y:y+dy])
        #print "naoume" + str(len(list_images))
    return list_images



#functions for resizing an image
def fix_image_size(image,minsize,maxsize):
    dimensions=image.shape
    low=min(dimensions[0],dimensions[1])
    high=max(dimensions[0],dimensions[1])
    if(low < minsize or (high > maxsize and maxsize != 0)):
    	print "here"
        return cv2.resize(image,(maxsize,maxsize))       
    return image




def fix_size_of_images(list_images,minsize,maxsize):
    outputlist=[]
    for image in list_images:
        outputlist.append(fix_image_size(image,minsize,maxsize))
    return outputlist



def create_images(image, lcord, minsize, maxsize, numbgen,mode):    
    windows_generated=generate_windows(image, lcord, minsize, maxsize, numbgen,mode)
    #print "printing windows"
    #print len(windows_generated)
    print windows_generated
    #print "done"
    list_images=get_images_from_windows(image,windows_generated)
    return fix_size_of_images(list_images,minsize,maxsize)





#img=cv2.imread("training_cascade/negatives/beach-1.jpg")
img=cv2.imread("/home/mpourmpoulis/Pictures/turtles/t-1.jpg")
print img.shape
lcord=[ [0, 0, 500, 1900]    ]
ll=create_images(img,lcord,0,500, 1, 0)
for gg in ll:
    print gg.shape
cv2.imwrite("naoume.jpg", ll[0])
print point_is_inside_window( [10,20], [0,0,100,100]                   )




      