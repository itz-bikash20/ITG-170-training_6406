# Assignment Tasks
# Create a list of 5 fruits and print:
# First fruit
# Last fruit

fruits = ["Apple","Banana","PineApple","Mango","Grapes"] 
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


Create a list of numbers from 1 to 10 using list comprehension.

num = [i for i in range(1,11) ]
print(num)

From the list below, filter only numbers greater than 5:
[2,5,7,1,9,3,10]

numbers = [2,5,7,1,9,3,10]
ans = [i for i in numbers if i > 5]
print(ans)

Create a dictionary storing:
Name
Age
Course
Print all keys and values.

d = {"Name": "John", "Age": 25, "Course": "Python"}
for k ,v in d.items():
    print(k,v)


Create a dictionary comprehension to store squares of numbers from 1–5.

d = {i: i*i for i in range(1,6)}
print(d)

Create a list of 5 favorite movies and print them using a loop.
Add a new movie to the list and remove one movie.

movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
for movie in movies:
    print(movie)

movies.append("The Lord of the Rings")
movies.remove("Pulp Fiction")

print(movies)


Create a dictionary of a product: name, price, quantity
Calculate total cost.

product = {"name": "Laptop", "price": 1000, "quantity": 2}
cost = product["price"] * product["quantity"]
print("Total cost:", cost)

Use list comprehension to create a list of odd numbers from 1–20.

odd = [i for i in range(1,21) if i%2 != 0]
print(odd)

From a list of names, filter names longer than 4 letters.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
long_names = [name for name in names if len(name) > 4]
print(long_names)