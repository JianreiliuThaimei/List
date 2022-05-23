# a=[1,2,3,4,'5',6,'7',8]
# i=0
# int_sum=0
# str_sum=0
# while i<len(a):
#     if a[i]=="5" or a[i]=="7":
#         str_sum+=int(a[i])
#     else:
#        int_sum+=a[i]
#     i+=1
# print("sum of int",int_sum)
# print("sum of str",str_sum)

a=['1',2,'3',4,'5',6]
i=0
sum_int=0
sum_str=0
while i<len(a):
    if a[i]=='1'or a[i]=='3' or a[i]=='5':
        sum_str+=int(a[i])
    else:
        sum_int+=a[i]
    i+=1
print("sum of int",sum_int)
print("sum of str",sum_str)