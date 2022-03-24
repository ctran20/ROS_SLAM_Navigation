import shutil, os
import getpass
#files = ['file1.txt', 'file2.txt', 'file3.txt']

def copytree(main_dir, src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
	print item
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

root, dirs, files = os.walk("models").next()
print dirs
#print len(dirs)
print  (os.getlogin())

#for f in dirs:
#    shutil.copy(dir_path+"/new_models/"+f, '~/.gazebo/models/')

source = dir_path+"/models/"
dest = "/home/"+os.getlogin()+"/"+".gazebo/models/"

copytree(dir_path, source, dest, symlinks=False, ignore=None)
