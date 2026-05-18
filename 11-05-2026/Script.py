1Program to take the number at runtime and check whether the given number
is positive or negative

n = int(input())
if n == 0:
    print("Zero")
if n > 0:
    print("Positive")
else:
    print("Negative")


2. Check whether the student passed or failed and if he passed print which rank
obtained.

marks = int(input())
if marks > 90 and marks <= 100:
    print("O")
elif marks > 80 and marks <= 90:
    print("A")
elif marks > 70 and marks <= 80:
    print("B")
elif marks > 60 and marks <= 70:
    print("C")
elif marks > 40 and marks <= 50:
    print("D")
elif marks >=35 and marks <= 40:
    print("E")
else:
    print("fail")

3. Check the given character uppercase or lower case or digit or special
character?

ch = input()
if ch[0].isupper():
    print("upper")
elif ch[0].islower():
    print("lower")
elif ch[0].isdigit():
    print("digit")
else:
    print("Special Symbol")


4. Print which number is biggest among two numbers.

a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)

5. Print square of each number up to 20.

for i in range(1,21):
    print(i*i)


6. Print “n” Even numbers.
n = int(input())
for i in range(1,n):
    if i % 2 == 0:
        print(i)

7. Print sum of all even numbers b/w 1 to n.
n = int(input())
sum = 0
for i in range(1,n):
    if i % 2 == 0:
        sum += i

print(sum)


8. Program to print the prime numbers from 1 to 10.

for i in range(2,11):
    prime = True
    for j in range(2,11):
        if i % j == 0 and i != j:
            prime = False
            break
    if(prime):
        print(i)


9. Print square of each number up to 20.
for i in range(1,21):
    print(i*i)

10.Print factorial of n.
import sys

sys.setrecursionlimit(500000)

def fact(n):
    if n == 1:
        return 1

    return fact(n-1) * n

n = int(input())
print(fact(n))




