# Object Oriented Programming

def logging(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with arguments {args[1:]}")
        res = func(*args)
        print(f"{func.__name__} returned {res}")

        return res
    return wrapper


class BigObject:
    @logging
    def add(self, a,b):
        return(a+b)
    
    @logging
    def sub(self, a,b):
        return(a-b)

obj1 = BigObject() #Class

print(obj1.add(3,2))
print(obj1.sub(5,2))