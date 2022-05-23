a=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k']
i=0
last_c=0
last_w=0
last_k=0
while i<len(a):
    if a[i]=='c':
        last_c=str(i)
    elif a[i]=='w':
        last_w==str(i)
    elif a[i]=='k':
        last_k=str(i)
    i+=1
print("last occ.of c :",last_c)
print("last occ.of w :",last_w)
print("last occ.of k :",last_k)