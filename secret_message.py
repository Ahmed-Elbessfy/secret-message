import os 

def rename_file():
    file_names = os.listdir(r"E:\Web Design\1MCoder\Python\Files")
    #print file_names

    for name in file_names:
        os.rename(name,name.translate(None,"0123456789"))
        print name


rename_file()