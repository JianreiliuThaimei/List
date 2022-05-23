# list=[6,1,3,5,6,3,1]
# i=0
# p=1
# a=[]
# while i<len(list):
#     if list[i] not in a:
#         a.append(list[i])
#         p=p*a[i]
#     i+=1
# print(p)

numbers=[23,40,50,70,56,12,5,10,7]
firstmax=numbers[0]
secmax=numbers[0]
thirdmax=numbers[0]                                         
i=0
while i<len(numbers):
    if numbers[i]>firstmax:
        firstmax=numbers[i]
    i+=1
i=0
while i<len(numbers):
    if numbers[i]>secmax and numbers[i]!=firstmax:
        secmax=numbers[i]
    i+=1
i=0
while i<len(numbers):
    if numbers[i]>thirdmax and numbers[i]!=firstmax and numbers[i]!=secmax:
        thirdmax =numbers[i]
    i+=1
print(firstmax)
print(secmax)
print(thirdmax)



