# 1
def listy(lista1, lista2):
    lista = []
    for a in lista1:
        if lista1[a] % 2 == 0:
            lista.append(a)
    for b in lista2:
        if lista2[b] % 2 == 1:
            lista.append(b)
    return lista


lista_pierwsza = [2, 5, 2, 5, 2, 5, 2]
lista_druga = [5, 2, 5, 2, 5, 2, 5]

nowa = listy(lista_pierwsza, lista_druga)
print(nowa)


# 2
def druga(data_text):
    slownik = {"długość: ": len(data_text), "lista znaków: ": list(data_text), "duże litery: ": data_text.upper(), "małe litery: ": data_text.lower()}
    return slownik

string = 'Ala ma kota, a kot ma Alę'
print(druga(string))


# 3
def trzecia(text, letter):
    text = text.lower()
    text = list(text)
    for x in text:
        if x == letter:
            text.remove(letter)
    return text


print(trzecia('Ala ma kota', 'a'))


# 4
def czwarta(temperature_type):
    int(temperature_type)
    F = (9 / 5) * temperature_type + 32
    R = temperature_type * 1.8 + 491.67
    K = temperature_type + 273.15
    wynik = {'Fahrenheit: ': F, 'Rankine: ': R, 'Kelwin: ': K}
    return wynik

print(czwarta(30))


# 5
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(a, b):
        wynik = a + b
        return wynik

    def difference(a, b):
        wynik = a - b
        return wynik

    def multiply(a, b):
        wynik = a * b
        return wynik

    def divide(a, b):
        wynik = a / b
        return wynik

print(Calculator.add(5, 7))
print(Calculator.difference(5, 7))
print(Calculator.multiply(5, 7))
print(Calculator.divide(5, 7))

# 6
class ScienceCalculator(Calculator):
    def potęgowanie(a, b):
        wynik = a ** b
        return wynik

print(ScienceCalculator.potęgowanie(5, 3))

# 7
def wypisz(tekst):
    return print(tekst[::-1])

wypisz("Arbuz")

# 8
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def update_file(text_data):
        dodaj = open('file_manager.py', 'w', encoding='utf-8')
        dodaj.write(text_data)
        dodaj.close()

    def read_file(self):
        dodaj = open('file_manager.py', 'r', encoding='utf-8')
        dane = dodaj.read()
        print(dane)
        dodaj.close()


FileManager.update_file('no elo')
FileManager.read_file()
