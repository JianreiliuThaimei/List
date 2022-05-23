a=[1,2,2,1]
b=[]
i=0
while i<(len(a)):
    b.append(a[i])
    i+=1
if a==b:
    print("palindrome no.")
else:
    print("not")