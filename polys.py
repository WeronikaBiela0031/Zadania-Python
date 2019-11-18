class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka (Algorytmy w C++) - tworzymy wielomian c*x^n- jednomian: (współczynnik, potęga)
    def __init__(self, c=0, n=0):  # konstruktor tworzy jednomian, potem je dodajemy
        self.size = n + 1  # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size - 1] = c

    def __str__(self):
        return str(self.a)

    def __eq__(self, other):  # obsługa poly1 == poly2
        return (self.a == other.a)

    def __ne__(self, other):  # obsługa poly1 != poly2
        return not self == other

    def __add__(self, other):  # poly1 + poly2
        result = Poly(0)
        if self.size > other.size:
            result.size = self.size
        else:
            result.size = other.size

        result.a = result.size * [0]
        for i in range(self.size):
            result.a[i] += self.a[i]
        for j in range(other.size):
            result.a[j] += other.a[j]
        return result

    def __sub__(self, other):  # poly1 - poly2
        result = Poly(0)
        if self.size > other.size:
            result.size = self.size
        else:
            result.size = other.size

        result.a = result.size * [0]
        for i in range(self.size):
            result.a[i] += self.a[i]
        for j in range(other.size):
            result.a[j] -= other.a[j]
        return result

    def __mul__(self, other):  # poly1 * poly2
        result = Poly(0)
        result.size = self.size + other.size - 1
        result.a = result.size * [0]

        for i in range(self.size):
            for j in range(other.size):
                result.a[i + j] += self.a[i] * other.a[j]
        return result

    def __pos__(self):  # +poly1 = (+1)*poly1- nie mam pojęcia co ta funkcja ma robić
        return self

    def __neg__(self):  # -poly1 = (-1)*poly1- także nie mam pojęcia co ta funkcja ma robić (brak testu)
        result = Poly(0)
        result.a = self.size * [0]
        result.size = self.size
        # import pdb; pdb.set_trace()
        for i in range(result.size):
            result.a[i] = -self.a[i]
        return result

    def eval(self, x):
        pass  # schemat Hornera dla jednomianu? mohe założyć że to nie jest jednomian ale i tak test musi być dla jednomianu!

    def combine(self, other):  # złożenie poly1(poly2(x))
        result = Poly(0)
        result.size = (self.size - 1) * (other.size - 1) + 1
        result.a = result.size * [0]
        for i in range(self.size):
            for j in range(other.size):
                result.a[i * j] += self.a[i] * (other.a[j] ** i)
        return result

    def __pow__(self, n):  # poly(x)**n lub pow(poly(x),n)
        result = Poly(0)
        result.size = (self.size - 1) * n + 1
        result.a = result.size * [0]
        for i in range(self.size):
            result.a[i * n] += self.a[i] ** n
        return result

    def diff(self):  # różniczkowanie
        result = Poly(0)
        result.size = self.size - 1
        result.a = result.size * [0]
        for i in range(self.size):
            if i == 0:
                continue
            result.a[i - 1] += self.a[i] * (self.size - 1)
        # del result.a[-1]
        return result

    def integrate(self):  # całkowanie
        result = Poly(0)
        result.size = self.size + 1
        result.a = result.size * [0]
        for i in range(result.size):
            # if i == 3:
            #     import pdb;
            #     pdb.set_trace()
            if i == 0:
                result.a[i] = 0
            else:
                result.a[i] += self.a[i - 1] / i
        # del result.a[-1]
        return result

    def is_zero(self):  # bool, True dla [0], [0, 0],...
        # import pdb; pdb.set_trace()
        return False if any(self.a) else True
        # if any(self.a):
        #     return False
        # else:
        #     return True


# Kod testujący moduł.

import unittest


class TestPoly(unittest.TestCase):
    def setUp(self):
        a = Poly(2, 3)

    def test_cmp(self):
        self.assertTrue(Poly(2, 3) == Poly(2, 3))
        self.assertTrue(Poly(3, 4) != Poly(7, 8))

    def test_add(self):
        self.assertEqual(Poly(2, 3) + Poly(3, 3), Poly(5, 3))

    def test_sub(self):
        self.assertEqual(Poly(3, 3) - Poly(2, 3), Poly(1, 3))

    def test_mul(self):
        self.assertEqual(Poly(2, 3) * Poly(3, 4), Poly(6, 7))

    def test_znak(self):  # pass #w nazwie testu musi być "test"
        self.assertEqual(Poly(2, 3).__pos__(),
                         Poly(2, 3))  # zapewne w tescie powinno być +Poly(2,3), ale o co chodzi to nie wiem...
        self.assertEqual(Poly(2, 3).__neg__(), Poly(-2, 3))  # ctrl+alt+L poprawia pop8

    def test_combine(self):
        self.assertEqual(Poly(2, 2).combine(Poly(3, 4)), Poly(18, 8))

    def test_pow(self):
        self.assertEqual(pow(Poly(3, 2), 2), Poly(9, 4))

    def test_diff_and_integrate(self):
        # import pdb; pdb.set_trace()
        self.assertEqual(Poly(2, 3).diff(), Poly(6, 2), 'test deff failed')
        self.assertEqual(Poly(3, 2).integrate(), Poly(1, 3))

    def test_zero(self):
        self.assertTrue(Poly(0).is_zero())
        self.assertFalse(Poly(3, 4).is_zero())

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
