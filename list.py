a=["one","two","three","four","five"]
def  word(n):
    if n==0:
        return ""
    else:
        x=a[n%10]
        y=word(int(n/10))+x
    return y
n=int(input("enter the number"))
print(word(n))

# a="jiANreILiu"
# i=0
# b=[]
# while i<len(a):
    





# output="JIanREilIU"
# output=[0,1,4,5,8,9]