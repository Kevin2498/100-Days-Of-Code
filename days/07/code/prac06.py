from functools import reduce

l1 = [1,2,3,4]
l2 = [9,8,7,6]

print(list(zip(l1, l2)))

print(list(filter(lambda x: x%2==0, l1)))

print(reduce(lambda a,b: a+b, l1))

print(list(map(lambda x: x*2, l1)))