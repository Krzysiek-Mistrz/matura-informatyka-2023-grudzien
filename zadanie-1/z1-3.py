with open('../informatyka-2022-grudzien-probna-rozszerzona-zalaczniki/Dane_2212/mecz_przyklad.txt', 'r') as plik:
    mecze = plik.read()

Passa = 0
najdluzszaPassa = 0
obecnyZwyciezca = ''
poprzedniZwyciezca = ''
dobraPassa = 0

for element in mecze:
    if element == 'A':
        obecnyZwyciezca = 'A'
    else:
        obecnyZwyciezca = 'B'

    if obecnyZwyciezca == poprzedniZwyciezca:
        Passa += 1
    else:
        if Passa >= 10:
            dobraPassa += 1
        Passa = 1

    if Passa > najdluzszaPassa:
        najdluzszaPassa = Passa
        zwyciezca = obecnyZwyciezca

    poprzedniZwyciezca = obecnyZwyciezca

with open('wyniki1.txt', 'w') as plik:
    plik.write('zad. 3.3\n')
    plik.write('1. Liczba dobrych pass: {}\n'.format(dobraPassa))
    plik.write('2. Najdłuższa dobra passa: {} (drużyna {})\n'.format(najdluzszaPassa, zwyciezca))
