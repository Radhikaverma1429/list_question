ele=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=0
odd=0
sum=0
sum1=0
while i<len(ele):
	if ele[i]%2==0:
		even=even+1
		sum=sum+even
	elif ele[i]%2!=0:
		odd=odd+1
		sum1=sum1+odd
	i=i+1
print(sum1,'odd number')
print(sum,'even number')
