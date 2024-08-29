# *args and **kwargs

def some_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total

print(some_func(1,2,3,4,5, num1=5, num2=10))