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

stat=1



while stat == 1:
    a=input("Выберите программу \n 1)Код Хэмминга \n 2)Морзе \n 3)Система счисления")
    if a==1:
         hem()
    elif a==2:
         morz()
    else :
         ss()
    a=input("Введите 1, если хотите прекратить работу программы.Введите 0, если хотите вернутся в меню")
