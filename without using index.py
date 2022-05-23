# list=[1,2,3,4,5,6]
# i=0
# while i<len(list):
#     b=str(list[i])+str(list[i+1])
#     print(b)
#     i+=2
a="jiANreILiu"
count=0
if (a.isupper()) == True: 
        count1+= 1
        newstring+=(a.lower()) 
elif (a.islower()) == True: 
        count2+= 1
        newstring+=(a.upper()) 
elif (a.isspace()) == True: 
        count3+= 1
        newstring+= a 
          
print("In original String : ") 
print("Uppercase -", count1) 
print("Lowercase -", count2) 
print("Spaces -", count3) 
  
print("After changing cases:") 
print(newstring)