import cv2
from randwindgen import generate_random_windows


def windows_to_images(image,windows,togray):
    if(windows is None):
        return None
    images=[]
    if(togray):
        limage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    for window in windows:
        img=image[window[0]:window[0]+window[2], window[1]:window[1]+window[3]]
        images.append(img)
    return images


def create_images(image,lcord,minsize,maxsize,numbgen,mode,togray=True):
    windows=None
    if(mode == 0):
        windows=generate_random_windows(image,lcord,minsize,maxsize,numbgen,2.0)
    return windows_to_images(image,windows,togray)
