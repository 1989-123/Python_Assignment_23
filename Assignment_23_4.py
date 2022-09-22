# Create a generator to produce squares of first N natural numbers

def squaresProducer(n):
    x = 1
    while n:
        yield x ** 2
        x += 1
        n -= 1

for i in squaresProducer(int(input("Enter a number: "))):
    print(i, end=" ")
