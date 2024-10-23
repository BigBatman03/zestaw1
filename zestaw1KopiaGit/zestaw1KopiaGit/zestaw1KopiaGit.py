#zad 1 ------------

# waga = float(input("Podaj wage (kg): "))
# wzrost = float(input("Podaj wzrost (m): "))

# if waga <= 0 or wzrost <= 0:
#     print("Nieprawidlowe dane")
# else:
#     bmi = waga/(wzrost**2.0)
#     print("BMI: ", bmi)
#     if bmi >= 18.5 and bmi <= 24.9:
#         print("waga prawidlowa")
#     elif bmi < 18.5:
#         print("niedowaga")
#     elif bmi > 24.9:
#         print("nadwaga")


#zad 2-------------

# cena = float(input("Podaj cene towaru:"))
# liczbaRat = int(input("Podaj liczbe rat:"))
# rata = 0

# if not(cena >= 100 and cena <= 10000 and liczbaRat >= 6 and liczbaRat <= 48):
#     print("Nieprawidlowe dane")
# else:
#     if liczbaRat >= 6 and liczbaRat <= 12:
#         rata = cena/liczbaRat + cena*0.025
#     elif liczbaRat >= 13 and liczbaRat <= 24:
#         rata = cena/liczbaRat + cena*0.05
#     elif liczbaRat >= 25 and liczbaRat <= 48:
#         rata = cena/liczbaRat + cena*0.1
#     print("Miesieczna rata wynosi: ", rata)



#zad 3-------------

# liczba = int(input("Podaj pierwsza liczbe calkowita: "))
# liczba2 = int(input("Podaj druga liczbe calkowita: "))

# wieksza = max(liczba,liczba2)
# mniejsza = min(liczba,liczba2)


# if liczba > 0 and liczba2 > 0:
#     if mniejsza%2 == 0:
#         mniejsza+=1
#         while mniejsza<=wieksza:
#             print(mniejsza,end=" ")
#             mniejsza = mniejsza+2
#     else:
#         while mniejsza<=wieksza:
#             print(mniejsza,end=" ")
#             mniejsza = mniejsza+2
# else:
#     print("Nieprawidlowe dane.")


#zad 4-------------

# n = int(input("Podaj liczbe n: "))
# baza = int(input("Podaj liczbe bazowa: "))
# potega = 1

# if n > 0 and baza > 0:
#     while potega <= n:
#         print(potega)
#         potega *= 2

#     print("Dla liczby bazowej",sep="")
#     potega = 1
#     while potega <= n:
#         print(potega)
#         potega *= baza
# else:
#     print("Nieprawidlowe dane")

#zad 5--------------

# suma = 0
# while True:
#     x = int(input("Podaj liczbe: "))
#     suma += x
#     if x == 0:
#         break
# print("Suma wynosi: ", suma)

#zad 6----------------

# suma = 0
# ilosc = 0
# liczby = []

# while True:
#     x = int(input("Podaj liczbe: "))
#     if x == 0:
#         break
#     liczby.append(x)
#     suma += x
#     ilosc += 1

# print("Podane liczby: ", liczby)
# Max = max(liczby)
# Min = min(liczby)
# sumaMinMax = Max + Min
# srednia = suma/ilosc
# print("Suma min i max = ", sumaMinMax )
# print("Srednia arytmetyczna = ", srednia )

#zad 7---------------

# import random

# poziomTrudnosci = int((input("Wybierz poziom trudnosci (od 1 do 3): ")))
# if poziomTrudnosci == 1:
#     Min = 1
#     Max = 50
# elif poziomTrudnosci == 2:
#     Min = 1
#     Max = 100
# elif poziomTrudnosci == 3:
#     Min = 1
#     Max = 200
# else:
#     print("Nieprawidlowy wybor")

# liczba = random.randint(Min,Max)
# ilosc = 0

# while True:
#     guess = int(input("Podaj liczbe: "))
#     ilosc += 1
#     if guess > liczba:
#         print("Podales za duza wartosc")
#     elif guess < liczba:
#         print("Podales za mala wartosc")
#     elif guess == liczba:
#         print("Gratulacje")
#         break
# print("Ilosc prob: ", ilosc)

#zad 8-------------

# cyfryStr = []
# cyfryInt = []
# suma = 0
# sumaParzystych = 0
# sumaNieParzystych = 0
# iloscP = 0
# iloscNP = 0
# sredniaP = 0
# sredniaNP = 0
# liczba = int(input("Podaj liczbe: "))
# slowo = str(liczba)
# if liczba < 0:
#     print("Nieprawidlowe dane")
# else:
#     for i in slowo:
#         cyfryStr.append(i)
#     for j in cyfryStr:
#         cyfryInt.append(int(j))
#     for cyfra in cyfryInt:
#         suma += cyfra
#         if cyfra%2 == 0:
#             sumaParzystych += cyfra
#             iloscP += 1
#         else:
#             sumaNieParzystych += cyfra
#             iloscNP += 1
#     print("Suma cyfr: ", suma)
#     if iloscP != 0:
#         sredniaP = sumaParzystych/iloscP
#     if iloscNP != 0:
#         sredniaNP = sumaNieParzystych/iloscNP
#     print("Stosunek srednich cyfr parzystych do cyfr nieparzystych: ", sredniaP, ":", sredniaNP)
    
#     liczba2 = int(input("Podaj druga liczbe: "))
#     cyfryStr2 = []
#     cyfryInt2 = []
#     suma2 = 0
#     slowo2 = str(liczba2)
#     for i in slowo2:
#         cyfryStr2.append(i)
#     for j in cyfryStr2:
#         cyfryInt2.append(int(j))
#     for cyfra in cyfryInt2:
#         suma2 += cyfra
#     print("Stosunek sum obu liczb: ",suma , ":", suma2)

#zad 9------------

# def CzyDoskonala(dzielniki):
#     if suma - dzielniki[-1] == liczba:
#         print("Podana liczba jest liczba doskonala.")
#     else:0
#         print("Podana liczba nie jest liczba doskonala.")

# liczba = int(input("Podaj liczbe: "))
# dzielniki = []
# suma = 0
# for i in range(1, liczba+1):
#     if liczba%i == 0:
#         dzielniki.append(i)
#         suma += i
# print("Dzielniki liczby: ", dzielniki)
# CzyDoskonala(dzielniki)


#zad 10-------------

# def czyPierwsza(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def Wyswietl():
#     liczbyPierwsze = []
#     for i in range(2, n + 1):
#         if czyPierwsza(i):
#             liczbyPierwsze.append(i)
#     print(liczbyPierwsze)

# n = int(input("Podaj liczbe: "))

# if n > 1:
#     if czyPierwsza(n):
#         print("Liczba", n, "jest liczba pierwsza.")
#     else:
#         print("Liczba", n, "nie jest liczba pierwsza.")
#     Wyswietl()
# else:
#     print("Nieprawidlowe dane")

#zad 11

# def uklad(a1, b1, c1, a2, b2, c2):
#     wyznacznik = a1 * b2 - a2 * b1
#     if wyznacznik == 0:
#         print("Uklad rownan nie ma jednoznacznego rozwiazania.")
#         return
#     x = (c1 * b2 - c2 * b1) / wyznacznik
#     y = (a1 * c2 - a2 * c1) / wyznacznik
#     print("Rozwiazanie ukladu rownan: ")
#     print("x = ", x)
#     print("y = ", y)

# a1 = float(input("Podaj wspolczynnik a1: "))
# b1 = float(input("Podaj wspolczynnik b1: "))
# c1 = float(input("Podaj wspolczynnik c1: "))
# a2 = float(input("Podaj wspolczynnik a2: "))
# b2 = float(input("Podaj wspolczynnik b2: "))
# c2 = float(input("Podaj wspolczynnik c2: "))

# uklad(a1, b1, c1, a2, b2, c2)


