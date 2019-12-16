print('Zadanie 10.2')
# Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków
# w przypadku pojawienia się błędu. Metoda pop() ma zgłaszać błąd w przypadku
# pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia
# stosu. Napisać kod testujący stos.
class Stack:
    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        try:
            if self.n == 0:
                raise ValueError('Stos jest pusty')
        except ValueError as e:
            print(e)
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None  # usuwam referencję
            return data


stack = Stack()
for i in range(10):
    stack.push(i)

print(stack.items, stack.n, stack.size)
print(stack.is_full())
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        for i in range(5):
            self.stack.push(i)

        self.empty = Stack()
        self.full = Stack()
        for j in range(10):
            self.full.push(j)

    def test_init(self):
        self.assertEqual(self.stack.items, [0, 1, 2, 3, 4, None, None, None, None, None])
        self.assertEqual(self.stack.n, 5)
        self.assertEqual(self.stack.size, 10)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)  # sprawdzam czy pierwszy in to ostatni out
        self.assertRaises(ValueError, self.empty.pop())

    def test_is_full_or_is_empty(self):
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.stack.is_empty())
        self.assertTrue(self.full.is_full())
        self.assertTrue(self.empty.is_empty())

    def tearDown(self):  # czyścimy self'a
        del self.stack  # utworzenie tablicy
        del self.full
        del self.empty


print('Zadanie 10.4')
# Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. Poprawić metodę put()
# w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek.
# Napisać kod testujący kolejkę.
class Queue:
    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError('Kolejka jest przepełniona')
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError('Kolejka jest pusta')
        data = self.items[self.head]
        self.items[self.head] = None  # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


queue = Queue()
for i in range(4):
    queue.put(i)

print(queue.items)
print(queue.get())


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        for i in range(4):
            self.queue.put(i)
        self.empty = Queue()
        self.full = Queue()
        for j in range(5):
            self.full.put(j)

    def test_init(self):
        self.assertEqual(self.queue.items, [0, 1, 2, 3, None, None])

    def test_get(self):
        self.assertEqual(self.queue.get(), 0)
        self.assertEqual(self.queue.get(), 1)
        self.assertRaises(ValueError, self.empty.get)

    def test_put(self):
        self.assertRaises(ValueError, self.full.put, 2)

    def tearDown(self):
        del self.queue
        del self.full
        del self.empty


print('Zadanie 10.8')
# wsadzanie i wyciągnie elementów ma być w stałym czasie, przypadkowość= że każdy z elementów ma takie samo
# prwadopodobieństwo wyjscia
import random


class RandomQueue:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0  # pierwszy wolny indeks
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        # brak zabezpieczenia
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencję
        return data

    def remove(self):
        # Uwaga- losując mieszam elementy ale celem jest wyciąganie z kolejki losowych elementów w stałym czasie.
        # Etap 1 - wyszukiwanie elementu.
        j = random.randint(0, self.n - 1)
        # wyciągnąć chce element losowy o j-tym indeksie self.items[j]
        # Etap 2 - usuwanie elementu.
        data = self.items[j]
        if self.is_full():
            x = self.items[-1]
            self.items[-1] = self.items[j]
            self.items[j] = x
            self.pop()
        else:
            x = self.items[self.n]
            self.items[self.n] = None
            self.items[j] = x
        #musimy znależć sposób żeby wybrany element wsadzić na koniec i wtedy uciąć ostatni element (nie można przeidneksowywać!
        self.n -= 1
        return data

    def clear(self):  # czyszczenie listy
        self.items = 10 * [None]
        self.n = 0  # pierwszy wolny indeks
        self.size = 10



randomquenue2 = RandomQueue()
for i in range(10):
    randomquenue2.insert(i)

print(randomquenue2.items)
import time
start = time.perf_counter()
for i in range(7):
    randomquenue2.remove()
end_short = time.perf_counter() - start
print("czas trwania dla listy 10 elementowej: {}".format(end_short))

randomquenue3 = RandomQueue(1000)
for i in range(1000):
    randomquenue3.insert(i)

print(randomquenue3.items)

start = time.perf_counter()
for i in range(7):
    randomquenue3.remove()
end_long = time.perf_counter() - start
print("czas trwania dla listy 1000 elementowej: {}".format(end_long))

print("stosunek czasów: {}".format(end_long / end_short)) #zależność będzie niezależna od długości listy


class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.randomquenue = RandomQueue()
        for i in range(9):
            self.randomquenue.insert(i)

    def test_init(self):
        self.assertEqual(self.randomquenue.items, [0, 1, 2, 3, 4, 5, 6, 7, 8, None])

    def test_is_full_or_is_empty(self):
        self.assertFalse(self.randomquenue.is_empty())
        self.assertFalse(self.randomquenue.is_full())

    def clear_test(self):
        self.assertTrue(self.randomquenue.clear().is_empty())

    def tearDown(self):
        del self

#
if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
