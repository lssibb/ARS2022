with open('17.txt') as f:
    a=[int(x) for x in f]
    count=0
for i in range (len(a)-1):
    if (abs(a[i])%10== 3 and abs(a[i+1])%10!=3) or (abs(a[i])%10!=3 and abs(a[i+1])%10
    ==3):
        count+=1
print(count)
sp=[]
sp2=[]
for i in a:
    if i%10==3:
        sp.append(i)
maxi=max(sp)**2
print(maxi)
if a[i]**2+a[i+1]**2>=maxi:
    count+=1
    sp2.append()
    print(count)
