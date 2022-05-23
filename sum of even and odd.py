# num=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# even_sum=0
# odd_sum=0
# while i<len(num):
#     if num[i]%2==0:
#         even_sum=even_sum+num[i]
#     else:
#         odd_sum=odd_sum+num[i]
#     i+=1
# print("sum of even no.:",even_sum)
# print("sum of odd no.:",odd_sum)


a=[1,2,3,4,'5',6,'7',8]
i=0
int_sum=0
str_sum=0
while i<len(a):
    if a[i]=="5" or a[i]=="7":
        int_sum+=int(a[i])
    else:
        str_sum+=a[i]
    i+=1
print("sum of int",int_sum)
print("sum of str",str_sum)
    

