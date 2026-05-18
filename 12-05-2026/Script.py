# 1. Check whether the number is Positive Negative, or Zero


n = int(input("Enter a number: "))

if n == 0:
    print("Zero")
elif n > 0:
    print("Positive")
else:
    print("Negative")



# 2. Student Grade Program


marks = int(input("Enter marks: "))

if 90 < marks <= 100:
    print("O")
elif 80 < marks <= 90:
    print("A")
elif 70 < marks <= 80:
    print("B")
elif 60 < marks <= 70:
    print("C")
elif 50 < marks <= 60:
    print("D")
elif 35 <= marks <= 50:
    print("E")
else:
    print("Fail")


# 
# 3. Check character type
# 

ch = input("Enter a character: ")

if ch[0].isupper():
    print("Uppercase")
elif ch[0].islower():
    print("Lowercase")
elif ch[0].isdigit():
    print("Digit")
else:
    print("Special Symbol")


# 
# 4. Find biggest among two numbers
# 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Biggest:", a)
else:
    print("Biggest:", b)


# 
# 5. Print squares up to 20
# 

for i in range(1, 21):
    print(i * i)


# 
# 6. Print first n Even numbers
# 

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


# 
# 7. Sum of all even numbers between 1 and n
# 

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum =", total)


# 
# 8. Prime numbers from 1 to 10
# 

for i in range(2, 11):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)


# 
# 9. Print squares up to 20
# 

for i in range(1, 21):
    print(i * i)


# 
# 10. Factorial using Recursion
# 

def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


n = int(input("Enter a number: "))
print("Factorial =", fact(n))


# 
# 11. Perfect Number
# 

n = int(input("Enter a number: "))
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# 
# 12. Fibonacci Series
# 

n = int(input("Enter n: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# 
# 13. Find biggest digit in a number
# 

n = input("Enter a number: ")
max_digit = 0

for digit in n:
    if int(digit) > max_digit:
        max_digit = int(digit)

print("Biggest digit =", max_digit)


# 
# 14. Sum of digits using Recursion
# 

def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


n = int(input("Enter a number: "))
print("Sum of digits =", digit_sum(n))


# 
# 15. Sum of alternative digits
# 

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1, 2):
    total += i

print("Sum =", total)


# 
# 16. Count occurrences of a digit
# 

n = input("Enter a number: ")
d = input("Enter digit to count: ")

count = 0

for i in n:
    if i == d:
        count += 1

print("Occurrences =", count)


# 
# 17. Check whether all digits are equal
# 

n = input("Enter a number: ")

flag = True

for i in n:
    if i != n[0]:
        flag = False
        break

if flag:
    print("All digits are equal")
else:
    print("Digits are not equal")


# 
# 18. Add first and last digit
# 

n = input("Enter a number: ")

total = int(n[0]) + int(n[-1])

print("Sum =", total)


# 
# 19. Sum of even and odd digits
# 

n = input("Enter a number: ")

even_sum = 0
odd_sum = 0

for i in n:
    if int(i) % 2 == 0:
        even_sum += int(i)
    else:
        odd_sum += int(i)

print("Even digit sum =", even_sum)
print("Odd digit sum =", odd_sum)


# 
# 20. Reverse a number
# 

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed number =", rev)


# 
# 21. Prime numbers between m and n
# 

m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

for num in range(m, n + 1):

    if num > 1:
        prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")

print()


# 
# 22. Print first n prime numbers
# 

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


n = int(input("Enter n: "))

count = 0
num = 1

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1

print()


# 
# 23. Perfect numbers between m and n
# 

m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

for num in range(m, n + 1):

    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        print(num)


# 
# 24. Print first n perfect numbers
# 

def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num


n = int(input("Enter n: "))

count = 0
num = 1

while count < n:
    if is_perfect(num):
        print(num)
        count += 1

    num += 1


# 
# 25. Armstrong Numbers from 1 to 1000
# 

def is_armstrong(num):
    power = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num


for i in range(1, 1001):
    if is_armstrong(i):
        print(i)


# 
# 26. Sum of Natural Numbers
# 

n = int(input("Enter n: "))
print("Sum =", (n * (n + 1)) // 2)


# 
# 27. Copy all elements of one array to another
# 

arr1 = [1, 2, 3, 4, 5]
arr2 = arr1.copy()

print("Copied Array:", arr2)


# 
# 28. Frequency of each element in an array
# 

arr = list(map(int, input("Enter array elements: ").split()))
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key, "->", freq[key])


# 
# 29. Print duplicate elements in an array
# 

arr = list(map(int, input("Enter array elements: ").split()))

seen = set()

for i in arr:
    if i in seen:
        print(i)
    else:
        seen.add(i)


# 
# 30. Reverse array without sorting
# 

arr = list(map(int, input("Enter array elements: ").split()))

print("Reversed Array:", arr[::-1])


# 
# 31. Largest and Smallest element in array
# 

arr = list(map(int, input("Enter array elements: ").split()))

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)


# 
# 32. Sort array in descending order
# 

arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):

        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)


# 
# 33. Sum of all elements in array
# 

arr = list(map(int, input("Enter array elements: ").split()))

total = 0

for i in arr:
    total += i

print("Sum =", total)


# 
# 34. Print Odd and Even numbers from array
# 

arr = list(map(int, input("Enter array elements: ").split()))

print("Even Numbers:")
for i in arr:
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd Numbers:")
for i in arr:
    if i % 2 != 0:
        print(i, end=" ")

print()


# 
# 35. Happy Number
# 

def next_num(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10

    return total


def is_happy(n):

    while n != 1 and n != 4:
        n = next_num(n)

    return n == 1


n = int(input("Enter a number: "))

if is_happy(n):
    print("Happy Number")
else:
    print("Not Happy Number")


# 
# 36. Sum of series: 1 + 1/2 + 1/3 + ... + 1/n
# 

n = int(input("Enter n: "))

s = 0

for i in range(1, n + 1):
    s += 1 / i

print("Sum =", s)


# 
# 37. Sum of series: 1/1² + 1/2² + ... + 1/n²
# 

n = int(input("Enter n: "))

s = 0

for i in range(1, n + 1):
    s += 1 / (i * i)

print("Sum =", s)


# 
# 38. Sum of series:
# 1/1^0 + 1/2^1 + 1/3^2 + ... + 1/n^(n-1)
# 

n = int(input("Enter n: "))

s = 0

for i in range(1, n + 1):
    s += 1 / (i ** (i - 1))

print("Sum =", s)


# 
# 39. Sum of series:
# 1/2^0 + 1/2^1 + 1/2^2 + ... + 1/2^n
# 

n = int(input("Enter n: "))

s = 0

for i in range(n + 1):
    s += 1 / (2 ** i)

print("Sum =", s)


# 
# 40. Sum of series:
# 1/1! + 1/2! + 1/3! + ... + 1/n!
# 

n = int(input("Enter n: "))

s = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    s += 1 / fact

print("Sum =", s)


# 
# 41. Sum of series:
# 1/1² + 1/2² + ... + 1/n²
# 

n = int(input("Enter n: "))

s = 0

for i in range(1, n + 1):
    s += 1 / (i * i)

print("Sum =", s)


# 
# 42. Sum of factorial series
# 

n = int(input("Enter n: "))

s = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    s += 1 / fact

print("Sum =", s)


# 
# 43. Star Pyramid Pattern
# 

n = int(input("Enter n: "))

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for k in range(i):
        print("* ", end="")

    print()

# 44. Number Triangle Pattern

n = int(input("Enter n: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

# 45. Floyd’s Triangle Pattern

n = int(input("Enter n: "))

num = 1

for i in range(1, n + 1):

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()