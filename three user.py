# q1
# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(numbers):
#     i+=1
# print(i)

# 3 userinput
# user1=input("enter the name:")
# user2=input("enter the name:")
# user3=input("enter the name:")
# b=''
# i=0
# while i<len(user1) and i<len(user2):
#     if user1[i]==user1[0] and user2[i]==user2[0]:
#         cap=user1[i].upper()
#         cap1=user2[i].upper()
#         b+=cap+''+cap1
#     i+=1
# print(b+'.'+user3)

list=[1,2,3,4,5,6,7,8]
i=0
while i<len(list):
    b=str(list[i])+str(list[i+1])
    print(b)
    i+=2