

x=list(input("Vvedi chislo"))
x.reverse()
y=int(0)
print(x)
for i in range (len(x)):
    print(x[i])
    y+=int(x[i])*8**(i)
print (y)
