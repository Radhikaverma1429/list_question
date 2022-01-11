a=[11,23]
b=[]
i=0
while i<len(a):
	j=0
	c=" "
	d=str(a[i])
	while j<len(d):
		if d[j]=='0':
			c=c+'zero'
		elif d[j]=='1':
			c=c+'one'
		elif d[j]=='2':
			c=c+'two'
		elif d[j]=='3':
			c=c+'three'
		j+=1
	i=i+1
	b.append(c)
print(b)