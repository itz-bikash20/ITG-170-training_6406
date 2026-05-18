# 1. Print your details

print("Name: Rahul")
print("City: Hyderabad")
print("Date: 08-05-2026")
print("Favourite Food: Biryani")
print("Favourite Color: Blue")

# 2. Store details in variables and print

name = "Rahul"
city = "Hyderabad"
date = "08-05-2026"
favourite = "Cricket"

print(f"My name is {name}")
print(f"I live in {city}")
print(f"Today's date is {date}")
print(f"My favourite thing is {favourite}")


# 3. Calculator Program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Division =", num1 / num2)


# 4. Different types of strings

single_quote = 'Hello'
double_quote = "Python"
triple_quote = """This is
a multi-line
string"""

print(single_quote)
print(double_quote)
print(triple_quote)

# 5. Compare two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

# 6. Introduction paragraph using multi-line string

intro = """
Hello!
My name is Rahul.
I am learning Python programming.
I enjoy coding and solving problems.
"""

print(intro)


# 7. Book bill calculation

price = 250
quantity = 3
total_cost = price * quantity

print(f"Book Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ₹{total_cost}")


# 8. Calculate age from birth year

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("Your age is:", age)

# 9. String operations on name

user_name = input("Enter your name: ")

print("Uppercase:", user_name.upper())
print("Lowercase:", user_name.lower())
print("Length:", len(user_name))

# 10. Celsius to Fahrenheit conversion

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
