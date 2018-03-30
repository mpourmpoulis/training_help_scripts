import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file


f=open("bg.txt","w")

for file in files("negatives"):
    print(file)
    f.write("negatives/"+file)
    f.write("\n")


f.close()