l1 = [1,2,3,2,2,4,5,2,6,2,2,2,7,8,2,2,9,2]

length = len(l1) -1
# print(length)

while length>0:
    if l1[length] == 2:
        # print(l1[length])
        l1.pop(length)
    length = length - 1

print(l1)
