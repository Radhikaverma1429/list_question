string =input("enter anything! ") 
newstring ='' 
for a in string: 
    if (a.isupper()) == True: 
        newstring+=(a.lower()) 
    elif (a.islower()) == True: 
        newstring+=(a.upper()) 
    elif (a.isspace()) == True: 
        newstring+= a 
print("In original String : ") 
print("After changing cases:")
print(newstring) 
