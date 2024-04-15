# 1. Create a file with file name sample.txt, accept some data from the user and store it in the file.

# f = open('sample.txt', 'w')
# data = input("Enter some data you want to write into the file : ")
# f.write(data)
# print("Data has been stored in sample.txt.")
# f.close()


#==============================================================================

# 2. Display the data stored in the sample.txt file (created in question 1).

# f = open('sample.txt', 'r')
# data = f.read()
# print(data)
# f.close()

#==============================================================================

# 3. Accept some data from the user and append it into the file sample.txt (created in question 1),
# also the data in the file.

# f = open('sample.txt', 'a')
# new_data = input("Enter new data to append to sample.txt: ")
# f.write(new_data)
# print("All data stored in sample.txt after appending:")
# f.close()

#==============================================================================

# 4. Accept the file name from the user, check the availability of the file: i). If the file exists display
# the data on the screen, ii). If the file is not available, display the appropriate message.

# import os

# fname = input('Enter the name of file to open : ')
# if os.path.isfile(fname):
#     f = open(fname , 'r')
#     data = f.read()
#     print(data)
# else : 
#     print('The file does not exist')

#==============================================================================

# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: i). No. of characters, ii). No. of words and iii). No. of lines
# b. If the file does exist, than display the appropriate message.

# import os 
# fname = input('Enter the name of file to open : ')
# if os.path.isfile(fname) :
#     f = open(fname , 'r')
#     # data = f.read()
#     # print(data)
# else : 
#     print('The file does not exist')
# cl=cw=cc=0
# for line in f : 
#     words = line.split()
#     cl = cl + 1 
#     cw= cw + len(words)
#     cc = cc + len(line) 
# print('Number of line in a file is : ' ,cl)
# print('Number of words in a file is : ' ,cw)
# print('Number of characters in a file is : ' ,cc)
# f.close()

#==============================================================================

# 6. Create and open the binary file with ‘with’ option. Store names of all the subjects you study in
# semester 2. Ask user to enter the subject number they wanted to see and display that subject name.


