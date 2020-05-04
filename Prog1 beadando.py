# #EX26

from math import gcd

part = input("Írja be a megnézett időtartalmat! (hh:mm:ss):")
total = input("Írja be a teljes időtartalmat! (hh:mm:ss):")
par=part.split(":")
tota=total.split(":")

if part==total:
    print("Megnézted az egész filmet")
elif part== "00:00:00":
    print("Még nem kezdted el a filmet")
elif part>total:
    print("A megadott rész hosszabb mint maga a film, módosítsd a bevitt adatokat")
else:
    part_h=int(par[0])
    total_h=int(tota[0])

    part_m=int(par[1])
    total_m=int(tota[1])

    part_s=int(par[2])
    total_s=int(tota[2])

#most átalakítok mindent másodpercbe
    parth_s=(part_h*60)*60
    totalh_s=(total_h*60)*60

    partm_s=(part_m*60)
    totalm_s=(total_m*60)

    osszpart=parth_s+partm_s+part_s
    ossztotal=totalh_s+totalm_s+total_s

    g=gcd(osszpart,ossztotal)

    megtekintes=[]
    megtekintes.append(int(osszpart/g))
    megtekintes.append(int(ossztotal/g))
    a=megtekintes[0]
    b=megtekintes[1]

    print(megtekintes, "A teljes videó ", int(a), "/", int(b), "részét sikerült már megnézni.", sep='')

#EX9

x=1
teszt=int(input("Adja meg a kívánt tesztesetek számát: "))
if teszt<1 or teszt>5000:
    print("A tesztesetek számának 1 és 5000 közé kell esnie")
else:
    print("A megadott tesztesetek száma megfelel a kritériumnak.")
    while x!=teszt+1:
        n=int(input("Adja meg a tábla sorainak számát(1-50-ig): "))
        m=int(input("Adja meg a tábla oszlopainak számát(1-50-ig): "))
        if (n<1 or m<1 or n>50 or m>50):
            print("A megadott sorok vagy oszlopok száma nem felel meg a megadott kritériumoknak: No")
        else:
            if (n>=1 and m>=1 and n<=50 and m<=50) and (n%2==0 or m%2==0):
                print(f"A {x}. esetben: Yes")
            else:
                print(f"A {x}. esetben: No")
        x=x+1


#EX19

from matplotlib import pyplot as plt

n=int(input("Adja meg mekkora legyen a rajzfelület(n):  "))
plt.xlim(0, n)
plt.ylim(0, n)


x = int(input("Adja meg honan szeretné kezdeni a rajzolást(x) (n-től kisebb értkék): "))
while not 0 <= x <= n:
    print("A megadott szám nem megfelelő!")
    x = int(input("Adja meg honan szeretné kezdeni a rajzolást(x) (n-től kisebb értkék): "))

y = int(input("Adja meg honan szeretné kezdeni a rajzolást(y) (n-től kisebb értkék): "))
while not 0 <= y <= n:
    print("A megadott szám nem megfelelő!")
    y = int(input("Adja meg honan szeretné kezdeni a rajzolást(y) (n-től kisebb értkék): "))
a=[x]
b=[y]

while True:
    irany=input("Adja meg merre szeretne rajzolni(fel/le/jobb/bal): ")
    rajzolas_hossz=int(input("Adja meg mennyit szeretne rajzolni: "))
    if irany=="jobb":
        xs=x+rajzolas_hossz
        ys=y
    elif irany=="bal":
        xs=x-rajzolas_hossz
        ys=y
    elif irany=="fel":
        xs=x
        ys=y+rajzolas_hossz
    elif irany=="le":
        xs=x
        ys=y-rajzolas_hossz
    else:
        print("A megadott irány nem megfelelő")
        continue
    a.append(xs)
    b.append(ys)
    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.plot(a, b,  "k-")
    plt.show()
    x=xs
    y=ys







