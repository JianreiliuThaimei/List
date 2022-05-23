# list=[[1,2,3],[4,5,6],[7],[8,9]]
# import itertools
# flat_list=list(itertools.chain(*list))
# print(flat_list)


# a=[[1,2,3],[4,5,6],[7],[8,9]]    
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         e=(a[i][j])
#         b.append(e)
#         j=j+1
#     i=i+1
# print(b)


list=[[1,2,3],[4,5,6],[7],[8,9]]
# print(len(list))
b=[]
i=0
while i<len(list):
        j=0
        while j<len(list[i]):
            b.append(list[i][j])
            j+=1
        i+=1
print(b)
