""" 
Create an endless iterator using generator method 
to produce terms of Fibonacci series
"""

def fib():
    a, b = 0, 1
    while True:
       yield a
       a, b = b, a + b

it = fib()
l1 = []

while True:
    x = input("Do you want to genrate another element[y / n]: ")
    if x == 'y':
        n = next(it)
        l1.append(n)
        print(n)
    else:
        print()
        print(l1)
        break
