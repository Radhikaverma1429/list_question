a = [1,2,3,4,5,6]
b = [2,3,1,0,6,7]
i=0
empty=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i] not in b:
            empty.append(a)
            empty.append(b)
        j+=1
    i+=1
print(empty)