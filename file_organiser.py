import os, shutil

try:
    path="//home//robotics//Downloads"
    # path1 = os.path.join(path, book)
    # os.mkdir(path1)
    for (path, dirs, files) in os.walk(path):
        for file in files:
            extension=file.split('.')[1] # will take the 2nd object after dot
            print(extension)
            source = ("//home//robotics//Downloads//"+file)
            destination = ("//home//robotics//Downloads//"+extension)
            tt = os.path.exists(destination)
            print(tt)
            if os.path.exists(destination):
                if file.endswith(extension):
                    shutil.move(source, destination)
            else:
                os.mkdir(destination)
                shutil.move(source, destination)
except:
    print("an error occured")
