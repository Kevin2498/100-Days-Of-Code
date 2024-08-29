def highest_even(l1):
    num = 0

    for i in l1:
        if i % 2 == 0:
            if num < i:
                num = i
    
    return num

print(highest_even([10, 2, 3, 4, 16, 8, 19]))