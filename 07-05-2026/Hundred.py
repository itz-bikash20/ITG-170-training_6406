def hundred(n):
    if n > 100:
        return
    print(n)
    n+=1
    hundred(n)

n = int(input())
hundred(n)