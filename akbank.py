from datetime import datetime


class Pizza:
    def __init__(self, description, fiyat):
        self._description = description
        self.fiyat = fiyat

    def get_description(self):
        print (self._description)

    def get_cost(self):
        return self._price
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza, Malzemeler: peynir", 20.00)


class TurkPızzam(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza, Malzemeler: Keçi Peyniri", 30.0)

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza, Malzemeler: mozzarella peyniri ve domates", 25.00)


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

class Sade_Pizza(Pizza):
        def __init__(self):
                super().__init__("Sadeli Pizzam, Malzemeler: mozzarella peyniri ", 35.00)

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "Zeytin Soslu"

    def get_cost(self):
        return self.component.get_cost() + 1.5

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Mantarlar(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "Ekstra:mantarlı piizzam"

    def get_cost(self):
        return self.component.get_cost() + 2.0

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Keçili(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "full:Keçili"

    def get_cost(self):
        return self.component.get_cost() + 3.5

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Et(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "dopdolu:etli"

    def get_cost(self):
        return self.component.get_cost() + 4.0

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Sogan(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "full:Soğanlı"

    def get_cost(self):
        return self.component.get_cost() + 1.0

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Misir(Decorator):
    def __init__(self, pizza):
        self.component = pizza
        self._description = "full: mısırlı sosu"

    def get_cost(self):
        return self.component.get_cost() + 1.5

    def get_description(self):
        return self.component.get_description() + ' ' + self._description
def print_menu():
    with open('Menu.txt', 'r') as format:
        print(format.read())


def get_pizza():
    while True:
        choice = input("Lütfen bir pizza tabanı seçiniz (1-4): ")
        if choice == '1':
            return KlasikPizza()
        elif choice == '2':
            return MargaritaPizza()
        elif choice == '3':
            return TurkPızzam()
        elif choice == '4':
            return Sade_Pizza()
        else:
            print("Geçersiz giriş. Lütfen 1-4 arasında bir değer giriniz.")


class KeciPeyniri:
    pass


def get_sec(pizza):
    while True:
        secim = input("Lütfen bir sos seçiniz (11-16): ")
        if secim == '1':
            return Zeytin(pizza)
        elif secim == '2':
            return Mantarlar(pizza)
        elif secim == '3':
            return KeciPeyniri(pizza)
        elif secim == '4':
            return Et(pizza)
        elif secim == '5':
            return Sogan(pizza)
        elif secim == '6':
            return Misir(pizza)
        else:
            print("Geçersiz tekrar deneyiniz.")
            break


def place_order():
    print_menu()
    pizza = get_pizza()
    sec = get_sec(pizza)
    print("gir:", sec.get_description())
    print(" fiyat:", sec.get_cost())
    ad = input("isim git: ")
    kart = int(input("kart bilgini gir "))
    kart_sifre = input("sifreni gir ")
    kimlik_bilgilerim = int(input("kimlik bilgnizi inteher giriniz: "))

    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bul = [sec.get_description(), ad, kimlik_bilgilerim, kart, get_sec, kart_sifre]
    with open('Orders_Database.csv', 'a', end='') as format:
        writer = kart_sifre.writer(format)
        writer.writerow(bul)
    print("siparişiniz alındı")


if __name__ == '__main__':
    place_order()

with open("Menu.txt", "w") as format:
    format.write(" seç")
    format.write("1: Klasik")
    format.write("2: Margaritalı")
    format.write("3: TürkPizzalı")
    format.write("4: Sade pizzam")
    format.write("11:sosu giriniz")
    format.write("5: zeytin ezmeli")
    format.write("6: Mantarlı")
    format.write("7: et")
    format.write("8: keçi")
    format.write("9: mısır")
    format.write("10: Soğan")
    format.write("*Teşekkür ederim")