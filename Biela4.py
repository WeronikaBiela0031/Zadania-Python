print('Zadanie 4.2')
print('Ad Zadanie 3.5')
N = int(input('Podaj dlugosc miarki (liczba całkowita): '))
#import pdb;pdb.set_trace() do programu PyCharm, działa przy Run, sprawdzanie kolejnej komendy poprzez (n Enter)
#do programu PyCharm ctr+alt+L poprawia składniena Pythonowska

def miarka(n):
    '''Funkcja rysująca miarkę '''
    i = 0
    X = ' |'
    Y = '0   '

    while i < n:
        X = X + '...|'
        i1 = str(i + 1)
        Y = Y + i1 + '   '
        i += 1

    return print(X, '\n', Y)


miarka(N)

print('Ad Zadanie 3.6')

N1 = int(input('Podaj liczbe kwadratow w wierszu: '))
N2 = int(input('Podaj liczbe kwadratow w kolumnie: '))


def kwadraciki(n1, n2):
    '''Funkcja rysująca kwadraciki '''
    i = 0
    j = 0

    if n1 == 0 or n2 == 0:
        return print('Nie mam co wydrukować jeśli jest 0 wierszy lub kolumn')
    else:
        X = '+'
        Y = '|'
        Z = ''
        while j < n2:
            while i < n1:
                X = X + '---+'
                Y = Y + '   |'
                i += 1
            # string Z będzie moim wierszem
            Z = Z + X + '\n' + Y + '\n'
            j += 1
        return print(Z + X)


kwadraciki(N1, N2)
# input('Naciśnij Enter aby kontynuuować.')


print('Zadanie 4.3')
N = int(input('Podaj argument funkcji silnia: '))


def factorial(n):
    i = 1
    silnia = 1
    if n == 0:
        return silnia
    else:
        while i < n + 1:
            silnia = silnia * i
            i += 1
        return silnia


print(factorial(N))
# input('Naciśnij Enter aby kontynuuować.')

print('Zadanie 4.4')
N = int(input('Podaj numer wyrazu ciągu Fibonacciego, który chcesz obliczyć: '))


def fibonacci(n):
    F = [0, 1]
    i = 2
    fibonacci = 1
    if n == 0 or n == 1:
        return n

    else:
        while i < n + 1:
            f = sum(F)
            F[0] = F[1]
            F[1] = f
            i += 1
        return F[1]


print(fibonacci(N))

print('Zadanie 4.5')
print('Wersja interacyjna')
input('Naciśnij Enter aby kontynuuować.')
L5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# left-wartość elementu n-tego listy (pierwszy występujący)
# right-wartosc elementu m-tego listy (pierwszy występujący po elemencie left)
def odwracanie_listy_it(L, left, right):
    n = L.index(left)
    m = L.index(right)
    L3 = L[n:m + 1]
    L3.reverse()
    L2 = L[:n] + L3 + L[m + 1:]
    return L2


print(odwracanie_listy_it(L5, 3, 8))

print('Wersja rekurencyjna')
input('Naciśnij Enter aby kontynuuować.')


def odwracanie_listy_rek(L, left, right):
    # nie wiem jak rozumieć rekurencje- poprez ustalanie ze ostatni wyraz innej listy to kolejny nowej?
    j = 0
    n = L.index(left)
    m = L.index(right)
    L2 = L[n:m + 1]  # wycinam co chce obrócić, mogłabym nie tworzyć L1 ale to nie robi różnicy
    L22 = []  # pusta lista ktora bedzie tworzona
    while len(L2) > 0:
        L22.append(L2.pop())
        j += 1
    L3 = L[:n] + L22 + L[m + 1:]
    return L3


print(odwracanie_listy_rek(L5, 3, 8))

print('Zadanie 4.6')
input('Naciśnij Enter aby kontynuuować.')
L6 = [1, 2, (3, 7), [4, 5, 6], 7, 8, 9, 10]


def sum_seq(S):
    wynik = 0
    if isinstance(S, (list, tuple)):
        for i in S:
            try:
                wynik += sum(i)
            except TypeError:
                wynik += i

        return wynik


    else:
        return "Argument nie jest sekwencją"


print(sum_seq(L6))

print('Zadanie 4.7')
input('Naciśnij Enter aby kontynuuować.')
L7 = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]


def flatten(Sn, first=True):
    # import pdb; pdb.set_trace()
    '''Funkcja wypisująca elemanty listy zagnieżdżonej'''
    if first:  # przy pierwszym wejsciu ma domyślną wartość, więc wchodzi w ta pętle
        flatten.lista = []  # definiuje sobie pusta "liste", dodaje to jako atrybut funkcji
    for i in Sn:

        if not isinstance(i, (list, tuple)):
            flatten.lista.append(i)

        else:
            flatten(i, False)
    return flatten.lista


print(flatten(L7))
