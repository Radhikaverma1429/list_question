n=int(input("enter number"))
i=1
a=[]
while i<=n:
	j=1

	b=[]
	while j<=10:
		c=i*j
		b.append(c)
		j=j+1
	i=i+1
	a.append(b)
print(a)
	