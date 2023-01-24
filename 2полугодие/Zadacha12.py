for i in range (2,1000):
    k=0 
    for n in range(2,i-1):
        if i%n==0 :
            k=1
            
    if k==0:
        d=(i-117)%4
        if d==0:
            if i>121:
                f=(i-117)/4
                print(f)