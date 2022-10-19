def avg(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t   
    
    avg = sum_num / len(num)
    return avg
 
x = 128
y = 255
z = avg([x,y])
print ("The average of",x,"and", y, "is", z)