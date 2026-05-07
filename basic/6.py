def f(value:int):
    total=1
    for i in range(1,value+1):
        total*=i
    return total


print(f(5))
