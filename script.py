import os,sys
from distutils.dir_util import copy_tree

if len(sys.argv) < 2 :
    print("Please specify the app name")
    exit()

app_name = sys.argv[1]
current_directory = os.getcwd()

directory_path = os.path.join(current_directory, app_name)

print("Creating react app '" + app_name + "' in " + directory_path + "\\")
print("Copying node_modules...")
print("This may take a couple of minutes.")

os.mkdir(directory_path)

copy_tree('C:/Program Files/react_files/newapp',directory_path)

print("Modifying package.json..")

f = open(directory_path + "\package.json", "r")
content = f.read()

content = content.replace("newapp",app_name)
f = open(directory_path + "\package.json", "w")
f.write(content)

f1 = open(directory_path + "\package-lock.json", "r")
content = f1.read()

content = content.replace("newapp",app_name)
f1 = open(directory_path + "\package-lock.json", "w")
f1.write(content)

print("Done!")
