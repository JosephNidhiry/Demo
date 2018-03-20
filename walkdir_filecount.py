import os

def get_dirname_filecount(startdir):
        for root, directories,filenames in os.walk(startdir):
                print(root,len(filenames))

if __name__=="__main__":
        get_dirname_filecount(os.getcwd())
