print('Zadanie 3.1')
print('Odpowiedz opisowa zakomentowana')
#Zad 1: Jest poprawnie, ale instrukcje nie powinny się konczyc srednikiem (nie jest to błąd ale jest to wbrew konwencji)

#Zad 2: for i in "qwerty":if ord(i) < 100: print(i) (<-używam Python 3) -to byloby dobrze tylko trzeba rozrzucić po linijkach w zrobic ciecia bo python nie bedzie wiedzial ze jest petla?

#Zad 3: Poprawne gdy: for i in "axby": print(ord(i) if ord(i) < 100 else i)

print('Zadanie 3.2')
print('Odpowiedz opisowa zakomentowana')
#Zad: L=[3,5,4]-powinno byc L.sort() samo, jesli chcemy zmienićkolejnosc w istniejacej iscie lub L2=sorted(L) jesli chcemy miec nowa lise posortowana

#Zad: x,y -dwom zmiennym przypisujemy trzy wartosci- sprzecznosc

#Zad: X=1,2,3 -mozemy tworzyc nowa zmodyfikowana tuple, ale nie mozemy podmieniac elementow w strej, ponadto nie miała ona elementu X[3] ktory moznaby podmienic

#Zad: X=[1,2,3] -dla listy można podmieniać elementy ale ta lista nie ma elementu X[3] ")

#Zad: X='abc' -na stringu nie mozna wykonac metody append, jest ona mozliwa dla listy, np. jezeli byloby X=['abc']
        #Nei umiem użyćfunkcji map()
#Zad map(abs, L) -funkcja pow() musi miec dwa argumenty (lub 3), jesli chcemy uzyc range() musimy wrcucic calos w petle

print('Zadanie 3.3')
n=30
while n>0:
        if (n % 3) == 0:
                n -= 1
        else:
                print(n)
                n -= 1

print('Zadanie 3.4', '\n', 'nieniejszy program oblicza trzecią potęgę liczby rzeczywistej, jeżeli chcesz przerwać pracę programu wpisz stop')
n = 0
while True:
        n = input("Podaj liczbe: ")
        if n == "stop":
            break
        try:                
                n=float(n)
        except ValueError:                        
                print("To nie jest liczba typu float!")
                continue
        else:
                x = n**3
                print("para x i trzecia potęga x: ",n ,", ", x)
 

print('Zadanie 3.5')
n = input('Podaj dlugosc miarki (liczba całkowita): ')
i=0
X = ' |'
Y = '0   '
if not n.isdigit():
        print("To nie jest liczba!")
else:
        n1=int(n)
        while i < n1:
                X = X + '...|'
                i1=str(i+1)
                Y = Y +i1 + '   '
                i += 1
        print(X, '\n', Y)
        
print('Zadanie 3.6') 
n1 = int(input('Podaj liczbe kwadratow w wierszu: '))
n2 = int(input('Podaj liczbe kwadratow w kolumnie: '))

i=0
j=0

if n1==0 or n2==0:
        print('Nie mam co wydrukować jeśli jest 0 wierszy lub kolumn')
else:
        X = '+'
        Y = '|'
        Z = ''
        while j < n2:       
                while i < n1:
                        X = X+'---+'
                        Y = Y+'   |'
                        i += 1
                #string Z będzie moim wierszem
                Z = Z + X +'\n'+ Y + '\n'
                j += 1
        print(Z+X)                

#Zadanie 3.7. Po co jest: def __init__(self, seconds=0):self.s = seconds?

print('Zadanie 3.8.')
#Wybrałam listy bo je łatwo modyfikować. Czy jakbym miała użyc tupli które nie są
#modyfikowalne musiałabym ściągać je do listy modyfikować a potem ewentulanie zmienić na liste?
#jest ta opcja z tworzeniem nowej tupli T='a'+T[1:] ale nie umiałam użyć
K1=[1,2,4,'e','g',6,8,'g','w','z','c','v','b','b','a','e',2,2,8]
K2=['p','k','l','a',3,4,6,7,8,'d','s','s','e','a',2]
common = [x for x in K1 if x in K2]
print('Podpunkt a', '\n',common)
all = set(list(K1) + list(K2))
print('Podpunkt b', '\n', all)
#Ka=[]   inny sosób
#Kb=[]
#for i in K1:
#        if i in K2:
#                if i not in Ka:
#                        Ka=Ka+[i]
#print('Podpunkt a', '\n', Ka)

#for i in K1:
#        if i not in Kb:
#                Kb=Kb+[i]
#for i in K2:
#        if i not in Kb:
#                Kb=Kb+[i]
#print('Podpunkt b', '\n', Kb)

print('Zadanie 3.9.')
L=[[2,3],[3,4],(3,4,5,6),[4,3,2,6,8,9],(1,2),[1,9]]
result_c = [sum(x) for x in L]
print(result_c)
#L1=[] inny sposób
#i=0
#while i<len(L):
#        L1=L1+[sum(L[i])]
#       i+=1
#print(L1)

print('Zadanie 3.10')
Roman_dict2 = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}#druga definicja słownika

Roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def roman2int(roman):
    final = 0
    skip = False
    arabic = [Roman_dict[x] for x in roman]
    for index, num in enumerate(arabic):
        if skip:
            skip = False
            continue
        try:                
            next_num = arabic[index+1]
            if not next_num > num:            
                final = final + num
            else:
                dif = next_num - num
                final += dif
                skip = True
        except IndexError:
            final += num
    return final


print(roman2int('XII'), roman2int('IX'), roman2int('MCXL'))

