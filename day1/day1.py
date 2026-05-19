# *****************************************************
# Miracle Python Training - Day 1
# Employee Name : Geetha Gangabattula
# Topic : Intermediate Python Programs
# Status : Completed
# *****************************************************


# ================= PROGRAM 1 =================
# Student Result Program

print("\n------ Student Result Program ------")

name = input("Enter Student Name : ")

sub1 = int(input("Enter Python Marks : "))
sub2 = int(input("Enter Java Marks : "))
sub3 = int(input("Enter DBMS Marks : "))

total = sub1 + sub2 + sub3

average = total / 3

print("\nStudent Name :", name)
print("Total Marks  :", total)
print("Average Marks:", average)

if average >= 75:
    print("Result : Distinction")

elif average >= 50:
    print("Result : Pass")

else:
    print("Result : Fail")



# ================= PROGRAM 2 =================
# ATM Withdraw Program

print("\n------ ATM Withdraw Program ------")

balance = 10000

amount = int(input("Enter Withdraw Amount : "))

if amount <= balance:

    balance = balance - amount

    print("Transaction Successful")
    print("Available Balance :", balance)

else:
    print("Insufficient Balance")



# ================= PROGRAM 3 =================
# Login Program

print("\n------ Login Program ------")

username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "geetha" and password == "1234":

    print("Login Successful")

else:

    print("Invalid Username or Password")



# ================= PROGRAM 4 =================
# Multiplication Table

print("\n------ Multiplication Table ------")

number = int(input("Enter a Number : "))

for i in range(1, 11):

    print(number, "x", i, "=", number * i)



# ================= PROGRAM 5 =================
# Even Odd Numbers from 1 to 10

print("\n------ Even and Odd Numbers ------")

for i in range(1, 11):

    if i % 2 == 0:

        print(i, "is Even Number")

    else:

        print(i, "is Odd Number")



# ================= END =================

print("\nDay 1 Python Tasks Completed")
print("Employee Name : Geetha Gangabattula")
print("Company Name  : Miracle")
