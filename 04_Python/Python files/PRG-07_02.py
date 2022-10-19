numbers = [20, 12 ,33 , 70, 9]
thislist = numbers
print(thislist)
for i in range(len(thislist)):
    if i != 4:
       print(thislist[i + 1] + thislist[i])
    else:
        print(thislist[0] + thislist[i])  