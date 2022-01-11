num1=int(input("enter a number "))
num2=int(input("enter a number "))
list1=[]
while num1<=num2:
    i=1
    f=0
    while i<=num1:
        if num1%i==0:
            f=f+1
        i=i+1
    if f==2:
        list1.append(num1)
    num1+=1
print(list1)

