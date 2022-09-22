# Create a generator to produce first n even natural numbers

def evenProducer(n):
    x = 2
    while n:
        yield x
        x += 2
        n -= 1

for i in evenProducer(int(input("Enter a natural number: "))):
    print(i, end=" ")
