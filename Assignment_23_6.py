# Create a generator to produce first n prime numbers

def prime(n):
    x = 2
    while n:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
             yield x
             n -= 1
        x += 1

for i in prime(5):
    print(i, end=" ")
