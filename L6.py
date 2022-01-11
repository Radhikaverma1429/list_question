a=[[1,2,3],[4,5,6],[2,5,4]]
sum=0
i=0
while i<len(a):
	j=0
	while j<len(a[i]):
		sum=sum+a[i][j]
		j=j+1
	i=i+1
	print(sum)
