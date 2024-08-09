# #Opening a file
# #reading a file
# #writing a file
# #closing a file

# #Different modes:
# #'r' read mode (default mode)
# #w write mode (creates a new file or edits existin)
# #a Append (adds content to the end of the file)
# #b binary mode
# #t Text mode (default mode)
# #x Exclusive creation (fails if file alraedy exist) 

# # Open a file for reading (default mode)
# #file = open('example.txt', 'r')

# #TO READ A FILE
# # read(): reads entire file
# # readline(): one line at a time
# # readlines(): reads all lines into a list

# # Read the entire file
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# # Read one line at a time
# with open('example.txt', 'r') as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

# # Read all lines into a list
# with open('example.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end='')

# # Write to a file (overwrites existing content)
# with open('example.txt', 'w') as file:
#     file.write('Hello, World!\n')

# # Append to a file
# with open('example.txt', 'a') as file:
#     file.write('Appending a new line.\n')

# # Write multiple lines
# lines = ['First line\n', 'Second line\n', 'Third line\n']
# with open('example.txt', 'w') as file:
#     file.writelines(lines)

# # Using close() method
# file = open('example.txt', 'r')
# content = file.read()
# file.close()

# # Using with statement (recommended)
# with open('example.txt', 'r') as file:
#     content = file.read()



# # Writing to a file
# with open('example.txt', 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a test file.\n')

# # Appending to a file
# with open('example.txt', 'a') as file:
#     file.write('Appending a new line.\n')

# # Reading from a file
# try:
#     with open('example.txt', 'r') as file:
#         content = file.read()
#         print('File Content:')
#         print(content)
# except FileNotFoundError:
#     print('File not found.')
# except IOError:
#     print('An I/O error occurred.')




# file_path = "wale.txt" # This is useful when you need to just pass different files you want to work with
# fp = "dibaal.txt"

# with open(file_path, "w") as file:
#     file.write("1. This is wale's text 1\n")
#     file.write("2. This is wale's text 2\n")
#     file.write("3. Hey dibaal wasup with my 2 lines of file written above")
#     file.write("4. Hey dibaal wasup with my 2 lines of file written above. I ask again")


# with open(file_path, "r") as file:
#     lines = file.readlines()
#     print("Contents of the file in read mode:")
#     for line in lines:
#         if "dibaal" in line: #To print lines that contain dibaal in it
#             print(line.strip())

# with open(fp, "a") as file:
#     file.write("1. Just testing this 1\n")
#     file.write("2. this is the 2nd line 2\n")

# with open(fp, "r") as file:
#     lines = file.readlines()
#     print("Contents of the file in read mode:")
#     for line in lines:
#         # if "dibaal" in line: #To print lines that contain dibaal in it
#             print(line.strip()) # strp() is a method that removes any whitespaces from the beginning and end of the string stored in the variable line



# file_path = "wale.txt" 
# fp = "dibaal.txt"

# def read_file(f):# This reusable function is to just check if a particular word (wale) exixt
#      with open(f, "r") as file:
#           lines = file.readlines() #This function opens the file in read mode and reads lines into a list called lines.
#           for line in lines:
#                if "wale" in line:
#                     return True
#           return False    


# with open(file_path, "w") as file:
#     file.write("1. This is wale's text 1\n")
#     file.write("2. This is wale's text 2\n")
#     file.write("3. Hey dibaal wasup with my 2 lines of file written above")
#     file.write("4. Hey dibaal wasup with my 2 lines of file written above. I ask again")

# with open(fp, "a") as file:
#     line = read_file(fp) #what ever the function returns is what we use to process here. If it return False, then wale exit in the line, but if it returns True then we can go ahead to append
#     if line:
#          print("This line with wale already exist")
#     else:
#          file.write("1. This is wale's text 1\n")
#          file.write("2. This is wale's text 2\n")



               