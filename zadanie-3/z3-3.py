"""import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# wczytywanie liczb z pliku
with open("../informatyka-2022-grudzien-probna-rozszerzona-zalaczniki/Dane_2212/liczby_przyklad.txt") as f:
    numbers = [int(x) for x in f.readlines()]

min_solutions = float("inf")
max_solutions = 0
number_with_max_solutions = -1
number_with_min_solutions = -1

for n in numbers:
    solutions = 0
    for i in range(2, n):
        if is_prime(i) and is_prime(n-i):
            solutions += 1
    if solutions < min_solutions:
        min_solutions = solutions
        number_with_min_solutions = n
    if solutions > max_solutions:
        max_solutions = solutions
        number_with_max_solutions = n
    print(f"Liczba {n} ma {solutions} rozkladów na sumę dwóch liczb pierwszych")

print(f"Liczba z największą ilością rozkładów na sumę dwóch liczb pierwszych: {number_with_max_solutions}, liczba rozkładów: {max_solutions}")
print(f"Liczba z najmniejszą ilością rozkładów na sumę dwóch liczb pierwszych: {number_with_min_solutions}, liczba rozkładów: {min_solutions}")
"""

import math

def sito(tab, n):
    for i in range(2, int(math.sqrt(n))+1):
        if(tab[i]):
            for j in range(i*i, n, i):
                tab[j] = False

tab = [True for i in range(1000000)]
tab[0], tab[1] = False, False

sito(tab, 1000000)

ileMax, ileMin = -1000000, 1000000
maxLiczba, minLiczba = 0, 0

with open("../informatyka-2022-grudzien-probna-rozszerzona-zalaczniki/Dane_2212/liczby_przyklad.txt", "r") as plik:
    for liczba in plik:
        ile = 0
        liczba = int(liczba)
        rozklad0, rozklad1 = 2, liczba-2
        while rozklad0 <= rozklad1:
            if tab[rozklad0] and tab[rozklad1]:
                ile += 1
            rozklad0 += 1
            rozklad1 = liczba - rozklad0
        if ile > ileMax:
            ileMax = ile
            maxLiczba = liczba
        if ile < ileMin:
            ileMin = ile
            minLiczba = liczba
print(maxLiczba, ileMax)
print(minLiczba, ileMin)