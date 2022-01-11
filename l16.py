ele=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=0
odd=0
while i<len(ele):
	if ele[i]%2==0:
		even=even+1
		avr=ele[i]//even
	elif ele[i]%2!=0:
		odd=odd+1
		avre=ele[i]//odd
	i=i+1
print(avr,'tota avrege of even bumber')
print(avre,'total avrege of odd number')


