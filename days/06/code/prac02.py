# map, filter, zip, reduce and lambda
from functools import reduce 


li = [1,2,3]

res = map(lambda x: x*2, li)
print(list(res))

li = [1,2,3,4,5,6,7,8,9]

res = filter(lambda x: x%2 == 0,li)
print(list(res))


l1 = [1,2,3,4,5]
l2 = ["a", "b", "c", "d"]

res = list(zip(l1, l2))
print(res)

l1 = ["name", "age"]
l2 = ["Kevin", "26"]

res = dict(zip(l1,l2))
print(res)


li = [1,2,3,4,5,6,7,8,9,10]
res = reduce(lambda x, y: x+y, li)
print(res)

l1 = [1,2,3,4,5]
res = [(lambda x:x*2)(i) for i in l1]
print(res)