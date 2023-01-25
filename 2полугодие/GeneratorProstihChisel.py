sp=[]
for num in range (2,1000000):
    if all (num%delit!=0 for delit in range (2,num-1)):
        sp.append(num)
print(sp)