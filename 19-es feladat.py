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