print("Добро пожаловать в игру президент острова!")
ludn=0
zac=0
zem=float(input("Введите начальное количество гектар земли: "))
if zem<0: zem=zem*-1
zer=float(input("Введите начальное количество килограмм зерна: "))
if zer<0: zer=zer*-1
lud=float(input("введите начальное количество ваших людей(1 человек за 1 неделю засеет 1 гектар земли, однако каждую неделю люди кушают 1 кг зерна): "))
if lud<0: lud=lud*-1
i=0
id=1
zern=0
while i<1:
    if lud>zer: 
        lud=zer
        print("У вас осталось", lud,"людей, остальные умерли с голоду")
        zer=0
    zer=zer-lud
    if zer<=0: zer=0
    print("сейчас",id,"неделя")
    print("У вас сейчас:", zem, "гектар земли")
    print("У вас сейчас:", zer, "килограмм зерна")
    print("У вас сейчас:", lud, "людей")
    print("У вас сейчас:", zac, "засееных земель")
    id=id+1
    d=int(input("введите действия(1 - засеять поля (1кг зерна = 1 гектар), 2 - собрать урожай(3 кило с одного гектара), 3 - нанять людей(за 2 кг зерна), 4 - продать людей(1 человек - 2 кг зерна), 5 - закончить игру): "))
    if zer==0 and lud==0: 
        print("Ты проиграл, у тебя нету ни людей без которых ты не сможешь засеять поля и собрать урожай, ни зерна без которого не будет урожая, не будет чем накормить людей и не будет возможности людей нанять.")
        print("Удачи в следующий раз!")
        break
    if d==1 and zem!=0 and lud!=0:
        zac=zac+min(lud,zer,zem)
        zer=zer-min(lud,zem,zer)
        zem=zem-min(lud,zer,zem)
        print("ты засеял", zac ,"гектаров")
    if d==2:
        zern=zac*3
        if zern == 0:
            print("Вы ничего не собрали, поскольку ничего не засеяли.") 
        zem=zem+zac
        zac=0
    if d==3: 
        ludn=int(input("Сколько людей ты хоxешь нанять? напиши тут: "))
        if ludn<0: ludn=ludn*(-1)
        lud=lud+ludn
        zer=zer-ludn*2
    if d==4:
        ludn=int(input("Сколько людей вы хотите продать? Введите тут:"))
        if ludn<0: ludn=ludn*(-1)
        lud=lud-ludn
        zer=zer+ludn*2
    if d==5: break
    elif d!=1 and d!=2 and d!=3 and d!=4 and d!=5: 
        print("Такой команды нет, повтори попытку.")
        break
    if lud<=0: lud=0
    if zer<=0: zer=0
    if zem<=0: zem=0