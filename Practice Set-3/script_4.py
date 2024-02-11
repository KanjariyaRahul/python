
marks = float(input("Enter the marks scored by the student: "))

if marks > 90:
    print("A1 Grade")
elif marks <= 90 and marks > 80:
    print("A Grade")
elif marks <= 80 and marks > 70:
    print("B1 Grade")
    
elif marks <= 70 and marks > 60:
    print("B Grade")
    
elif marks <= 60 and marks > 50:
    print("Can do Better!")
else:
    print("Need to work hard.")

