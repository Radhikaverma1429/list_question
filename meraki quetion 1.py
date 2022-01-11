# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# c=0
# for i in numbers:
#     c+=1
# print("total elements in a list",c)

# num=int(input("please enter a number :"))
# x=(num//2)*2
# if x==num:
#     print("even")
# else:
#     print("odd")

# def plus(oprator,a,b):
#     sum=a+b
#     return sum
# def substract(aprator1,value1,value2):
#     sub=value1-value2
#     return sub
# def multiply(oprator,c,d):
#     mul=c*d
#     return mul
# def main():
#     print(plus(input("rnter a any symbal"),int(input("enter a any number ")),int(input("enter a number "))))
#     print(substract(input("rnter a any symbal"),int(input("enter a any number ")),int(input("enter a number "))))
#     print(multiply(input("rnter a any symbal"),int(input("enter a number ")),int(input("enter a number ")))) 
# main()

# def plus(oprator,a,b):
#     if oprator=="+":
#         return a+b
#     elif oprator=="-":
#         return a-b
#     elif oprator=="*":
#         return a*b
#     elif oprator=="/":
#         return a/b
#     elif oprator=="//":
#         return a//b
#     elif oprator=="%":
#         return a%b
# def main():
#     print(plus(input("rnter a any symbal"),int(input("enter a any number ")),int(input("enter a number "))))
# main()

# l=[1,2,3,4,5,6,7]
# sum=0
# c=0
# i=0
# while i<len(l):
#     sum+=l[i]
#     c+=1
#     avrge=sum//c 
#     i+=1
# print(sum)
# print(avrge)

# dic={1:"one",2:"two",3:"three",4:"four",5:"five"}
# even={}
# odd={}
# for i in dic:
#     if i%2==0:
#         even[i]=dic[i]
#     else:
#         odd[i]=dic[i]
# print(even)
# print(odd) 


# dic={1:"one",2:"two",3:{4:"three",5:"four",6:"five"}} 
# odd={}
# even={}
# for i in dic:
#     if type(dic[i])==dict:
#         for j in dic[i]:
#             if j%2==0:
#                 even[j]=dic[i][j]
#             else:
#                 odd[j]=dic[i][j]
#     if i%2==0:
#         even[i]=dic[i] 
#     else:
#         odd[i]=dic[i]
# print(odd) 
# print(even) 

# dic={"c1":[10,20,30],"c2":[20,30,40],"c3":[1,2,3,4]}
# for i in dic:
#     dic[i].clear()
# print(dic)

# dic=[1,2,3,4,5,6,7]
# d={}
# while len(dic)>=3:
#     d["c1"]=dic
#     # i+=1
# print(d) 

# l=[1,2,3,4,2.4,3.5,"radhika","shiv"]
# s=[]
# f=[]
# intiger=[]
# i=0
# while i<len(l):
#     if type(l[i])==str:
#         s.append(l[i])
#     elif type(l[i])==int:
#         intiger.append(l[i])
#     else:
#         f.append(l[i])
#     i+=1
# print(s)
# print(intiger)
# print(f) 

# n=int(input("enter aqny number! "))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",(i*j))
#         j+=1
#     i+=1

# str1="bhavya is a girl"
# i=0
# c=0
# while i<len(str1):
#     if str1[i]==" ":
#         c+=1
#     i+=1
# print(c) 

# l=[-1,-2,-3,-4]
# m=0
# i=0
# while i<len(l):
#     if l[i]>m:
#         m=l[i]
#     i+=1
# print(m) 

# a=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
#     print(sum)  

# a=[1,[2,3,45,[67]]]
# l=[] 
# i=0
# while i<len(a):
#     print(i)
#     s=' '
#     j=0 
#     d=str(a[i])
#     while j<len(d):
#         if d[j]=='1':
#             s=s+'one'
#         if d[j]=='2':
#             s=s+'two'
#         if d[j]=='3':
#             s=s+'three'
#         if d[j]=='4':
#             s=s+'four'
#         if d[j]=='5':
#             s=s+'five'
#         if d[j]=='6':
#             s=s+'six'
#         if d[j]=='7':
#             s=s+'seven'
#         if d[j]=='8':
#             s=s+'eight'
#         if d[j]=='9':
#             s=s+'nine'
#         if d[j]=='0':
#             s=s+'zero'
#         j+=1
#     i=i+1
#     l.append(s)
# print(l)

# name=input("enter any number! ")
# upper=0
# lower=0
# for i in name:
#     if (i.isupper()):
#         upper+=1
#     if (i.islower()):
#         lower+=1
# print(i)

n=int(input("enter any number! "))
if n%2!=0:
    print("wiered")
elif n%2==0 and 2<5:
    print("Not Weird")
elif n%2==0 and 6<20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")
else:
    pass

n = int(input()) 
i=0
while i<n:
    print(i**n)
    i+=1

n=int(input("enter a number "))
for i in range(0,n):
    print(i*i) 