import os

main_folder = 'C:\\Users\\Yaniv'

# This is what os.listdir() returns
for folderName, subfolders, filenames in os.walk('C:'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are' + str(subfolders))
    print('The filenames in ' + folderName + ' are' + str(filenames))