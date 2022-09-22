"""
Create an endless iterator using generator method to 
produce Prime numbers 
"""


def primeGenerator():
    x = 2
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1

it = primeGenerator()
l1 = []

while True:
    x = input("Do you want to generator another prime number[y / n]: ")
    if x == 'y':
        n = next(it)
        l1.append(n)
        print(n)
    else:
        print()
        print(l1)
        break
