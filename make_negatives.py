import cv2
from os import listdir,makedirs
from os.path import isfile,join

#downloads='home/root/pigi/training_cascade/downloads'
downloads='downloads/'
folder = 'downloads/*' # Source Folder
dstpath = 'negatives/' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

# Folder won't used

folders=[join(downloads,f) for f in listdir(downloads)]
for folder in folders:
    images = [i for i in listdir(folder) if isfile(join(folder,i))] 
    for image in images:
        try:
            #print os.path.join(folder,image)
            print folder+'/'+image
            img = cv2.imread(folder+'/'+image)
            print "hello"
            #img = cv2.imread(image)
            img = cv2.resize(img, (100, 100))
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            dstPath = join(dstpath,image)
            cv2.imwrite(dstPath,gray)
        except:
            print ("{} is not converted".format(image))