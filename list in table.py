num=int(input("enter a number "))
list1=[]
i=1
while i<=num:
    j=1
    c=0
    list2=[]
    while j<=10:
        c=i*j
        list2.append(c)
        j=j+1
    list1.append(list2)
    i=i+1
print(list1)