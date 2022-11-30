a=['Sin30?','tg45','tg*ctg','1 Алкан','2+2']
b=['0.5','1','1','метан','4']
count=0
for i in range (len(a)):
    print(a[i])
    ans=input()
    if ans==b[i]:
        print('Правильно')
        count+=1
    else:
        print('Неправильно')
print(count)