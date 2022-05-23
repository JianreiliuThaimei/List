# num=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# even_count=0
# odd_count=0
# while i<len(num):
#     if num[i]%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#     i+=1
# print("no. of even",even_count)
# print("no. of odd", odd_count)

# a=[2,3,4,5,6]
# even=0
# odd=0
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
#     i+=1
# print(even)
# print(odd)
a=[2,3,4,5,6]
odd=0
i=0
while i<len(a):
    if a[i]%2!=0:
        odd+=1
    i+=1
print(odd)