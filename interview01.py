l1 = [1,2,3,2,2,4,5,2,6,2,2,2,7,8,2,2,9,2]

str1 = "[{}{}(]"
str2 = "[{}{}]"

# Handle int and string concatination using decorators

# Python 
# Signal
# Different types of memory


# output = [1, 3, 4, 5, 6, 7, 8, 9]

# print(dir(l1))
l1.sort()
count = l1.count(2)
print(l1[count::])
# print(count)
# print(l1)

def is_balanced(s):
    # Define matching pairs of brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        if char in matching_brackets.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_brackets:
            # If it's a closing bracket, check if it matches the top of the stack
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    
    # Return True if the stack is empty (all brackets matched), else False
    return not stack

# Test the strings
str1 = "[{}{}(]"
str2 = "[{}{}]"

print(is_balanced(str1))  # Output: False
print(is_balanced(str2))  # Output: True
