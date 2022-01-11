name=["n","i","t","i","n"]
i=0
while i<len(name):
	my_list=(name[::-1])
	if name==my_list:
		i+=1
	else:
		print("not palindrom")
print(my_list,"palindrom")
