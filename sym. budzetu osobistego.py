# 📊 Wyświetlać podsumowanie miesiąca

print("Witaj w apce do kontrolowania budrzetu")

przychody = []
wydatki = []


# "a" → tryb dopisywania (append)
# "w" → nadpisuje plik
# "r" → odczyt

def dodawanie_pieniedzy(ilosc, kategoria, data):
    with open("plusy.txt", "a") as file:
        file.write(f"{ilosc},{kategoria},{data}\n")

def odejmowanie_pieniedzy(ilosc, kategoria, data):
    with open("minusy.txt", "a") as file:
        file.write(f"{ilosc},{kategoria},{data}\n")

def liczenie_salda_plus():
    suma_przychodow = 0
    for x in przychody:
        suma_przychodow += x["ile"]
    return suma_przychodow

def liczenie_salda_minus():
    suma_wydatkow = 0
    for x in wydatki:
        suma_wydatkow += x["ile"]
    return suma_wydatkow

def podsumowanie_miesiaca(miesiac, rok):
    miesiac = int(miesiac)
    rok = int(rok)

    glowne_kategorie2 = []
    glowne_kategorie = []
    przychody_w_miesiacu = []
    wydatki_w_miesiacu = []
    suma = 0

    for x in przychody:
        if x["miesiac"] == miesiac and x["rok"] == rok:
            przychody_w_miesiacu.append(x)
            suma += x["ile"]

    for x in wydatki:
        if x["miesiac"] == miesiac and x["rok"] == rok:
            wydatki_w_miesiacu.append(x)
            suma -= x["ile"]

    for x in przychody_w_miesiacu:
        glowne_kategorie.append(x["kategoria"])

    for x in wydatki_w_miesiacu:
        glowne_kategorie2.append(x["kategoria"])

    return suma, glowne_kategorie, glowne_kategorie2

def dodawanie_przychodow():
    przychody.clear()
    try:
        with open("plusy.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    ilosc, kategoria, data = line.split(",")
                    dzien, miesiac, rok = data.split(".")
                    przychody.append({
                        "ile": float(ilosc),
                        "kategoria": kategoria,
                        "data": data,
                        "dzien": int(dzien),
                        "miesiac": int(miesiac),
                        "rok": int(rok)
                    })
    except FileNotFoundError:
        pass

def dodawanie_wydatkow():
    wydatki.clear()
    try:
        with open("minusy.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    ilosc, kategoria, data = line.split(",")
                    dzien, miesiac, rok = data.split(".")
                    wydatki.append({
                        "ile": float(ilosc),
                        "kategoria": kategoria,
                        "data": data,
                        "dzien": int(dzien),
                        "miesiac": int(miesiac),
                        "rok": int(rok)
                    })
    except FileNotFoundError:
        pass


dodawanie_przychodow()
dodawanie_wydatkow()


while True:
    while True:
        print("=====MENU=====")
        print("1.Przychód")
        print("2.Wydatkek")
        print("3.Podsumowania")
        print("==============")

        wybor = input("Co chcesz zrobić (wpisz 1, 2 lub 3):    ")

        if wybor == "1":
            dodawanie_pieniedzy(input("Ile: "), input("kategoria: "), input("data: "))
            dodawanie_przychodow()
            break

        elif wybor == "2":
            odejmowanie_pieniedzy(input("Ile: "), input("kategoria: "), input("data: "))
            dodawanie_wydatkow()
            break

        elif wybor == "3":
            while True:
                print("==============")
                print("1.Podsumowanie miesiąca")
                print("2.Twoje saldo")
                print("==============")

                wybor = input("Co chcesz zrobić (wpisz 1 lub 2):    ")

                if wybor == "1":
                    print("Podsumowanie którego miesiąca chcesz zobaczyć?")

                    ktory_miesiac = input("Wpisz miesiąc(01,02...):    ")
                    ktory_rok = input("Wpisz rok(2026,2027...):    ")

                    aktualne_pods, kategorie, kategorie2 = podsumowanie_miesiaca(ktory_miesiac, ktory_rok)

                    if aktualne_pods > 0:
                        print(f"W tym miesiącu zarobiłeś: {aktualne_pods}")
                    elif aktualne_pods == 0:
                        print(f"W tym miesiącu twoje saldo to: {aktualne_pods}")
                    else:
                        print(f"Niestety twoje saldo miesiąca wynosi: {aktualne_pods}")

                    odp = input("Czy chcesz zobaczyć kategorie na które wydawałeś i z których zarabiałeś (jeśli tak wpisz 1, lub jeśli nie wpisz 2):    ")

                    if odp == "1":
                        print("w tym miesiącu kategorie z których zarabiałeś to: \n")
                        print(kategorie)
                        print("w tym miesiącu kategorie na które wydawałeś to: \n")
                        print(kategorie2)
                    else:
                        break

                    break

                elif wybor == "2":
                    suma_przychodow = liczenie_salda_plus()
                    suma_wydatkow = liczenie_salda_minus()
                    saldo_laczne = suma_przychodow - suma_wydatkow
                    print(saldo_laczne)
                    break

                else:
                    print("Coś poszło nie tak...")

        else:
            print("Coś poszło nie tak...")