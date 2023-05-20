tablica = []
for i in range(16):
    tablica.append(i)
with open("../informatyka-2022-grudzien-probna-rozszerzona-zalaczniki/Dane_2212/liczby_przyklad.txt", "r") as plik:
    liczby = [int(x) for x in plik]
for i in tablica:
    ileRazy = 0
    for j in liczby:
        liczba = hex(j)[2:]
        for k in liczba:
            if k == hex(i)[2:]:
                ileRazy += 1
    print(f"{i}:{ileRazy}")

"""
import collections

with open("liczby.txt", "r") as plik:
    liczby = [int(x) for x in plik]

counter = collections.Counter()
for liczba in liczby:
    hex_str = hex(liczba)[2:]
    counter.update(hex_str)

for i in range(16):
    hex_digit = hex(i)[2:].upper()
    count = counter[hex_digit]
    print(f"{hex_digit}:{count}")
"""