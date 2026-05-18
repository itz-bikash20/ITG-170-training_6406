

# 1. Positive or Negative Number
n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 2. Student Pass or Fail with Rank
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Passed")
    if marks >= 90:
        print("First Rank")
    elif marks >= 75:
        print("Second Rank")
    else:
        print("Third Rank")
else:
    print("Failed")


# 3. Check Character Type
ch = input("Enter character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")


# 4. Biggest Among Two Numbers
a = int(input())
b = int(input())
if a > b:
    print(a, "is biggest")
else:
    print(b, "is biggest")

# 5. Squares up to 20
for i in range(1, 21):
    print(i * i)

# 6. Print n Even Numbers
n = int(input())
for i in range(1, n + 1):
    print(i * 2)

# 7. Sum of Even Numbers from 1 to n
n = int(input())
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)

# 8. Prime Numbers from 1 to 10
for n in range(2, 11):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime:
        print(n)


# 9. Squares up to 20
for i in range(1, 21):
    print(i ** 2)


# 10. Factorial of n
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# 11. Perfect Number
n = int(input())
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

# 12. Fibonacci Series
n = int(input())

a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# 13. Biggest Digit in a Number
n = int(input())
big = 0
while n > 0:
    digit = n % 10
    if digit > big:
        big = digit
    n //= 10
print(big)

# 14. Sum of Digits using Recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
n = int(input())
print(sum_digits(n))

# 15. Sum of Alternative Digits
n = input()
sum = 0
for i in range(0, len(n), 2):
    sum += int(n[i])
print(sum)

# 16. Occurrences of a Digit
n = input()
digit = input()
print(n.count(digit))

# 17. All Digits Equal or Not
n = input()
if n.count(n[0]) == len(n):
    print("All digits are equal")
else:
    print("Not equal")

# 18. Add First and Last Digit
n = input()
first = int(n[0])
last = int(n[-1])
print(first + last)

# 19. Add Even and Odd Digits
n = input()
even = 0
odd = 0
for i in n:
    if int(i) % 2 == 0:
        even += int(i)
    else:
        odd += int(i)
print("Even sum:", even)
print("Odd sum:", odd)


# 20. Reverse a Number
n = input()
print(n[::-1])

#21 Prime numbers between m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
for num in range(m, n + 1):    
    if num > 1:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

#22 n Prime numbers 
n = int(input("Enter n value: "))
for num in range(n + 1):    
    if num > 1:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

#23Print perfect numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
for num in range(m, n + 1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)

#24Program to print n perfect numbers.
n = int(input("Enter n value: "))
count = 0
num = 1
while count < n:
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)
        count += 1
    num += 1

#25 Program to Print Armstrong Numbers Between 1 to 1000
for num in range(1, 1001):
    power = len(str(num))
    total = 0
    for digit in str(num):
        total += int(digit) ** power
    if total == num:
        print(num)

#26 Program to Find Sum of Natural Numbers.
n=int(input("ENter the numbers"))
Sum=0
for i in range(n+1):
    Sum+=i
print(Sum)

#27 program to find to copy the elements in the array
arr1 = [1, 2, 3, 4, 5]
arr2 = []
for i in arr1:
    arr2.append(i)
print(arr2)

#28 Find the frequency of each element in the array
arr = [1, 2, 2, 3, 4, 3, 2]
freq = {}
for i in arr:
    
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#29 Print duplicate elements of an array
arr = [1, 2, 3, 2, 4, 5, 1]
freq = {}
duplicates = []
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    if value > 1:
        duplicates.append(key)
print(duplicates)

#30 Print the elements of an array in reverse order without sorting
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

#31. Find Largest Number and Smallest Number in an Array
arr = [10, 20, 5, 40, 2]
largest = max(arr)
smallest = min(arr)
print("Largest =", largest)
print("Smallest =", smallest)

#32. Sort the elements of an array in descending order
arr = [10, 20, 5, 40, 2]
arr.sort()
for i in range(len(arr)-1,-1,-1):
    print(arr[i])

#33. Print the sum of all the items of the array
arr = [1, 2, 3, 4, 5]
total = sum(arr)
print("Sum =", total)

#34. Print Odd and Even Numbers from an Array
arr = [1, 2, 3, 4, 5, 6]
print("Even Numbers:")
for i in arr:
    if i % 2 == 0:
        print(i)
print("Odd Numbers:")
for i in arr:
    if i % 2 != 0:
        print(i)

#36 Program to Find the Sum of the Series 1/1+1/2+1/3+…1/N.
n = 5
total = 0
for i in range(1, n + 1):
    total += 1 / i
print("Sum =", total)

#37 Program to Find the Sum of the Series 1/1+1/2^2+1/3^2+1/4^2+1/5^2.
n = 5
total = 0
for i in range(1, n + 1):
    total += 1 / (i*i)
print("Sum =", total)

#38 Program to Find the Sum of the Series 1/1^0+1/2^1+1/3^2+1/4^3+1/5^4.
n = 5
total = 0
for i in range(1, n + 1):
    total += 1 / (i ** (i - 1))
print("Sum =", total)

#39 Program to Find the Sum of the Series 1/2^0+1/2^1+1/2^2+1/2^3+1/2^4.
n = 5
total = 0
for i in range(n):
    total += 1 / (2 ** i)
print("Sum =", total)

#40 Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = 5
total = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += 1 / fact
print("Sum =", total)

#41 Program to Find the Sum of the Series 1/1+1/4+1/9+…1/N^2
n = 5
total = 0
for i in range(1, n + 1):
    total += 1 / (i ** 2)
print("Sum =", total)

#42 Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
n = 5
total = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += 1 / fact
print("Sum =", total)

#44 How Python Access Modifiers is Useful for Programming in Python?
# 1. Public Access Modifier
# Public members can be accessed anywhere:
# inside the class
# outside the class
# in child classes
# By default, all variables and methods in Python are public.
# 2. Private Access Modifier
# Private members are accessed only inside the class.
# To make something private, use double underscore __.
# 3. Protected Access Modifier
# Protected members are meant to be used:
# inside the class
# inside child classes (inheritance)
# Use a single underscore _.