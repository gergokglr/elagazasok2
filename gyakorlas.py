def feladat1():
    print("1. feladat")
    print("A program eldönti, hogy egy egész szám pozitív-e!")
    szam: int = int(input("Adjon meg egy edész számot. :"))
    if szam > 0:
        print("A szám pozitív!")
    else:
        print("")

def feladat2():
    print("2. feladat")
    print("A feladat leirja az egyjegyyű egész szám elötti és mögötti számot.")
    szam: int = int(input("Adjon meg egy számot. :"))
    if szam >= 0 and szam < 10:
        print(f"{szam-1} , {szam+1}")
    else:
        print("")

def osztalyzat1():
    print("Oszályzat 1.")
    szam: int = int(input("Adjon meg egy számot. :"))
    if szam >= 0 and szam <= 59:
        print(f"{szam}% Elégtelen")
    elif szam >= 60 and szam <= 69:
        print (f"{szam}% Elégséges")
    elif szam >= 70 and  szam <= 79:
        print (f"{szam}% Közepes")
    elif szam >= 80 and szam <= 89:
        print (f"{szam}% Jó")
    elif szam >= 90 and szam <= 100:
        print (f"{szam}% Jeles")
    else:
        print (f"Hiba: érvénytelen százalék! {szam}%")

def osztalyzat2():
    print("Osztályzat 2.")
    szam: int = int(input("Adja meg az osztályzatot! :"))
    if szam == 1:
        print(f"Elégtelen, érdemjegy: {szam}.")
    elif szam == 2:
        print(f"Elégséges, érdemjegy: {szam}.")
    elif szam == 3:
        print(f"Közepes, érdemjegy: {szam}.")
    elif szam == 4:
        print(f"Jó, érdemjegy: {szam}.")
    elif szam == 5:
        print(f"Jeles, érdemjegy: {szam}.")
    else:
        print(f"Érvénytelen osztályzat! {szam}?")

def parosparatlan():
    print("Páros páratlan!")
    szam: int = int(input("Adjon meg egy számot! :"))
    if szam % 2 == 0:
        print("A szám páros!")
    else:
        print("A szám páratlan!")
