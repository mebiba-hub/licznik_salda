
# 📊 Wyświetlać podsumowanie miesiąca

print("Witaj w apce do kontrolowania budrzetu")

przychody = []
wydatki = []


# "a" → tryb dopisywania (append)
#
# "w" → nadpisuje plik
#
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
    przychody_w_miesiacu = []
    for x in przychody:
        if x[int(miesiac)] == "miesiac" and x[int(rok)] == "rok":
            przychody_w_miesiacu.append(x)
        else:
            continue
    return przychody_w_miesiacu

def dodawanie_przychodow():
    with open("plusy.txt", "r") as file:
        for line in file:
            line = line.strip()
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

def dodawanie_wydatkow():
    with open("minusy.txt", "r") as file:
        for line in file:
            line = line.strip()
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

while True:
    while True:
        print("=====MENU=====")
        print("1.Przychód")
        print("2.Wydatkek")
        print("3.Podsumowania")
        print("==============")

        wybor = input("Co chcesz zrobić (wpisz 1, 2 lub 3):    ")

        if wybor == "1":
            dodawanie_pieniedzy(input("Ile: ",), input("kategoria: ",), input("data: "))
            dodawanie_przychodow()
            break
        elif wybor == "2":
            odejmowanie_pieniedzy(input("Ile: ",), input("kategoria: ",), input("data: "))
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

                    aktualne_pods = podsumowanie_miesiaca(ktory_miesiac, ktory_rok)

                    print(aktualne_pods)

                    break
                elif wybor == "2":
                    # liczenie salda
                    suma_przychodow = liczenie_salda_plus()
                    suma_wydatkow = liczenie_salda_minus()
                    saldo_laczne = suma_przychodow - suma_wydatkow
                    print(saldo_laczne)
                    break
                else:
                    print("Coś poszło nie tak...")
        else:
            print("Coś poszło nie tak...")



