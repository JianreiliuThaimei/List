# list1=['0','1','2','3','4','5']
# list2=['red','green','black','blue','yellow','indigo']
# list3=['100','200','300','400','500','600']
# i=0
# b=[]
# while i<len(list1):
#     b="".join(list1[i]+list2[i]+list3[i])
#     i+=1
#     print(b,end="")


list1=['0','1','2','3','4','5']
list2=['red','green','black','blue','yellow','indigo']
list3=['100','200','300','400','500','600']
length=len(list1)
count=0
while count<length:
    print(list1[count]+str(list2[count]+str(list3[count])))
    count+=1