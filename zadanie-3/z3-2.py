import math

def Pierwsza(liczba):
	if liczba <= 1:
		return False
	else:
		for i in range(2, int(math.sqrt(liczba))+1):
			if not liczba % i:
				return False
	return True

ileLiczb = 0

for i in range(100):
	liczba = int(input()) - 1
	if Pierwsza(liczba):
		ileLiczb += 1

print(ileLiczb)