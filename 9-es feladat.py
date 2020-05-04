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