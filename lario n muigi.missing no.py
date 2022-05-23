list=[1,3,5,6,7,8]
i=0
a=[]
while i<list[-i]:
    if i not in list:
        a.append(i)
    i+=1
    print(i)