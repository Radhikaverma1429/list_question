a=['a','b','a','c','d','e','f','f','a','b','i','j']
i=0
empty=[]
while i<len(a):
	j=0
	c=0
	b=[]
	while j<len(a):
		if a[i]==a[j]:
			c=c+1
		j=j+1
	b.append(a[i])
	b.append(c)
	if b not in empty:
		empty.append(b)			
	i+=1
print(empty) 