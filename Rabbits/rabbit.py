__author__ = 'Uporabnik'

n = 33
k = 5

def fib(p):
    if p == 1:
        return 1
    elif p == 0:
        return 0
    return (fib(p-1) + k*fib(p-2))

print fib(n)