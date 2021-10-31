#Mateusz Szybiak lab3 20.10.2021
#Zadanie 1

def hello(name: str, surname: str) -> str:

    str = "Cześć " + name + " " + surname + "!"
    return(str)

result = hello("Mateusz", "Szybiak")
print(result)

#Zadanie 2

def multiply(a: int,b: int) -> int:
    return(a*b)

print("wynik mnożenia {} i {} to: {}".format(2,4,multiply(2,4)))


#Zadanie 3

def check_even(a: int) -> bool:
    if a % 2 ==0:
        res = True
    else:
        res = False
    return(res)

num = 2
if check_even(num):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


#Zadanie 4

def check(a: int,b: int,c: int) -> bool:
    if a+b >= c:
        res = True
    else:
        res = False
    return(res)

if check(8,3,6):
    print("Suma jest większa bądź równa")
else:
    print("Suma jest mniejsza")



#Zadanie 5

def check_if_in(list: list, a: int) -> bool:
    if a in list:
        res = True
    else:
        res = False
    return(res)

list = [1,2,4,5,7]
num = 8
if check_if_in(list, num):
    print("{} należy do listy".format(num))
else:
    print("{} nie należy do listy".format(num))


#Zadanie 6

def concatenate(list1: list, list2: list) -> list:
    res = []
    for i in list1:
        res.append(i)
    for i in list2:
        res.append(i)
    res = list(dict.fromkeys(res))
    for i in range(len(res)):
        res[i] = res[i]**3
    return(res)

list1 = [1,2,4,6,7]
list2 = [2,5,7,8,9]
print(concatenate(list1,list2))
