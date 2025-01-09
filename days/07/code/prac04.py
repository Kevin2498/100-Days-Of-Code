l0 = [1,2,3,9]
l2 = [1,2,4,4]
l3 = [1,3,4,5]

def check_add(l1):
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if (l1[i]+l1[j] == 8):
                print(l1[i], l1[j])
                return True
    return False

print(check_add(l0)) #False
print(check_add(l2)) #True
print(check_add(l3)) #True