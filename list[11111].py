# list=[1,2,3,4,5]
# i=0
# b=[]
# a=1
# while i<len(list):
#     c=list[i-a+1]
#     print(c)
#     b.append(c)
#     a=a+1
#     i+=1
# print(b)



num=[1,2,3,4,5]
i=0
a=1
b=[]
while i<len(num):
    b.append(a-i)
    i+=1
    a+=1
print(b)

