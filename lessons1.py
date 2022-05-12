def func(ls:list, result = 0):
    for i in ls:
        if type (i) == int:
            result += i
        else:
            result = func(i, result)
    return result

print(func())

