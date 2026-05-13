def func1(*args):
    for item in args:
        print(item, end=" ")
    print()


func1(20, 40, 60)
func1(80, 100)