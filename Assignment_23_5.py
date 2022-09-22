# Create a generator to produce first n terms of Fibonacci series


def fib(n):
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1

for i in fib(int(input("Enter a number: "))):
    print(i, end=" ")
