#Mateusz Szybiak Informatyka lab2 19.10.2021

from math import *
#Zadanie 2
#a

def names(name):
    for n in name:
        print(n)
    return
names(['ala','kamil','darek','julia','michał'])


#b

def multiply(numbers):
    res = []
    for n in numbers:
        res.append(2*n)
    return(res)

def multiply_list(numbers):
    res = [2*i for i in numbers]
    return (res)

print("Sposób 1")
print("Pierwotna lista: {} \nZwrócona lista: {}".format([1,3,7,22,30], multiply([1,3,7,22,30])))
print("Sposób 2")
print("Pierwotna lista: {} \nZwrócona lista: {}".format([1,3,7,22,30], multiply_list([1,3,7,22,30])))


#c

lista = [1, 2, 5, 10, 13, 14, 18, 21, 24, 30]

for i in range (len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i])


#d

lista = [1, 2, 5, 10, 13, 14, 18, 21, 24, 30]

for i in range(floor(len(lista)/2)):
    print(lista[2*i+1])
