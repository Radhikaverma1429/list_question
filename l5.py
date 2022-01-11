a=[1,2,-3,-4,5,-6]
i=0
while i<len(a):
	if a[i]>0:
		a[i]=a[i]
	else:
		a[i]=0
	i=i+1
print(a)

a=[1,2,-3,-4,5,-6]
i=0
empty=[]
while i<len(a):
	if a[i]<0:
		empty.append(0)
	else:
		empty.append(a[i])
	i=i+1
print(empty)