import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file


f=open("info.lst","w")

for file in files("positives"):
    print(file)
    f.write("positives/"+file)
    f.write(" 1 0 0 49 49\n")


f.close()