import shutil
import os

main_folder = 'C:\\Users\\Yaniv\\Desktop\\Python-Projects'
main_file = main_folder+'spam.txt'

# Directories in use
directory =[main_folder+'\\delicious', main_folder+'\\walnut', main_folder+'\\delicous_backup']

for i in directory[0:2]:
   if not os.path.exists(i):     # Create directories
       os.makedirs(i)


# Start by creating a file
file = open(main_file, 'w')
file.write("This is the first line\n")
file.write("This is the second line")
file.close()


# Start to run
shutil.copy2('c:\\spam.txt', 'c:\\delicious')
shutil.copy2('c:\\spam.txt', 'c:\\delicious\\spamspam.txt')
shutil.copytree('c:\\delicious', 'c:\\delicious_backup\\')
shutil.move('c:\\delicious\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt')

# Cleanup old leftover directories
for i in directory:
    if os.path.exists(i):
      shutil.rmtree(i)