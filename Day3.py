# ==============================
# PROGRAM FLOW AND ACCESS MODIFIER
# ALL 45 PROGRAMS IN ONE FILE
# ==============================

# 1. Positive or Negative
n = int(input("1.Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 2. Student Pass/Fail and Rank
marks = int(input("\n2.Enter marks: "))
if marks >= 35:
    print("Passed")
    if marks >= 90:
        print("Rank A")
    elif marks >= 75:
        print("Rank B")
    elif marks >= 60:
        print("Rank C")
    else:
        print("Rank D")
else:
    print("Failed")


# 3. Uppercase / Lowercase / Digit / Special Character
ch = input("\n3.Enter character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")


# 4. Biggest Among Two Numbers
a = int(input("\n4.Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is biggest")
else:
    print(b, "is biggest")


# 5. Square of Numbers up to 20
print("\n5.Squares up to 20")
for i in range(1, 21):
    print(i, "=", i*i)


# 6. Print n Even Numbers
n = int(input("\n6.Enter n: "))
for i in range(1, n+1):
    print(i*2)


# 7. Sum of Even Numbers
n = int(input("\n7.Enter n: "))
s = 0

for i in range(2, n+1, 2):
    s += i

print("Sum =", s)


# 8. Prime Numbers 1 to 10
print("\n8.Prime numbers from 1 to 10")
for n in range(2, 11):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False

    if prime:
        print(n)


# 9. Square of Numbers up to 20
print("\n9.Squares")
for i in range(1, 21):
    print(i**2)


# 10. Factorial
n = int(input("\n10.Enter number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)


# 11. Perfect Number
n = int(input("\n11.Enter number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# 12. Fibonacci Series
n = int(input("\n12.Enter n: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a+b

print()


# 13. Biggest Digit
n = input("\n13.Enter number: ")
print("Biggest digit =", max(n))


# 14. Sum of Digits using Recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

n = int(input("\n14.Enter number: "))
print(sum_digits(n))


# 15. Sum of Alternative Digits
n = input("\n15.Enter number: ")
s = 0

for i in range(0, len(n), 2):
    s += int(n[i])

print("Sum =", s)


# 16. Occurrences of Digit
n = input("\n16.Enter number: ")
digit = input("Enter digit to search: ")

print(n.count(digit))


# 17. All Digits Equal
n = input("\n17.Enter number: ")

if n.count(n[0]) == len(n):
    print("All digits equal")
else:
    print("Not equal")


# 18. Add First and Last Digit
n = input("\n18.Enter number: ")
print(int(n[0]) + int(n[-1]))


# 19. Add Even and Odd Digits
n = input("\n19.Enter number: ")
even = 0
odd = 0

for i in n:
    if int(i) % 2 == 0:
        even += int(i)
    else:
        odd += int(i)

print("Even sum =", even)
print("Odd sum =", odd)


# 20. Reverse a Number
n = input("\n20.Enter number: ")
print(n[::-1])


# 21. Prime Numbers Between m and n
m = int(input("\n21.Enter m: "))
n = int(input("Enter n: "))

for num in range(m, n+1):
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False

        if prime:
            print(num)


# 22. Print n Prime Numbers
n = int(input("\n22.Enter n: "))
count = 0
num = 2

while count < n:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False

    if prime:
        print(num)
        count += 1

    num += 1


# 23. Perfect Numbers Between m and n
m = int(input("\n23.Enter m: "))
n = int(input("Enter n: "))

for num in range(m, n+1):
    s = 0

    for i in range(1, num):
        if num % i == 0:
            s += i

    if s == num:
        print(num)


# 24. Print n Perfect Numbers
count = 0
num = 1

print("\n24.Perfect numbers")
while count < 3:
    s = 0

    for i in range(1, num):
        if num % i == 0:
            s += i

    if s == num:
        print(num)
        count += 1

    num += 1


# 25. Armstrong Numbers
print("\n25.Armstrong numbers")
for num in range(1, 1001):
    s = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10

    if s == num:
        print(num)


# 26. Sum of Natural Numbers
n = int(input("\n26.Enter n: "))
print(n * (n + 1) // 2)


# 27. Copy Array
a = [1, 2, 3, 4]
b = a.copy()

print("\n27.Copy array")
print(b)


# 28. Frequency of Elements
a = [1, 2, 2, 3, 1, 4]

print("\n28.Frequency")
for i in a:
    print(i, "=", a.count(i))


# 29. Duplicate Elements
a = [1, 2, 2, 3, 4, 4]

print("\n29.Duplicate elements")
for i in a:
    if a.count(i) > 1:
        print(i)


# 30. Reverse Array
a = [1, 2, 3, 4]

print("\n30.Reverse array")
print(a[::-1])


# 31. Largest and Smallest
a = [10, 20, 5, 40]

print("\n31.Largest =", max(a))
print("Smallest =", min(a))


# 32. Sort Descending
a = [4, 2, 8, 1]

a.sort(reverse=True)

print("\n32.Descending order")
print(a)


# 33. Sum of Array
a = [1, 2, 3, 4]

print("\n33.Sum =", sum(a))


# 34. Odd and Even in Array
a = [1, 2, 3, 4, 5]

print("\n34.Odd and Even")
for i in a:
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


# 35. Happy Number
n = int(input("\n35.Enter number: "))

while n != 1 and n != 4:
    s = 0

    while n > 0:
        digit = n % 10
        s += digit * digit
        n //= 10

    n = s

if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")


# 36. Sum of Series
n = int(input("\n36.Enter n: "))
s = 0

for i in range(1, n+1):
    s += 1/i

print(s)


# 37. Sum of Series Squares
n = int(input("\n37.Enter n: "))
s = 0

for i in range(1, n+1):
    s += 1/(i*i)

print(s)


# 38. Sum of Series
n = int(input("\n38.Enter n: "))
s = 0

for i in range(n):
    s += 1 / ((i+1) ** i)

print(s)


# 39. Sum of Series Powers
n = int(input("\n39.Enter n: "))
s = 0

for i in range(n):
    s += 1 / (2 ** i)

print(s)


# 40. Sum of Factorial Series
import math

n = int(input("\n40.Enter n: "))
s = 0

for i in range(1, n+1):
    s += 1 / math.factorial(i)

print(s)


# 41. Sum of Series
n = int(input("\n41.Enter n: "))
s = 0

for i in range(1, n+1):
    s += 1/(i*i)

print(s)


# 42. Sum of Factorial Series
n = int(input("\n42.Enter n: "))
s = 0

for i in range(1, n+1):
    s += 1/math.factorial(i)

print(s)


# 43. Patterns

print("\n43.Patterns")

# Pattern 1
for i in range(1, 6):
    print("* " * i)

# Pattern 2
for i in range(1, 6, 2):
    print("*" * i)

# Pattern 3
for i in range(1, 6):
    print(i * "*")

# Pattern 4
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern 5
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Pattern 6
for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()

# Pattern 7
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Pattern 8
for i in range(1, 6):
    print("10" * i)

# Pattern 9
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

# Pattern 10
for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()

# Pattern 11
for i in range(1, 5):
    print("*".join(str(x) for x in range(1, i+1)))

# Pattern 12
for i in range(65, 72):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()


# 44. Access Modifiers

print("\n44.Access Modifiers")

class Student:

    # Public
    name = "Geetha"

    # Protected
    _branch = "CSE"

    # Private
    __marks = 90

    def display(self):
        print("Name:", self.name)
        print("Branch:", self._branch)
        print("Marks:", self.__marks)

obj = Student()

print(obj.name)
print(obj._branch)

obj.display()


# 45. Multiple Classes

print("\n45.Multiple Classes")

class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

obj1 = A()
obj2 = B()

obj1.showA()
obj2.showB()