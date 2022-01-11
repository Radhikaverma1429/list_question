a = [1,2,3,4,5,6]
maxs=0
max_1=0
i=0
while i<len(a):
    if a[i]>maxs:
        max_1=maxs
        maxs=a[i]
        if max_1<a[i] and maxs>a[i]:
            maxs=a[i]
    i=i+1
print(max_1)
    