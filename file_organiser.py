import os, shutil

try:
    path="//home//robotics//Downloads/book"    
    for (path, dirs, files) in os.walk(path):
        for file in files:
            extension=file.split('.')[-1] # will take the last object after dot
            print(extension)
            source = (path+"//"+file)
            destination = (path+"//"+extension)
            if os.path.exists(destination):
                if file.endswith(extension):
                    shutil.move(source, destination)
            else:
                os.mkdir(destination)
                shutil.move(source, destination)
except:
    print("This should never happened")
