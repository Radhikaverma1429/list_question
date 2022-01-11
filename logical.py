chance=int(input("enter a chance number "))
c=0
c1=0
odd=[]
even=[]
i=0
while i<chance:
    userinput=int(input("enter a user number "))
    if userinput%2==0:
        c+=1
        even.append(userinput)
    else:
        c1+=1
        odd.append(userinput)
    i+=1 
print(c)
print(c1)
print("even number ",even)
print("odd number ",odd)