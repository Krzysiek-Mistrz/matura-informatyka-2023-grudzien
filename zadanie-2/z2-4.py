pairs = []

with open('../informatyka-2022-grudzien-probna-rozszerzona-zalaczniki/Dane_2212/pary.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        pairs.append((a, b))

for pair in pairs:
    liczba0, liczba1 = pair[0], pair[1]
    while liczba0 < liczba1:
        liczba1 //= 2
    if liczba0 == liczba1:
        print(pair[0], pair[1])