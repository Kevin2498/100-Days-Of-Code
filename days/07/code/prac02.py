a = 1
b = "Hello"
c = 3

def dec(func):
    def concat_vars(*args):
        print(f"Calling {func.__name__} with arguments {args}")
        if any(isinstance(i, str) for i in args):
            args = tuple(str(i) if isinstance(i, int) else i for i in args)
        # print(args)
        return(func(*args))
    return concat_vars
    

@dec
def custom_sum(a, b):
    return a+b
    

print(custom_sum(a,b))