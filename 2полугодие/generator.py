from itertools import product
a=[x for x in range(3)]
print(a)
for i  in a:
    print(i)
for i in range (len(a)):
    print(a[i])
for k in range (len(a)):
    for y in range (len(a)):
        print(a[k],a[y])
for x in range(len(a)):
    for y in range(x+1,len(a)):
        print(a[x],a[y])
b=list(product('012',repeat=2))
print(b)
for i in range (len(a)-1):
    if a[i]+a[i+1]:
        print(a[i]+a[i+1])
while true:
    status=0
    for i in range (len(a)-1)
        if a[i] < a[i+1]:
            a[i],a[i+1]+a[i+1],a[i]
    print(a)
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            status+=1

    if status==0: break

