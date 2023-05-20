mecze = input()
rozne = 0
for i in range(len(mecze)-1):
    if mecze[i] != mecze[i+1]:
        rozne += 1
print(rozne)