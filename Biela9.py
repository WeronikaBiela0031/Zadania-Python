print('Zadanie 9.1')


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):  # klasy O(N)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        #     import pdb; pdb.set_trace()
        if self.length == 0:
            raise ValueError('pusta lista')
        elif self.length == 1:
            removed = self.head
            self.tail = self.head = None
        elif self.length == 2:
            removed = self.tail
            self.tail = self.head
            self.tail.next = None
        else:
            second_to_last_tail = self.head
            removed = self.tail
            for i in range(self.length - 2):
                second_to_last_tail = second_to_last_tail.next
            self.tail = second_to_last_tail
            self.tail.next = None
        self.length -= 1
        return removed

    def merge(self, other):  # klasy O(1)
        if other.length != 0:
            # dajemy na koniec listy
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        return 'SingleLists merged'

    def clear(self):  # czyszczenie listy
        while not self.is_empty():
            print(self.tail)
            self.remove_tail()
        return "List cleard"


# Zastosowanie.
alist = SingleList()
alist.insert_head(Node(11))  # [11]
alist.insert_head(Node(22))  # [22, 11]
alist.insert_tail(Node(33))  # [22, 11, 33]

blist = SingleList()
blist.insert_head(Node(44))  # [44]
blist.insert_tail(Node(55))  # [44, 55]
blist.insert_tail(Node(66))  # [44, 55, 66]

print("length {}".format(alist.length))  # odczyt atrybutu
print("length {}".format(alist.count()))  # wykorzystujemy interfejs
# while not alist.is_empty():   # kolejność 22, 11, 33
#     print ( "remove head {}".format(alist.remove_head()) )

# while not alist.is_empty():   # kolejność 22, 11, 33
#     print ( "remove tail {}".format(alist.remove_tail()) )

# while not blist.is_empty():  # kolejność 44, 55
print("{}".format(alist.merge(blist)))
print("{}".format(alist.tail))

print("{}".format(alist.clear()))

print('Zadanie 9.6')


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def traverse_stack(top, visit):
        if top is None:
            return
        stack = list()  # stos symulujemy przez listę Pythona
        stack.append(top)
        while stack:
            node = stack.pop()
            visit(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def count_leafs(top):
        if top is None:
            return
        number_of_leafs = 0
        stack = list()  # stos symulujemy przez listę Pythona
        stack.append(top)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            else:
                number_of_leafs += 1
        return number_of_leafs

    def count_total(top):
        if top is None:
            return
        sum_of_leafs = 0
        stack = list()  # stos symulujemy przez listę Pythona
        stack.append(top)
        sum_of_leafs += top.data
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                sum_of_leafs += node.right.data
            if node.left:
                stack.append(node.left)
                sum_of_leafs += node.left.data
        return sum_of_leafs


root = None  # puste drzewo
root = Node("start")  # drzewo z jednym węzłem
# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.traverse_stack(print))
print(root.count_leafs())
print(root.count_total())
