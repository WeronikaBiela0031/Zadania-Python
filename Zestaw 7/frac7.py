from math import gcd
from functools import total_ordering


class frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ZeroDivisionError("Mianownik musi być różny od 0")
        self.x = x
        self.y = y

        # Chce żeby obsługiwał floaty bez zmieniania w testach z 1 na 1.0
        #Nie! bo floaty to nie wymierny
        #self.x=float(x)
        #self.y=float(y)
        # try: #spróbuj zmienić int z float
        #     self.x=int(self.x)
        #     self.y=int(self.y)
        # except SyntaxError: #jak nie umiesz to tego nie rób
        #     continue

    def __str__(self):
        nwd = gcd(self.x, self.y)
        result = [self.x // nwd, self.y // nwd]
        if not result[1] == 1:
            return str(result[0]) + "/" + str(result[1])
        else:
            return str(result[0])

    def __repr__(self):
        nwd = gcd(self.x, self.y)
        result = [self.x // nwd, self.y // nwd]
        return "frac" + str(tuple(result))

    def __add__(self, other):
        total = frac(0)
        total.y = self.y * other.y
        total.x = self.x * other.y + other.x * self.y
        nwd = gcd(total.x, total.y)
        total.x = total.x // nwd
        total.y = total.y // nwd  # uwaga! licznik - i mianownik - trzeba zredukować!!!
        # import pdb; pdb.set_trace()
        return total

    def __radd__(self, other):
        return self.__add__(other)

    def sub_frac(self, other):
        total = frac(0)
        total.y = self.y * other.y
        total.x = self.x * other.y - other.x * self.y
        nwd = gcd(total.x, total.y)
        total.x = total.x // nwd
        total.y = total.y // nwd  # uwaga! licznik - i mianownik - trzeba zredukować!!!
        return total

    def mul_frac(self, other):
        total = frac(0)
        total.y = self.y * other.y
        total.x = self.x * other.x
        nwd = gcd(total.x, total.y)
        total.x = total.x // nwd
        total.y = total.y // nwd  # uwaga! licznik - i mianownik - trzeba zredukować!!!
        return total

    def div_frac(self, other):  # self / other
        total = frac(0)
        total.x = self.y * other.x
        total.y = self.x * other.y
        nwd = gcd(total.x, total.y)
        total.x = total.x // nwd
        total.y = total.y // nwd  # uwaga! licznik - i mianownik - trzeba zredukować!!!
        return total

    def is_positive(self):  # bool, czy dodatni

        if self.x > 0 and self.y > 0:
            total = True
        elif self.x < 0 and self.y < 0:
            total = True
        else:
            total = False
        return total

    def is_zero(self):  # bool, typu [0, x]

        if self.x == 0 and not self.y == 0:
            total = True
        else:
            total = False
        return total

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        self.x = -self.x
        return self

    @total_ordering
    def __eq__(self, other):

        wynik = self.sub_frac(other)
        if wynik.x == 0:
            return True
        else:
            return False

    def __lt__(self, other):
        wynik = self.sub_frac(other)
        if wynik.x < 0 and wynik.y > 0:
            return True
        elif wynik.x > 0 and wynik.y > 0:
            return True
        else:
            return False

    def frac2float(self):  # konwersja do float
        total = self.x / self.y
        return total

    def __invert__(self):  # odwrotnosc: ~frac
        result = frac(0)
        nwd = gcd(self.x, self.y)
        result.x = self.y // nwd
        result.y = self.x // nwd
        return result


f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        self.assertRaises(ZeroDivisionError, frac, 2, 0)

    def test_str_and_repr(self):
        self.assertEqual(str(frac(2, 3)), '2/3')
        self.assertEqual(repr(frac(2, 3)), 'frac(2, 3)')

    def test_add_frac(self):
        self.assertEqual(frac(1, 2) + frac(1, 3), frac(5, 6))
        self.assertEqual(frac(1, 2).__radd__(frac(1)), frac(3, 2))

    def test_sub_frac(self):
        self.assertEqual(frac(3, 4).sub_frac(frac(1, 2)), frac(1, 4))
        self.assertEqual(frac(3, 4).sub_frac(frac(1)), frac(-1, 4))

    def test_mul_frac(self):
        self.assertEqual(frac(3, 7).mul_frac(frac(7, 3)), frac(1))

    def test_div_frac(self):
        self.assertEqual(frac(3, 7).div_frac(frac(3, 7)), frac(1))

    def test_is_positive(self):
        self.assertEqual(frac(5, 8).is_positive(), True)
        self.assertEqual(frac(5, -8).is_positive(), False)
        self.assertEqual(frac(-5, -8).is_positive(), True)

    def test_is_zero(self):
        self.assertEqual(frac(0, 8).is_zero(), True)
        self.assertEqual(frac(5, -8).is_zero(), False)

    def test_cmp_frac(self):
        self.assertEqual(frac(1, 8) == frac(1, 8), True)
        self.assertEqual(frac(1, 8) != frac(2, 8), True)
        self.assertEqual(frac(1, 8) < frac(2, 8), True)
        # self.assertEqual(frac(2, 8) <= frac(1, 8), False)

    def test_pos_and_neg(self):
        self.assertEqual(frac(3, 4).__pos__(), frac(3, 4))
        self.assertEqual(frac(3, 4).__neg__(), frac(-3, 4))

    def test_frac2float(self):
        self.assertEqual(frac(1, 8).frac2float(), 0.125)

    def test_invert(self):
        self.assertEqual(frac(4, 3).__invert__(), frac(3, 4))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
