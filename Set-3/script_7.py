marks1 = float(input("Enter marks for student 1: "))
marks2 = float(input("Enter marks for student 2: "))
marks3 = float(input("Enter marks for student 3: "))
marks4 = float(input("Enter marks for student 4: "))


if marks1 >= marks2 and marks1 >= marks3 and marks1 >= marks4:
    print("student  1 is the highest scorer with", marks1, "marks.")
elif marks2 >= marks1 and marks2 >= marks3 and marks2 >= marks4:
    print("student  2 is the highest scorer with", marks2, "marks.")
elif marks3 >= marks1 and marks3 >= marks2 and marks3 >= marks4:
    print("student  3 is the highest scorer with", marks3, "marks.")
else:
    print("student  4 is the highest scorer with", marks4, "marks.")


