def generator_func(num):
    for i in range(num):
        yield i*2

# for i in generator_func(10):
#     print(i)

g = generator_func(10)
print(g)
next(g)
print(next(g))