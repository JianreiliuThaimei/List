a=[1,1,2,3,4,5,1,2]
i=0
while i<len(a):
    if a[i]==i:
        a.remove(a[i])
    i+=1
print(a)