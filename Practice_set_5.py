
Practice set 5


# 1) Create a list containing several strings. Take input from the user (search string); display whether
# entered string is available in the list or not.


string_list = ["apple", "banana", "orange", "grape", "kiwi"]


search_string = input("Enter a string to search in the list: \n")


if search_string in string_list:
    print("The entered string is available in the list.")
else:
    print("The entered string is not available in the list.")


# =======================================================================


# 2) Accept the string from the user; display the message whether the entered string is palindrom or not.


str = input("Enter a string : ")


str = str.lower().replace(" " , "")


if str  == str[::-1] :
    print("\n The entered string is a palindrome.")
else:
    print(" \n The entered string is not a palindrome.")


# =======================================================================


#3) Accept the string from the user; display the string in the reverse order.


str = input("Enter a string : ")


display  = str[:: -1]
print ("The string in reverse order  is : ", display)


# =======================================================================


# 4) Accept the string from the user; allow user to choose from the following options and perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title case


Take input from the user
string = input("Enter a string : ")
 


print("Choose an option : ")
print("1. Convert to upper case")
print("2. Convert to lower case")
print("3. Convert to swap case")
print("4. Convert to title case")


choice = input("Enter your choice (1/2/3/4): ")


if choice == '1':
    result = string.upper()
elif choice == '2':
    result = string.lower()
elif choice == '3':
    result = string.swapcase()
elif choice == '4':
    result = string.title()
else:
    print("Invalid choice")
    exit()
print("Result:", result)


# =======================================================================


# 5) Allow users to enter multiple strings in the list; arrange the entered string into alphabetical
# order and display.


string = []


n = int(input('How many string you want to enter ? :'))
for i in range(n):
    print("Enter the string  : ",end = '')
    string.append(input())
print(string)
arrange = string.sort()
print('======== arrange the entered string into alphabetical order ========= ')
for i  in string :
        print(i)


# =======================================================================


# 6) Create a tuple and display it. Enter 25 at the third position and display it again.


my_tuple = (1, 2, 3, 4, 5)


print("Original Tuple:", my_tuple)


my_list = list(my_tuple)
n = int(input('Enter an position to insert : '))


my_list[n] = int(input('Enter an element to insert : '))
my_tuple = tuple(my_list)
print("Modified Tuple:", my_tuple)


# =======================================================================


# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key
# and display the dictionary again.


dic = {"bookid" : 1,"title" : "Lipika","author" : "Rabindranath Tagore","price" : 200, "publisher": "Penguin Books"}
print("Display the dictionary\n",dic)
print("---------------------------------------------------------")
print("Display the name of Author\n",dic["author"])
print("---------------------------------------------------------")
print("Display the Bookid\n",dic["bookid"])
print("---------------------------------------------------------")
print("Display the length of the dictionary\n",len(dic))
print("---------------------------------------------------------")
print("Update the price\n")
print("Price before updating :",dic["price"])
dic["price"]=500
print("price after updating : ",dic["price"])
print("---------------------------------------------------------")
print("Insert year as the new key\n")
dic["year"] = "2020"
print(dic)


# =======================================================================


# 8. Create a numeric array and perform following operations on it: Add 2 to each elements,
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find
# max and min, find the average of all elements.


from numpy import *
arr = array([10,20,30,40])
print("Array :",arr)
print("-----------------------------------")
print("Add 2 to each elements :")
for i in range(len(arr)):
    arr[i] = arr[i] + 2
print(arr)
print("-----------------------------------")
print("Subtract 3 from each element :")
for i in range(len(arr)):
    arr[i] = arr[i]-3
print(arr)
print("-----------------------------------")
print("Multiply each element with 3 :")
for i in range(len(arr)):
    arr[i] = arr[i]*3
print(arr)
print("-----------------------------------")
print("Divide each element by 2")
for i in range(len(arr)):
    arr[i] = arr[i]/2
print(arr)
print("-----------------------------------")
print("Find max and min :")
print("Maximum value in array :",max(arr))
print("Minimum value in array :",min(arr))
print("-----------------------------------")
print("find the average of all elements")
print("Average of all elements :",average(arr))


# =======================================================================




# 9. Create a numeric array and do the following: append the element, pop the element, insert an
# element at the desired position, reverse the elements in the array, convert the array to list.


from array import *
arr = array('i',[10,20,30,40])
print("Array :\n",arr)
print("-----------------------------------------")
print("Append the element : ")
arr.append(100)
print(arr)
print("-----------------------------------------")
print("Pop the element : ")
print("Pop the element :")
arr.pop()
print(arr)
print("-----------------------------------------")
print("Insert an element at the desired position")
arr.insert(2,500)
print(arr)
print("-----------------------------------------")
print("Reverse the elements in the array")
print(arr,arr.reverse())
print("-----------------------------------------")
print("Convert the array to list")
lst=list(arr)
print(lst)




# =======================================================================


# 10. Accept numeric elements from the user, store it to the array and display. Ask user to enter
# search element. Display the position of the searched element.


from array import *
no = int(input("How many elements you want to enter? "))
arr = array('i',[])
for i in range(no):
    item = int(input("Enter {} element :".format(i+1)))
    arr.append(item)
print("Array :\n",arr)
print("--------------------------------------------")
search = int(input("Search Element : "))
print("Position of  the searched element is: ",arr.index(search))


# =======================================================================


# 11. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each
# array and display only the bigger number.


from array import *
a = array('i', []);
b = array('i', []);
print("Enter 1st Array's Elements :")
for i in range(5):
    item = int(input("Enter Element {} :".format(i+1)))
    a.append(item)
print("Array 1 :\n",a)
print("-------------------------------------------")
print("Enter 2nd Array's Elements :")
for i in range(5):
    item = int(input("Enter Element {} :".format(i+1)))
    b.append(item)
print("Array 2 :\n",b)
print("-------------------------------------------")
print("Maximum Number Array")
print(max(a,b))


# =======================================================================


# 12. Accept dimension of the array and its values from the user, create an array as desired.


from array import *
no = int(input("How many elements You want to enter ? "))
arr = array('i',[])
for i in range(no):
    arr.append(i)
arr2 = array('i',[])
a = len(arr)+1
arr2.append(a)
for i in range(no):
    item = int(input("Enter Index Number of the Array :"))
    for x in range(len(arr2)):
        if item==arr2[x]:
            print("Please enter valid index no.")
            item = int(input("Enter Index Number of the Array :"))
        else:
            arr2.append(item)
           
    if item>len(arr)-1:
        print("Please enter valid index no.")
        item = int(input("Enter Index Number of the Array :"))
    else:
        val = int(input("Enter Value of arr[{}] : ".format(item)))
        arr[item] = val


print(arr)


# =======================================================================


# 13. Create a function to calculate the simple interest.


def cal(amount,rate):
    print("Interest :",amount*rate/100)


amount = int(input("Enter Amount : "))
rate = int(input("Enter rate : "))
cal(amount,rate)


# =======================================================================


# 14. Create a function to perform basic arithmetic operations on the number.


def cal(val1,val2):
    print("Sum of {} + {} = {}".format(val1,val2,val1+val2))
    print("Subtraction of {} - {} = {}".format(val1,val2,val1-val2))
    print("Multiplication of {} X {} = {}".format(val1,val2,val1*val2))
    print("Division of {} / {} = {}".format(val1,val2,val1/val2))


a = int(input("Enter Value 1 :"))
b = int(input("Enter Value 2 :"))
print("--------------------------------------")
cal(a,b)


# =======================================================================


# 15. Accept multiple strings and store it into the list using function.


lst = []
def insert(val):
    for i in range(no):
        item = input("Enter String {} : ".format(i+1))
        lst.append(item)
    print("List :\n",lst)
   
no = int(input("How many strings you want to enter? "))
insert(no)


# =======================================================================


# 16. Find the biggest number from three values using lambda.


val = lambda a,b,c : max(a,b,c);
print("Biggest  Number : ",val(10,20,5))


# =======================================================================


# 17. Demonstrate the use of: i). break and ii). pass.


num = 5
print("Break :")
for i in range(num):
    if i==3:
        break
    else:
        print(i)
   
print("Pass :")
for i in range(num):
    if i==4:
        pass
    print(i)


# =======================================================================
