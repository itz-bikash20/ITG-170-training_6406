# # CALCULATING THE STUDENT GRADES 
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
students = int(input("Enter number of students: "))
for i in range(students):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    grade = calculate_grade(marks)
    print("Student:", name)
    print("Grade:", grade)
    print("-------------------")



# FINDING ELIGIBILITY FOR VOTES
print("Welcome to the voting eligibility system 2026")
gender=input("Enter your gender (Female/Male): ")
candidate_age=int(input("Enter the age: "))
if candidate_age>=18:
    print("You are eligible for the voting")
else:
    print("Sorry! You are not eligible for voting")




# Finding the name in the existing data
admin_list=["aashy","sri ram","vamsi","geethika","hema"]
name=input("Enter your name to check whether you are in the list or not: ")
for i in range(len(admin_list)):
    if admin_list[i]==name:
        print("You are in the list")
    else:
        print("Sorry! You are not in the list")


# Reversing the string without using reverse function

s = input("Enter the string: ")
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")