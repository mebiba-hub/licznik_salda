
# 📊 Wyświetlać podsumowanie miesiąca

print("Witaj w apce do kontrolowania budrzetu")

imiona = ["w", "d"]
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

def dodawanie_przychodow():
    with open("plusy.txt", "r") as file:
        for line in file:
            line = line.strip()
            ilosc, kategoria, data = line.split(",")
            przychody.append({
                "ile": float(ilosc),
                "kategoria": kategoria,
                "data": data
            })

def dodawanie_wydatkow():
    with open("minusy.txt", "r") as file:
        for line in file:
            line = line.strip()
            ilosc, kategoria, data = line.split(",")
            wydatki.append({
                "ile": float(ilosc),
                "kategoria": kategoria,
                "data": data
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
            dodawanie_pieniedzy(input("Ile",), input("kategoria",), input("data"))
            dodawanie_przychodow()
            break
        elif wybor == "2":
            odejmowanie_pieniedzy(input("Ile",), input("kategoria",), input("data"))
            dodawanie_wydatkow()
            break
        elif wybor == "3":
            while True:
                print("==============")
                print("1.Podsumowanie miesiąca")
                print("2.Twoje saldo")
                print("==============")

                wybor = input("Co chcesz zrobić (wpisz 1 lub 2):    ")

                if wybor == "1":#Jeszcze nie ma
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



