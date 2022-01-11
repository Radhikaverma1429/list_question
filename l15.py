ele= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
odd=0
even=0
count=0
all_sum=0
sum=0
sum1=0
while i<len(ele):
    all_sum=all_sum+ele[i]
    if ele[i]%2==0:
        even=even+1
        sum=sum+ele[i]
        avrage=sum//ele[i]
    if ele[i]%2!=0:   
        odd=odd+1
        sum1=sum1+ele[i]
        avrage1=sum1//ele[i]
        all_avrege=all_sum//ele[i]
    count=count+1
    i=i+1
print(avrage,"avrage of even number")
print(avrage1,"avrege of odd number") 
print(even,"total even of number")
print(odd,"total odd of numbere")
print(all_avrege,"total avrage of list")
print(all_sum,"total sum of list")
print(count,"total count of list")