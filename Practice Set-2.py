#  1) write a python program to find area of triangle

b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b * h / 2

print("area = ", area)

---------------------------------------------------------------

# 2) write a python program to find area of square


s=float(input("Enter side of square : " ))

area=s*s

print("Area of square=", area)

---------------------------------------------------------------

# 3) write a python program to calculate celsius to fahrenheit

celsius=float(input("Enter  of Celsius: " ))

fahrenheit = (celsius  * 9/5) + 32

print("calculate celsius to fahrenheit = ", fahrenheit)

---------------------------------------------------------------

# 4) write a python program to convert us dollars to indian rupees

dollars = float(input("Please enter dollars:"))
rupees = dollars * 82.88

print('convert us dollars to indian rupees',  rupees)

---------------------------------------------------------------

# 5) write a python program to convert litres to millilitres

litres = float(input("Enter the volume in litres: "))


millilitres = litres * 1000

print('convert liters to millilitres', millilitres)

---------------------------------------------------------------

# 6) enter binary octal and hexadecimal value and convert into decimal in python

binary_value = "101"
octal_value = "10"
hexadecimal_value = "2A"

binary = int(binary_value, 2)
octal = int(octal_value, 8)
hexadecimal = int(hexadecimal_value, 16)

print("Binary:", binary_value, "in Decimal:", binary)
print("Octal:", octal_value, "in Decimal:", octal)
print("Hexadecimal:", hexadecimal_value, "in Decimal:",hexadecimal)

---------------------------------------------------------------

# 7) Accept one integer value from the user; convert it to binary, octal and hexadecimal.
# Accept string from the user (‘The Rajkot is a good city to leave’), and do the following

int_value = int(input("Enter an integer: "))

binary_value = bin(int_value)
octal_value = oct(int_value)
hexaint_value = hex(int_value)

print("Binary:", binary_value)
print("Octal:", octal_value)
print("Hexadecimal:", hexaint_value)

---------------------------------------------------------------

# 8) Accept string from the user (‘The Rajkot is a good city to leave’), and do the following
# operations: i). Display the first character of the string, ii). Display the first character of the string
# using negative index, ii). Display ‘Rajkot is a good city’. iv) Display the last characte

str = input("Enter a string: ")

print("---------- Display the first character of the string --------\n")
print(str[0])

print("-------------Display the first character of the string using negative index--------------\n")
print(str[-34])

print("----------- Display Rajkot is a good city -----------\n")
print(str[4:25])

print("\n----------- Display the last character in -----------\n")
print(str[33])

---------------------------------------------------------------

# 9) Accept values of bytes from user and display all elements.

byte_input = [1,2,3,4,5]
byte_list = bytes(byte_input)
print(byte_list[0:5])

# byte_values_str = input("Enter byte values separated by spaces: ")
# byte_values_list = [int(value) for value in byte_values_str.split()]

# print("Byte values entered by the user:")

# print(byte_values_list)

---------------------------------------------------------------

# 10) Accept values of bytearray from user: i). Replace the 3" element with 7, ii). Display the 5" element.

byte_value = [2,5,9,10,3,6,4]

b = bytearray(byte_value)
print("Original Byte Array : ", b)

# Replacing the 3rd element  with 7
b[2] = 7
print("\nModified Byte Array after replacing 3rd element with 7 :", b)

# Display the 5" element
print("\nDisplay the 5 element : ",b[4])

---------------------------------------------------------------
# 11) Accept elements of list from the user. i).Display all the elements. ii). Display the the 3th element,
# iii). Replace the 4» element with ‘Atmiya’, iv). Display elements from 3 to 7 element.

list_value = [2,3,4,6,'a',-255,'rahul',10,'b']

# i).Display all the elements.

print("Display all the elements :",list_value,"\n")

# Display the the 3th element

print("Display the the 3th element :",list_value[2],"\n")

# Replace the 4» element with ‘Atmiya’

list_value[3]='Atmiya'
print("After Replacing the 4th Element:",list_value,"\n")

# Display elements from 3 to 7 element.

print("Display elements from 3 to 7 element :",list_value[2:6])


---------------------------------------------------------------

# 12) Take elements of tuple from the user. i). Try to replace the 3 element with 9, ii). Display the 5 element.

tuple_value = (2,3,4,6,'a',-255,'rahul',10,'b')

# Try to replace the 3 element with 9

# tuple_value[2]=9
# print("After Replacing the 3th Element:",tuple_value,"\n")  #can not modified tuple value
# TypeError: 'tuple' object does not support item assignment

# Display the 5th element

print("Display the 5 element : ",tuple_value[4])

---------------------------------------------------------------

# 13) Create a set insert some values. i). Add elements to it and display, ii). Remove elements from it
# and display.

# set_value = input("enter list value in round brackets :  ")
set_value = {2,3,4,6,'a',-255,'rahul'}

#  Add elements to it and display
set_value.update([10])
print(set_value)

# Remove elements from it and display

set_value.remove(2)
print(set_value)

---------------------------------------------------------------

# 14) Create a set insert some values and convert it to frozenset. Try to add and remove some
# elements.

set_value = {1,2,3,4,'a'}
print(set_value)

fs = frozenset(set_value)
print(fs)
---------------------------------------------------------------

# 15) Create an empty dictionary, Insert some Roll:Name into it. i). Retrieve 5th value using key, ii).
# Retrieve all the roll numbers, iii). Retrieve all the names, iv). Change the name of the student
# having roll no. 7, v). Remove roll no 9, vi). Display the dictionary.

s_dict = {}

print(s_dict)

# Insert some Roll:Name into it

s_dict = {
    1 : 'rahul',
    2 : 'jay',
    3 : 'dhaval',
    4 : 'mahaveer',
    5 : 'raj',
    6 : 'parash',
    7 : 'mukesh',
    8 : 'mehul',
    9 : 'vijay',
    10 : 'yash'
}

# i). Retrieve 5th value using key

print(s_dict[5])

# ii). Retrieve all the roll numbers

print(s_dict.keys())

# iii). Retrieve all the names

print (s_dict.values())

# iv). Change the name of the student having roll no. 7

s_dict[7] = 'ajay'
print(s_dict)

# v). Remove roll no 9

del s_dict[9]

# vi). Display the dictionary
print(s_dict)

---------------------------------------------------------------

# 16. Create a list having names of months. i). Check whether December is in list or not, 
#ii). Query the list using ‘not in’.

months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#  Check whether December is in list or not,

check_december = "December" in months_list
print(" Is December in the list? : ", check_december)

# Query the list using ‘not in’.

months_not = [month for month in months_list if "January" not in month]

print("Months not containing 'January':", months_not)

---------------------------------------------------------------

# Take two integer values from the user using split(), perform basic arithmetic operation on the
 # values.

n1,n2 = [int(no) for no in input('Enter two integer value by giving space : ').split()]
print('----------------------------------------------')
print('The Addition of two number is : ',n1 + n2,'\n')
print('The Subtraction of two number is : ',n1 - n2,'\n')
print('The Multiplication of two number is : ',n1 * n2,'\n')
print('The Division of two number is : ',n1 / n2,'\n')
---------------------------------------------------------------


 
