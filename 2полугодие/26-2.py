with open('26.txt') as f:
    s=[int(x) for x in f]
    s.pop(0)
    s.sort(reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)