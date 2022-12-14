def hem():
    chisla = '0123456789'
    chisla_spisok = list(chisla)
    print(chisla_spisok)
    haming = '0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    haming_spisok = haming.split()
    print(haming_spisok)


    def distance(x, y):
        k = 7
        for i in range(7):
            if x % 10 == y % 10:
                k = k - 1
                x = x // 10
                y = y // 10
        return k


    code = int(input("code= "))
    min=distance(code,int(haming_spisok[0]))
    imin = 0
    for i in range(10):
        D = distance(code, int(haming_spisok[i]))
        print(D)
        if D < min:
            min = D
            imin = i
    if min == 0:
        print(f"код верный: символ {chisla_spisok[imin]}")
    elif min == 1:
        print(f"код исправлен: символ {chisla_spisok[imin]}")
    else:
        print("код неверный")
def morz():
    a = "abwgdevijklmnoprstufhcqx"
    abc = list(a)
    print(abc)
    b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
    abcm=b.split()
    print(abcm)
    abcm=b.split()
    text=input("Введите текст на английском: ")
    indm=""
    for i in range (len(text)):
        ind = abc.index(text[i])
        indm=indm + abcm[ind]
    print(f"{indm}строка  в азбуке морзе")
def ss():
    p=int(input("p="))
    Np=int(input(f"N{p}="))
    k=int(1)
    N10=int(0)
    while  Np!=0:
        N10+= (Np %10)*k
        k=k*p
        Np= Np//10
    print(f"N10={N10}")
def tb():
    p = int(input("vvedite p (2<p<=10):"))
    x,y = int(1),int(1)
    for x in range (1,p):
       a=[]
       for y in range (1,p):
          z = (x*y//p)*10 + (x*y)% p
          a.append(z)
       print(a)
def periz10():
    print("Вdедите Число")
    N10 = int(input())
    print("Куда")
    p = int(input())
    k = 1
    Np = 0
    flag = True
    while flag == True:
        Np = Np + (N10 %p)*k
        k=k*10
        N10 = N10 // p
        if N10 == 0:
            flag = False
    print(Np)
stat=1

while stat == 1:
    a=int(input("Выберите программу \n 1)Код Хэмминга \n 2)Морзе \n 3)Перевод из любой в 10-ичную \n 4)Таблица Умножения \n 5)Перевод из 10-ичной в любую"))
    if a==1:
         hem()
    elif a==2:
         morz()
    elif a==3:
         ss()
    elif a==4:
        tb()
    elif a==5:
        periz10()
    else:
        print ("Error")

    a=input("Введите 1, если хотите прекратить работу программы.Введите 0, если хотите вернутся в меню")
