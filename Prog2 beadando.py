#EX26

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

    #EX2

