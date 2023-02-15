import sys
sys.setrecursionlimit(3050)
#def f(n):
    #if n==1:return 1
    #elif n>1:return n*f(n-1)
#print(f(2023)/f(2020))

it1=1
it2=1
for i in range(1,2024):
    it1=it1*i
for i in range(1,2021):
    it2=it2*i
print(it1/it2)