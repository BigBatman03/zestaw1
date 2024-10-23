# #zad 1

# from audioop import reverse
# import random


# lista = []

# for i in range(0,10):
#     los = random.randint(-10,10)
#     lista.append(los)
# print(lista)
# print("Max: ", max(lista))
# print("Min: ", min(lista))
# srednia = sum(lista)/len(lista)
# print("Avg: ", srednia)
# mniejsze = 0
# wieksze = 0
# for i in range(0, len(lista)):
#     if lista[i] < srednia:
#         mniejsze += 1
#     elif lista[i] > srednia:
#         wieksze += 1
# print("Ilosc mniejszych: ", mniejsze)
# print("Ilosc wiekszych: ", wieksze)
# lista.reverse()
# print(lista)

#zad 2------------

import random

lista = []

for i in range(0,20):
    los = random.randint(1,10)
    lista.append(los)
print(lista)

for i in range(1, 11):
    ilosc = 0
    for j in range(0, len(lista)):
        if i == lista[j]:
            ilosc += 1
    print(i, ":", ilosc)

#zad 3-----------

# import random

# lista = [[]]

# for i in range(0,5):
#     for j in range(0,5):
#         los = random.randint(-5,5)
#         lista.append(los)
