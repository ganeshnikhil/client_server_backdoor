import os 
import sys 
sys.setrecursionlimit(10**6)
file=open('all_path.txt','w')
def listdirs(rootdir):
    try:
        for it in os.scandir(rootdir):
            if it.is_dir():
                file.write(str(it.path)+'\n')
                listdirs(it)
    except Exception as e:
        pass
rootdir = '/users'
listdirs(rootdir)
file.close()
#using this program you can mine all file path in your system
