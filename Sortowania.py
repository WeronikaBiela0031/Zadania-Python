def swap(L, left, right):
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]


def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i + 1, right + 1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)


def insertsort(L, left, right):
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):  # od prawej do lewej (bez left)
            if L[j - 1] > L[j]:
                swap(L, j - 1, j)  # zamiana sąsiadów


def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j + 1]:
                swap(L, j + 1, j)


def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)  # element podziału
    pivot = left  # przesuń do L[left]
    for i in range(left + 1, right + 1):  # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)  # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:  # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left + 1):
        L[left + i] = T[i]


def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2  # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)  # scalanie
