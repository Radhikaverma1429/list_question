n = [6,1,3,5,6,3,1]
i=0
prod=1
empty=[]
while i<len(n):
    if n[i] not in empty:
        empty.append(n[i])
        prod=prod*empty[i]
    i=i+1
print(prod)
print(empty) 