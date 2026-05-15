# *****************************************************
# Miracle Python Training - Day 2
# Employee Name : Geetha Gangabattula
# Topic : Python Basics and Intermediate Programs
# Status : Completed
# *****************************************************

import datetime


# ================= PROGRAM 1 =================
# Personal Details Program

print("\n------ Personal Details Program ------")

name = input("Enter Your Name : ")
city = input("Enter Your City : ")
fav_food = input("Enter Favorite Food : ")
fav_color = input("Enter Favorite Color : ")
fav_hobby = input("Enter Favorite Hobby : ")

today = datetime.date.today()

print("\nYour Name        :", name)
print("Your City        :", city)
print("Today's Date     :", today)
print("Favorite Food    :", fav_food)
print("Favorite Color   :", fav_color)
print("Favorite Hobby   :", fav_hobby)



# ================= PROGRAM 2 =================
# Calculator Program

print("\n------ Calculator Program ------")

a = float(input("Enter First Number  : "))
b = float(input("Enter Second Number : "))

print("\nSum        :", a + b)
print("Difference :", a - b)
print("Product    :", a * b)

if b != 0:
    print("Division   :", a / b)
else:
    print("Division   : Undefined")



# ================= PROGRAM 3 =================
# String Creation Program

print("\n------ String Creation Program ------")

s1 = 'This is Single Quote String'

s2 = "This is Double Quote String"

s3 = """This is
Triple Quote
String"""

print("\nSingle Quote String :")
print(s1)

print("\nDouble Quote String :")
print(s2)

print("\nTriple Quote String :")
print(s3)



# ================= PROGRAM 4 =================
# Compare Two Numbers Program

print("\n------ Compare Two Numbers ------")

x = float(input("Enter First Number  : "))
y = float(input("Enter Second Number : "))

if x > y:

    print(x, "is Greater than", y)

elif y > x:

    print(y, "is Greater than", x)

else:

    print("Both Numbers are Equal")



# ================= PROGRAM 5 =================
# Introduction Paragraph Program

print("\n------ Introduction Paragraph ------")

intro = """
Hello,
My name is Geetha Gangabattula.

I am learning Python Programming.
I enjoy coding and building projects.
I want to become a Full Stack Developer.
"""

print(intro)



# ================= PROGRAM 6 =================
# Book Bill Program

print("\n------ Book Bill Program ------")

price = float(input("Enter Book Price : "))
quantity = int(input("Enter Quantity   : "))

total = price * quantity

print("\nBook Price :", price)
print("Quantity   :", quantity)
print("Total Cost :", total)



# ================= PROGRAM 7 =================
# Age Calculator Program

print("\n------ Age Calculator Program ------")

birth_year = int(input("Enter Birth Year : "))

current_year = datetime.date.today().year

age = current_year - birth_year

print("Your Age is :", age)



# ================= PROGRAM 8 =================
# Name Transformation Program

print("\n------ Name Transformation Program ------")

user_name = input("Enter Your Name : ")

print("\nUppercase Name :", user_name.upper())

print("Lowercase Name :", user_name.lower())

print("Length of Name :", len(user_name))



# ================= PROGRAM 9 =================
# Temperature Conversion Program

print("\n------ Temperature Conversion ------")

celsius = float(input("Enter Temperature in Celsius : "))

fahrenheit = (celsius * 9 / 5) + 32

print("\nTemperature in Fahrenheit :", fahrenheit)



# ================= END =================

print("\nPython Day 1 Tasks Completed Successfully")

print("Employee Name : Geetha Gangabattula")

print("Company Name  : Miracle")