print('Zadanie 8.1')
# Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0.
# Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa.
# Podać implementację algorytmu w Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.

# Twierdzenie: Równanie diofantyczne ax + by = c ma rozwiązanie wtedy i tylko wtedy, gdy NWD(a, b) jest dzielnikiem liczby c.
# jeżeli x0, y0 jest takim/ ozwiązaniem, to wszystkie inne rozwiązania mają postać x = x0 +b/dt, y = y0 −a/dt, t ∈ N
from math import gcd


def solve(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""

    if c % gcd(a, b) == 0:  # dzielenie z reszta
        if b==0 and a==0:
            return print("Rozwiązaniem jest cała płaszczyzna")
        elif b == 0:
            x = -c / a
            return print("Rozwiązaniem jest pionowa prosta przechodząca przez", x)
        elif a == 0:
            y = -c / b
            return print("Rozwiązaniem jest pozioma prosta przechodząca przez", y)
        else:  # przykładowe rozwiązanie
            x1 = 0
            z = -c / b
            y2 = 0

            return ("Prosta przechodząca przez punkt", (x1 , z), "oraz punkt", (z, y2))
    else:
        return print("Równanie nie ma rozwiązania")

print(solve(0,1,2))
print(solve(2,3,4))

print('Zadanie 8.3')

# Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie punktów z kwadratu z wpisanym kołem. Sprawdzić zależność dokładności wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.
import random


def calc_pi(k=100):
    n0 = 0
    n = 0
    i = 0
    while i < k:
        x = random.random()
        y = random.random()
        n += 1 #liczba wszystkich losowań
        i += 1
        if (x ** 2 + y ** 2) ** 0.5 < 1: #liczba w polu koła
            n0 += 1

    return 4*(n0 / n)

    # """Obliczanie liczby pi metodą Monte Carlo.
    # n oznacza liczbę losowanych punktów."""

print(calc_pi(100))
print(calc_pi(1000))
# mamy kwadrat o boku 2r i polu 4r^2, pole koła wpisanego jest pir^2
# n0 to liczba punktów które trafią do okręgu, n wszystki punkty wylosowane
# n0/n = pi/4
# Uwaga pracujemy w pierwszej ćwiartce!


print('Zadanie 8.4')


# Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami jego boków.
# Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.

def heron(a, b, c):
    try:
        if a + b < c or b + c < a or c + a < b:
            raise ValueError('Nie jest spełniona nierówność trójkąta')
    except ValueError as e:
        print(e)
    else:
        p = 0.5 * (a + b + c)
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return S

print(heron(1,0.1,0.1))
print(heron(1,1,1.41)) #bo wiem że jest ok. 0.5

print('Zadanie 8.6')
# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.
# wartości w tablicy
# P(0, 0) = 0.5, P(i, 0) = 0.0 dla i > 0, P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i - 1, j) + P(i, j - 1)) dla i > 0, j > 0.

# pierwszy problem obliczyć wartości dla jednej kratki
# w programowaniu dynamiczym zapiszemy te kratki żeby później już nie musieć ich liczyć!
a = int(input("Wprowadz numer wiersza oblicznej wartości tablicy P "))
b = int(input("Wprowadz numer kolumny obliczanej wartości tablicy P "))
P = dict()
#P = {'(0,0)':0.5, '(1,0)':0, '(0,1)':1} #słownik
for i in range(a):
    if i == 0:
        P[(i,0)] = 0.5 #pierwszy (0,0)
        for j in range(b):
            if j==0:
                pass
            else:
                P[(0,j)] = 1
    else:
        P[(i,0)] = 0
        for j in range(b):
            if j == 0:
                pass
            else:
                P[(i,j)] = 0.5 * (P[(i - 1, j)] + P[(i, j - 1)]) #(1,1)


print(P[(a-1,b-1)])
print(P[(1,1)])
#print(P[(2,5)])