# 1) Accept two integer values from the user; display the number which is smaller and the number which bigger.

# num1 = int(input("Enter a Number one : "))
# num2 = int(input("Enter a Number two  : "))

# if num1 > num2:
#     print("NUmber 1 : ",num1,"is bigger than Nunber 2 :",num2,"is smaller")
# else:
#     print("NUmber 1 : ",num1,"is smaler than Nunber 1 :",num2,"is bigger")


# 2)Accept one integer value from the user; check whether entered number is divisible by 5 or not.


# num = int(input("Enter interger Number  : "))

# if(num/5 == 0):
#     print(num,"Number Is Divisible By 5");
# else:
#     print(num,"Number Is Not Divisible By 5");

# Accept one integer value from the user; check whether entered number is Between 0-100 or not.

# num = int(input("Enter The NUmber :"))

# if num > 0 and num<=100:
#     print("Enter Number Is Between 0-100")
# else:
#     print("Enter Number Is Not Between 0-100")

# 4) Accept one integer value from the user; display the length of the entered number, also display that the entered number is of four digits or not.

# num = int(input("Enter The Number :"))

# str = str(num)

# length =  len(str)

# if(length == 4):
#     print("Entered Number",num,"Is Four Digit Number")
# else:
#     print("Entered Number",num,"Is Not Four Digit Number")

# 5)  Accept one integer value from the user; display appropriate day of the week.

# week = int(input('Enter Number of Day between 1 and 7 :'))
# if(week < 7):
#     if week == 1:
#         print('Sunday...')
#     if week == 2:
#         print('Monday...')
#     if week == 3:
#         print('Tuesday...')
#     if week == 4:
#         print('Wednesday...')
#     if week == 5:
#         print('Thursday...')
#     if week == 6:
#         print('Friday...')
#     if week == 7:
#         print('Saturday...')
# else:
#     print('please select a number between 1 and 7..')


# 6) take choice from the user ,and perform the arithmetic operation as per the choice.
# 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division

# num1 = int(input('Enter the number of one :'))
# num2 = int(input('Enter the number of two :'))

# operation = input('Enter operation of +,-,*,/ : ')

# if operation == '+':
#     add = num1 + num2
#     print('Addition is : ',add)
# elif operation == '-':
#     sub = num1 - num2
#     print('Subtraction  is : ',sub)
# elif operation == '*':
#     mul = num1 * num2
#     print('Multiplication is : ',mul)
# elif operation == '/':
#     div = num1 / num2
#     print('Division is : ',div)
# else:
#     print('Enter valid choice')

# 7) Accept the string from user;display the count of vowels and consonants.

# string = str.lower(input("Enter the String :"))
# print("======================================")
# vowel = 0
# consonants = 0
# space = 0


# for s in string:
#     if s=='a' or s=='e' or s=='i' or s=='o' or s=='u' :
#         vowel = vowel+1
#     elif s==' ':
#         space += 1
#     else:
#         consonants = consonants +1

# print("Space in given string :", space)
# print("Vowel in given string :", vowel)
# print("Constant in given string :", consonants)


# 8) Accept one integer value from the user; display the table of it. in python 

# num = int(input("Enter the number to print the tables for:"))
    
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)


# 9)  Display square and cube of number 1-10.

# for i in range(1,11):
#     print("Square of ",i ," : ",i**2,end = "\t")
#     print("Cube of ",i," : ",i**3)

# 10) Accept the string  from user; convert in to upper case

string = (input("Enter the String :"))

convert = (str.upper(string))
print("Convert string in lower case to upper case is : ",convert)


