try:
    n = int(input())
    result = 10 / n

except (ValueError, ZeroDivisionError) as e:
    print(e) 