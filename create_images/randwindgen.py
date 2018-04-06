import cv2
from wind import random_subwindow,window_check_size,windows_collide,window_overlaps_with_list,window_dim_ratio


#possible infinite loop
def generate_window_random(imagewindow,lcord,min_window_size,max_window_size,limit):
    randwind=random_subwindow(imagewindow)
    while (window_overlaps_with_list(randwind,lcord) or (not window_check_size(randwind,min_window_size,max_window_size)) or window_dim_ratio(randwind) > limit):
        randwind=random_subwindow(imagewindow)
    print window_dim_ratio(randwind)
    return  randwind


def generate_random_windows(image,lcord,minsize,maxsize,numbgen,limit):
    windowlist=[]
    imagewindow=[0,0,image.shape[0],image.shape[1]]
    for i in range(0,numbgen):
        windowlist.append(generate_window_random(imagewindow,lcord,minsize,maxsize,limit))
    return windowlist













