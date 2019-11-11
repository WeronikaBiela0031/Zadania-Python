from math import gcd


#def NWW(a, b):
 #   """Compute the least common multiple."""
  #  return a * b // gcd(a, b)


def add_frac(frac1, frac2):
    total = [None, None]
    total[1] = frac1[1] * frac2[1]
    total[0] = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    nwd = gcd(total[0], total[1])
    result = [total[0] // nwd, total[1] // nwd]
    return result


def sub_frac(frac1, frac2):
    total = [None, None]
    total[1] = frac1[1] * frac2[1]
    total[0] = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    nwd = gcd(total[0], total[1])
    result = [total[0] // nwd, total[1] // nwd]
    return result


def mul_frac(frac1, frac2):
    total = [None, None]
    total[1] = frac1[1] * frac2[1]
    total[0] = frac1[0] * frac2[0]
    nwd = gcd(total[0], total[1])
    result = [total[0] // nwd, total[1] // nwd]
    return result


def div_frac(frac1, frac2):  # frac1 / frac2
    total = [None, None]
    total[1] = frac1[1] * frac2[0]
    total[0] = frac1[0] * frac2[1]
    nwd = gcd(total[0], total[1])
    result = [total[0] // nwd, total[1] // nwd]
    return result

def is_positive(frac):   # bool, czy dodatni
    if frac[0] > 0 and frac[1] > 0:
        total = True
    else:
       total = False
    return total

def is_zero(frac):  # bool, typu [0, x]
    if frac[0] == 0 and not frac[1] == 0:
        total = True
    else:
       total = False
    return total

def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    wynik = [None, None]
    wynik = sub_frac(frac1, frac2)
    if wynik[0] < 0 or wynik[1] < 0:
        total = -1
        msg = 'Argument pierwszy mniejszy niż drugi'
    elif wynik[0]>0 and wynik[1]>0:
        total = 1
        msg = 'Argument pierwszy większy niż drugi'
    else:
        total = 0
        msg = 'Argumenty są równe'
    return total

def frac2float(frac):  # konwersja do float
    total=frac[0]//frac[1]
    return total

f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 4], [1, 2]), [1, 4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 7], [7, 3]), [1, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 7], [3, 7]), [1, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([5,8]), True)
        self.assertEqual(is_positive([5, -8]),False)


    def test_is_zero(self):
        self.assertEqual(is_zero([0,8]), True)
        self.assertEqual(is_zero([5, -8]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 8],[1,8]), 0)
        self.assertEqual(cmp_frac([1, 8], [2, 8]), -1)
        self.assertEqual(cmp_frac([2, 8], [1, 8]), 1)
    def test_frac2float(self):
        self.assertEqual(frac2float([1,8]), 0.125)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
