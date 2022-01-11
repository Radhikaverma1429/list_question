n=[[8,3,4],[1,5,9],[6,7,2]]
i=0
magic_sum=[]
while i<len(n):
	j=0
	row=0
	colum=0
	while j<len(n[i]):
		row=row+n[i][j]
		colum=colum+n[j][i]
		j=j+1
	i=i+1
	magic_sum.append(colum)
	magic_sum.append(row)
	print(row,"magic square")
	print(colum,"magic square")
i=0
m=len(n)-1
right_diaglon_sum=0
left_diaglon_sum=0
j=0
while i<len(n):
	right_diaglon_sum+=n[i][j]
	left_diaglon_sum+=n[i][m]
	m-=1
	i+=1
if left_diaglon_sum==left_diaglon_sum==colum==row:
	magic_sum.append(right_diaglon_sum)
	magic_sum.append(left_diaglon_sum)
	print(right_diaglon_sum,"magic square")
	print(left_diaglon_sum,"magic square")
else:
	print(right_diaglon_sum,"not magic square")
	print(left_diaglon_sum,"not magic square")
print(magic_sum)	




# real magic square