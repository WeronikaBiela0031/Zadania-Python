print('Zadanie 2.10.')
napis='Przykladowy tekst do liczenia wyrazow z wyrazem GvR'
L=napis.split()
print(len(L))
# /testfisfbiwbi
print('Zadanie 2.11.')
L1='slowo'
print('_'.join(L1))

print('Zadanie 2.12.')
L2=''
L3=''
for i in L:
    L2=L2+i[0]
    L3=L3+i[-1]
print(L2)
print(L3)

print('Zadanie 2.13.')
x=0
for i in L:
    x=x+len(i)
print(x)

print('Zadanie 2.14.')
L.sort(key=len)
print(L[-1])
L4=L[-1]
print(len(L4))

print('Zadanie 2.15.')
#ponieważ nazwę listy "L" już wykozystalam teraz uzyje innej
W=range(3,76,7)
w=''
for i in W:
    w=w+str(i)
print(w)

print('Zadanie 2.16.')
napis2=napis.replace('GvR', 'Guido van Rossum')
print(napis2)

print('Zadanie 2.17.')
L.sort(key=len) #sortuje wg. dlugosci wyrazow
print(L)
L.sort(key=str.lower) #sortuje alfabetycznie
print(L)

print('Zadanie 2.18.')
x=6**18
y=str(x)
print(y.count('0'))

print('Zadanie 2.19.')
K=[7,78,98,333,1,8]
k=str()
for i in K:
    k=k+str(i).zfill(3)+', '
print(k)
