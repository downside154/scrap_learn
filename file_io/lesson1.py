# f = open("test.txt") # open file in current direcotry
# f = open("C:/Python38/README.txt") #specifying full path

# # modes in reading : default is read & text
# # 1. r - Opens a file for reading. (default)
# # 2. w - Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# # 3. x - Opens a file for exclusive creation. If the file already exists, the operation fails.
# # 4. a - Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.	
# # 5. t - Opens in text mode. (default)
# # 6. b - Opens in binary mode.		
# # 7. + - Opens a file for updating (reading and writing)


# f = open("test.txt") # opens file in 'r' or 'rt'
# f = open('test.txt', 'w') # write in text mode
# f = open('img.bmp', 'r+b') # read and write in binary mode

# # unlike other languages, the character <a> does not imply the number 97 until it is encoded sing ASCII or other equivalent encondings.
# # The default encoding is platform dependent: 
# #       1. Windows - cp1252
# #       2. Linux - utf-8
# #Try not to rely on default encoding. Thus:
# f = open("test.txt", mode='r', encoding='utf-8')

# #closing files
# f = open("test.txt", encoding='utf-8')
# f.close()
# # but this method is not entirely safe if an exception arises so use:
# try:
#     f = open("test.txt", mode='r', encoding='utf-8')
# finally:
#     f.close()

# # THE BEST WAY TO CLOSE is :
# with open('test.txt', encoding = 'utf-8') as f:
#     #perform file operations ~~~~~~~~~~~~~~
#     pass


#Example:
# with open('test.txt', 'w', encoding = 'utf-8') as f:
#     f.write("my first file\n")
#     f.write("This file\n")
#     f.write("Contains three lines\n")


# READ Files 
f = open("test.txt",'r', encoding='utf-8')
f.read(4) # first 4 characters
f.read(4) # next 4 characters
f.close()

f.tell() # get the current file position
f.see(0) # bring file cursor to initial position


for line in f:
    print(line, end='')

f.readline() # -> 'This is my first file\n'
f.readline() # -> 'This file\n'
f.readline() # -> 'contains three lines\n'
f.readline() # -> ''
# readlines() moethod returns a list of remaining lines of the entire file.
# All these reading methods return empty values when the EOF (end of file) is reached.

# f.readlines() --> ['This is my first file\n', 'This file\n', 'contains three lines\n']




