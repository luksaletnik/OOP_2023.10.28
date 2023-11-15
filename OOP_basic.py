class Auto:
    def __init__(self, barwa, stan, wiek):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = stan
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023 - wiek

    def tryb_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 10

    def tryb_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def zmien_tryb(self, tryb):
        if tryb.lower() == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
            print(f'Wlaczono tryb ECO')
        elif tryb.lower() == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
            print(f'Wlaczono tryb NORMAL')
        else:
            self.tryb_eco()
            print(f'Nie rozpoznano wyboru, zostawiam tryb ekonomiczny')


auto_Lukasza = Auto('zielone', 4, 12)
print(auto_Lukasza.kolor)
auto_Lukasza.kolor = 'niebieskie'
print(auto_Lukasza.kolor)
print(f'Spalanie na 100 km w trybie NORMAL: {auto_Lukasza.spalanie_na_100} l')
auto_Lukasza.tryb_eco()
auto_Lukasza.tryb_normal()
print(f'Spalanie na 100 km po zmianie na tryb ECO: {auto_Lukasza.spalanie_na_100} l')
print(f'Przejedziesz jeszcze {auto_Lukasza.zasieg()} km')
auto_Lukasza.zmien_tryb('eco')
auto_Lukasza.zmien_tryb('ECO')
