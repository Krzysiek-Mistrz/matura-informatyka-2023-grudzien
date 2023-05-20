mecze = input()
a, b = 0, 0
for i in range(len(mecze)):
    if mecze[i] == 'A':
        a += 1
    else:
        b += 1
    if a >= 1000 and a - b >= 3:
        print("wygrala A, majac: ", a, "B miala: ", b)
        break
    elif b >= 1000 and b - a >= 3:
        print("wygrala B, majac: ", b, "A miala: ", a)
        break