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


 
