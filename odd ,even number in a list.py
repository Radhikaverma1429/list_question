list1=[]
even=0
odd=0
i=0
while i<=10:
    num=int(input("enter a number"))
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
    list1.append(num)
    i=i+1
print(list1,even,"even number")
print(list1,odd,"odd number") 
