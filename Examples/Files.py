# Shelve is important for storing variables that has lists, dictionaries and other well structured data then use this.
import shelve

# We create an object "helloFile" which opens the file to read only
helloFile = open('c:\\Users\\Yaniv\\hello.txt')

# We then read the content of the file and since its Pycharm we use print to see the output
print(helloFile.read())

# We close the file handler by using close() on the object "helloFile"
helloFile.close()

# readlines() will return all of the lines as string inside of a list
helloFile = open('c:\\Users\\Yaniv\\hello.txt')

# This will return this list : ['Hello World !\n', 'This is my file']
helloFile.readlines()
helloFile.close()

# Write into a file (if the file doesn't exist python will create it for us)
helloFile = open('c:\\Users\\Yaniv\\hello2.txt', 'a') # or instead of w you can use A (append)#

# write a string to the file (This will not add new lines):
helloFile.write('Hello!!!!!!')
helloFile.write('Hello!!!!!!')
helloFile.write('Hello!!!!!!\n')

helloFile.write('Here we will have a new line \n')
helloFile.write('Here we will have a new line \n')
helloFile.close()

# For storing complicated data structure you can use shelve

# We will store the shelve.open('mydata') object within shelfFile
# Please note that this creates 3 files (.dat, .bak, .dir and it will all be binary and only python will understand the text inside)
shelfFile = shelve.open('mydata')
# We will store a key with values :
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
# And we will close the object
shelfFile.close()

# We will open the file again
shelfFile = shelve.open('mydata')
# we can now retrieve the key :
print(shelfFile['cats'])
shelfFile.close()
