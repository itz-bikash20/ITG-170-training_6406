#writing a program that prints our city details like name,city,todays date,favourite things
print("City details")
name=input("Enter your name: ")
city=input("Enter your city: ")
todays_date=int(input("Enter the today's date: "))
favourite_things=input("Enter your favourite things:  ")
print(name)
print(city)
print(todays_date)
print(favourite_things)


# Creating variables to store details
name = "varshitha"
age = 20
city = "Kakinada"
course = "Python Programming"
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print(f"Course : {course}")


#Asking users for two numbers and printing the sum difference product division
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("Sum of the numbers is",n1+n2)
print("Difference between the numbers is ",n1-n2)
print("Product of the numbers is",n1*n2)
print("Division of the numbers is",n1/n2)



#creating the strings using single.double,triple quotes
print('Hello world!')
print("Hello world!")
print('''Hello world!''')


#printing the greater number
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if n1>n2:
    print("n1 is the biggest number")
else:
    print("n2 is the biggest number")


#printing the final bill
book_price = 250
quantity = 4
total_cost = book_price * quantity
print(f"Book Price : ₹{book_price}")
print(f"Quantity   : {quantity}")
print(f"Total Cost : ₹{total_cost}")

# Ask the user to enter their birth year and calculating the age
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"Your age is {age} years.")


#converting the user's name into upper and lower case
name=input("Enter the user name: ")
print(name.lower())
print(name.upper())
print("The length of the user's name is",len(name))


# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")