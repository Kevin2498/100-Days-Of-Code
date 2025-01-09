def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, kwargs: {kwargs}")
        if func.__name__ == "add":
            if any([i for i in args if isinstance(i, str)]):
                args = tuple([str(i) if isinstance(i, int) else i for i in args])
        else:
            args = tuple([int(i) if isinstance(i, str) else i for i in args])
        return(func(*args, **kwargs))
    return wrapper


@logging
def add(a, b):
    return(a+b)

@logging
def sub(a, b):
    return(a-b)

x = 5
y = 3

print(add(x, y))
print(sub(x, y))
