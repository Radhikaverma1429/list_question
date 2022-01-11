n=[23,25,145,153,225,407]
i=0
while i<len(n):
    num=n[i]
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem**3
        num=num//10
    if sum==n[i]:
        print(sum, "is armstrong number")
    i=i+1 