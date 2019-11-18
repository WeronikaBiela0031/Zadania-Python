print('Zadanie 6.1')
class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'.""" #nieformalny string
        h = self.s //3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec) #formatowanie stringa; d- oznacza ze to int

    def __repr__(self): #reprezentacja
        """Zwraca string 'Time(s)'.""" #wskoczy liczba sekund
        return "Time({0})".format(self.s)

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int.""" #można też rzutować na inne typy
        return self.s


    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s) #nowa instancja klasy- obiekt w klasie- dlatego Time(..)


    def __eq__(self, other):           # porównywanie, -1|0|+1
        """Porównywanie odcinków czasu. Sprawdzenie znaku równe, x == y """
        #dla Pythona 3 <, <=, != już nie działa == -_eq__ < __lt__
        return (self.s == other.s)

    def __lt__(self, other):
        '''Porównywanie odcinków czasu. Sprawdzenie znaku mniejsze, x < y'''
        return (self.s < other.s)

    def __gt__(self, other):
        '''Porównywanie odcinków czasu. Sprawdzenie znaku większe, x > y'''
        return (self.s > other.s)

    def __le__(self, other):
        '''Porównywanie odcinków czasu. Sprawdzenie znaku mniejsze lub równe, x <= y'''
        return (self.s <= other.s)

    def __ge__(self, other):
        '''Porównywanie odcinków czasu. Sprawdzenie znaku większe lub równe, x >= y'''
        return (self.s >= other.s)

    def __ne__(self, other):
        '''Porównywanie odcinków czasu. Sprawdzenie znaku różne, x != y, dawniej też x <> y'''
        return (self.s != other.s)




# Kod testujący moduł.

import unittest

class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self): # test str() i repr()
        self.assertEqual(str(Time(3601)), "01:00:01")
        self.assertEqual(repr(Time(20)), 'Time(20)')


    def test_cmp(self): #trzeba to zrobić przed dodawaniem
        # Można sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(1) == Time(1)) #eq(Time(1),Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertFalse(Time(3) < Time(2))
        self.assertTrue(Time(3) >= Time(2))
        self.assertTrue(Time(2) >= Time(2))
        self.assertFalse(Time(3) <= Time(2))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        #(Time(1)+Time(2)).s, 3 pierwszy argument jest 3 ale jest nieładny, ".s" określa że jest to atrybut klasy Time


    def test_int(self):
        self.assertEqual(int(Time(3)),3)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
