import re

pattern = re.compile(r"([a-zA-Z]).([a])")

string = "search this inside of this text please!!!"

a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

a = pattern.search(string)
print(a.group())

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(a)
# print(b)
# print(c)
# print(d)