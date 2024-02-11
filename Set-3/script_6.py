# Accept two integer values in separate variable, display the small value and big value out of it.

# Accept two integer values from the user
num1 = int(input("Enter the first integer value: "))
num2 = int(input("Enter the second integer value: "))

if num1 < num2:
    print("Smaller value:", num1)
    print("Larger value:", num2)
elif num1 > num2:
    print("Smaller value:", num2)
    print("Larger value:", num1)
else:
    print("Both values are equal:", num1)
