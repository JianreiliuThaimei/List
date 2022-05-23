a=[1,7,8]
i=0
while i<len(a):
    j=1
    c=0
    while j<=a[i]:
        if a[i]%j==0:
            c=c+1
        j+=1
    if c==2:
        print(a[i],"prime")
    else:
        print(a[i],"not")
    i+=1