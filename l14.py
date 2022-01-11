name = "mynamepreet"
a = []
tmp = " "
for c in name:
    if tmp == " ":
        a.append(tmp)
        tmp =tmp+c+" "
    else:
      a+= c
if tmp:
   a.append(tmp)
print(a)