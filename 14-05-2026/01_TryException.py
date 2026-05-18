# 1. Write a program to handle exceptions with Try-Except Block.

try:

    with open("read.txt","r") as file:
        print(file.read())

except FileNotFoundError as e:
    print("Error caught: File not found")
