# a="123"
# b="23"
# print(b+a+b)

# a="grace"
# b="sarika"
# print(a+b+a)
 
 
def add(a,b):
    if len(a)<len(b):
        return (a+b+a)
    else:
        return (b+a+b)
print(add("123","23"))
print(add("grace","sarika"))
print(add("jian","tessa"))
