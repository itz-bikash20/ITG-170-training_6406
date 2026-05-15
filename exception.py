# 1. Try-Except Block

try:
    a = 10 / 0
    print(a)

except ZeroDivisionError:
    print("Exception Handled")


# 2. Multiple Except Block

try:
    num = int("hello")
    a = 10 / 0

except ValueError:
    print("Value Error Occurred")

except ZeroDivisionError:
    print("Zero Division Error Occurred")
# 3. Nested Try Block

try:

    try:
        a = 10 / 0

    except ZeroDivisionError:
        print("Inner Try Exception Handled")

except:
    print("Outer Exception")
    # 4. Finally Block

try:
    a = 10 / 0

except ZeroDivisionError:
    print("Exception Caught")

finally:
    print("Finally Block Executed")
# 5. Raise Keyword (similar to Java throw)

age = 15

try:
    if age < 18:
        raise Exception("Not Eligible")

    else:
        print("Eligible")

except Exception as e:
    print(e)
# 6. Function Exception Handling (similar to throws)

def check():
    a = 10 / 0


try:
    check()

except ZeroDivisionError:
    print("Exception Handled")