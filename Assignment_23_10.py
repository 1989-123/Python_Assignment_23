"""
Define a function which calculates HCF of two numbers. 
Define and apply a decorator to check whether two given 
numbers are co-prime or not. 
"""


def HCF_co_prime(hcf_fun):
    def show(x, y):
        z = min(x, y)
        while z >= 1:
            if x % z == 0 and y % z == 0:
                if z == 1:
                    print("Co-prime numbers")
                    break
                else:
                    print("Not a co-prime")
                    break
            z -= 1
    return show

@HCF_co_prime
def HCF(a, b):
    h = min(a, b)
    while h >= 1:
        if a % h == 0  and  b % h == 0:
            print("HCF is:",h)
            break
        h -= 1

HCF(4, 8)
