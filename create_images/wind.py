from random import randint

#in the following we will use r for row and c for column

# returns a list of the corners of a window
def corners_of_window(window):
    r=window[0]
    c=window[1]
    dr=window[2]
    dc=window[3]
    return [ [r,c] , [r+dr-1,c] , [r,c+dc-1], [r+dr-1,c+dc-1] ]

# boolean function, checks if a given point is inside a window
def point_is_inside_window(point,window):
    rinside=(point[0] >= window[0] and point[0] <(window[0]+window[2]))
    cinside=(point[1] >= window[1] and point[1] <(window[1]+window[3]))
    return rinside and cinside


# boolean function returns true if the two windows have a common point
def windows_collide(window1, window2):
    retval=False
    for corner in corners_of_window(window1):
        retval=retval or point_is_inside_window(corner,window2)
    for corner in corners_of_window(window2):
        retval=retval or point_is_inside_window(corner,window1)
    return retval


# generate a random subwindow
def random_subwindow(window):
    r=randint(window[0],window[0]+window[2]-1)
    c=randint(window[1],window[1]+window[3]-1)
    dr=randint(1,window[0]+window[2]-r-1)
    dc=randint(1,window[1]+window[3]-c-1)
    return [r, c, dr, dc]

# boolean function returns true if each of the window's dimensions fit the constraints
def window_check_size(window,min_window_size,max_window_size):
    low =min(window[2],window[3])
    high=max(window[2],window[3])
    return (low >= min_window_size and high <= max_window_size)

# boolean checks if a window overlaps with another window in a list of windows
def window_overlaps_with_list(window, windowlist):
    for wind in windowlist:
        if(windows_collide(window,wind)):
            return True
    return False

# int returns ratio of window dimensions
def window_dim_ratio(window):
    low=min(window[2],window[3])
    high=max(window[3],window[2])
    return float(high)/low











