# n=[2,3,4,[4,2,4],[6,["a","b"],3],[7,4]]
# i=0
# a=[]
# while i<len(n):
#     if type(n[i])== type([]):
#         j=0
#         while j<len(n[i]):
#             if type(n[i][j])==type([]):
#                 k=0
#                 while k<len(n[i][j]):
#                     a.append(n[i][j][k])
#                     k=k+1
#             else:
#                 a.append(n[i][j])
#             j=j+1
#     else:
#         a.append(n[i])
#     i=i+1
# print(a)

