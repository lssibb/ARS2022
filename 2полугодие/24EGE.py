with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    cnt=cmax=0
    for i in s:
        if i=='*':
            cnt+=1
            cmax=max(cnt,cmax)
        else:cnt=0
print(cmax)