# # find the average
# marks=[[78,76,89,94,88,86],[91,71,67,87,65,71],[45,73,74,66,54,52]]
# i=0
# while i<len(marks):
#     j=0
#     sum=0
#     average=0
#     while j<len(marks[i]):
#         sum=sum+(marks[i][j])
#         average=sum//len(marks[i])
#         j+=1
#     i+=1
#     print(average,"is average")



# different type
marks=[[78,76,89,94,88,86],[91,71,67,87,65,71],[45,73,74,66,54,52]]
i=0
while i<len(marks):
    j=0
    sum=0
    average=0
    while j<len(marks[i]):
        sum=sum+(marks[i][j])
        average=sum//len(marks[i])
        j+=1
    i+=1
print(average,"is average")

# TOTAL MARK
# marks=[[78,76,89,94,88,86],[91,71,67,87,65,71],[45,73,74,66,54,52]]
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         j+=1
#     i+=1
# print(sum)