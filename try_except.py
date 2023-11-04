cena = input('Wprowadz cene ')

try:
    cena = float(cena)
    print('zrzutowano do float')

except:
    print('Cena ma typ ',type(cena))
    cena = 100
    print('zla cena, przyjmuję 100')

wynik = cena * 2.1

print(wynik)