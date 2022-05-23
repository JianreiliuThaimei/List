# name=['n','i','t','i','n']
# num=[]
# i=-1
# while i>=(-len(name)):
#     num.append(name[i])
#     i-=1
# if name==num:
#     print("palindrome")
# else:
#     print("palindrome")

user=input("enter the name")
rev_user=user[::-1]
if user==rev_user:
    print(user,"is a palindrome")
else:
    print(user,"is not")