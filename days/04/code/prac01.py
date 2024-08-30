# Logging using decorators

def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        print(args)
        print(kwargs)
        func(*args, **kwargs)
        print(f"Ran {func.__name__}")
    return wrapper

@logging
def add(a,b):
    print(a+b)


@logging
def subtract(a,b):
    print(a-b)


@logging
def multiply(a,b):
    print(a*b)


add(3,2)
subtract(3,2)
multiply(a=3, b=2)
