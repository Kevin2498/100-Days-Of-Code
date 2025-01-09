str1 = "[{}{}(]"
str2 = "[{}{}]"

str3 = "[{()()]"

def check_balance(str0):
    brackets = {"(": ")", "[": "]", "{": "}"}
    l1 = []
    l2 = []
    for i in str0:
        if i in brackets:
            l1.append(i)
        elif i in brackets.values():
            l2.append(i)
    
    if len(l1) == len(l2):
        return True
    else:
        return False

print(check_balance(str1))
print(check_balance(str2))
print(check_balance(str3))
