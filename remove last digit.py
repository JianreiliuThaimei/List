list=[1234,122,1984,19372,100]
i=0
a=0
last=[]
while i<len(list):
    if list[i]>=10:
        a=list[i]//10
    i+=1
    print(a,end=' ')

