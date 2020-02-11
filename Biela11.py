print('Zadanie 11.1')
import random


# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do N-1 w kolejności losowej,

# N = int(input('Podaj liczbę elementów listy (N): '))

def random_list(N):
    L = list(range(N))
    random.shuffle(L)
    return L


print(random_list(10))


# by int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)

def almost_sorted(N):
    L = list(range(N))

    for i in range(N):
        item = L[i]
        a = random.randint(-1, 2)
        if a == -1:
            if i == 0:
                pass
            else:
                s = L[i - 1]
                L[i - 1] = item
                L[i] = s

        if a == 1:
            if i == N - 1:
                pass
            else:
                s = L[i + 1]
                L[i + 1] = item
                L[i] = s
    return (L)


print(almost_sorted(10))


# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
def almost_sorted_reverse(N):
    L = list(range(N))
    L.reverse()
    for i in range(N):
        item = L[i]
        a = random.randint(-1, 2)
        if a == -1:
            if i == 0:
                pass
            else:
                s = L[i - 1]
                L[i - 1] = item
                L[i] = s

        if a == 1:
            if i == N - 1:
                pass
            else:
                s = L[i + 1]
                L[i + 1] = item
                L[i] = s
    return (L)


print(almost_sorted_reverse(10))


# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
def random_list_gauss(N):
    L = [None] * N
    for i in range(N):
        L[i] = random.gauss(0, 1)
    return (L)


print(random_list_gauss(10))

# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).
from math import floor


def special_random_list(N):
    L = [None] * N
    k = floor(N ** 0.5)
    for i in range(N):
        L[i] = random.randint(0, k)
    return (k, L)


print(special_random_list(10))

print('Zadanie 11.4')
from Sortowania import *


def time_sort(algorytm, L, j, k):
    import time
    start_time = time.perf_counter()
    algorytm(L, j, k)
    end_time = time.perf_counter()
    time_total = end_time - start_time
    return time_total


lengths = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

for i in lengths:
    print('Times for lists of {} elements'.format(i))
    L = random_list(i)
    time_quicksort = time_sort(quicksort, L, 0, i-1)
    time_selectsort = time_sort(selectsort, L, 0, i-1)
    time_bubblesort = time_sort(bubblesort, L, 0, i-1)
    time_mergesort = time_sort(mergesort, L, 0, i-1)

    print("Quicksort {q} \nSelectsort {s} \nBubblesort {b} \nMergesort {m}".format(q=time_quicksort,
                                                                                    s=time_selectsort,
                                                                                    b=time_bubblesort,
                                                                                    m=time_mergesort))

