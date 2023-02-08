from itertools import product
def f(x,y,z):
    count=0
    for i in range(3,z):
        print(i)
        input()
        b=product('12',repeat=i)
        for n in b:

            if (x==10 and n.count('2')>1):continue

            a=int(x)
            for j in n:
                if j=='1':
                    a+=1
                else :
                    a*=2
                if a==17:break
            if a==y:
                count+=1
    return(count)

print(f(1,10,10))
print(f(10,35,25))
