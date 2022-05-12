def fact(n:int):
    if n > 1:
        n = n * fact(n -1)
    return n

print(fact(5 ))