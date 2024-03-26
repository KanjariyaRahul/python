# 1) Create a list containing several strings. Take input from the user (search string); display whether
# entered string is available in the list or not.


# string_list = ["apple", "banana", "orange", "grape", "kiwi"]


# search_string = input("Enter a string to search in the list: \n")

# if search_string in string_list:
#     print("The entered string is available in the list.")
# else:
#     print("The entered string is not available in the list.")

# =======================================================================

# 2) Accept the string from the user; display the message whether the entered string is palindrom or not.

# str = input("Enter a string : ")

# str = str.lower().replace(" " , "")

# if str  == str[::-1] :
#     print("\n The entered string is a palindrome.")
# else:
#     print(" \n The entered string is not a palindrome.")

# =======================================================================


#3) Accept the string from the user; display the string in the reverse order.

# str = input("Enter a string : ")

# display  = str[:: -1]
# print ("The string in reverse order  is : ", display)
# =======================================================================

# 4) Accept the string from the user; allow user to choose from the following options and perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title case 

# Take input from the user
# string = input("Enter a string : ")
 

# print("Choose an option : ")
# print("1. Convert to upper case")
# print("2. Convert to lower case")
# print("3. Convert to swap case")
# print("4. Convert to title case")


# choice = input("Enter your choice (1/2/3/4): ")

# if choice == '1':
#     result = string.upper()
# elif choice == '2':
#     result = string.lower()
# elif choice == '3':
#     result = string.swapcase()
# elif choice == '4':
#     result = string.title()
# else:
#     print("Invalid choice")
#     exit()
# print("Result:", result)

# =======================================================================


# 5) Allow users to enter multiple strings in the list; arrange the entered string into alphabetical
# order and display.

# string = []

# n = int(input('How many string you want to enter ? :'))
# for i in range(n):
#     print("Enter the string  : ",end = '')
#     string.append(input())
# print(string)
# arrange = string.sort()
# print('========  arrange the entered string into alphabetical order ========= ')
# for i  in string : 
#         print(i)

# =======================================================================

# 6) Create a tuple and display it. Enter 25 at the third position and display it again.

my_tuple = (1, 2, 3, 4, 5)

print("Original Tuple:", my_tuple)

my_list = list(my_tuple)
n = int(input('Enter an postion to insert : '))

my_list[n] = int(input('Enter an element to insert : '))
my_tuple = tuple(my_list)
print("Modified Tuple:", my_tuple)
