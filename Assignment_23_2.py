"""
Create a generator to produce first n odd natural numbers 
"""

def oddGenerator(n):
    x = 1
    while n:
        yield x
        x += 2
        n -= 1

for i in oddGenerator(int(input("Enter a natural number: "))):
    print(i, end=" ")
