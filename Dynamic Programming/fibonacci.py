import itertools

def fibonnacci_recu(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnacci_recu(n-1) + fibonnacci_recu(n-2)


def fibonnaci_dp(n):
    fib = [0, 1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]


def fibonnaci_ultimate(n):
    back2, back1 = 1, 0
    if n==0:
        return 0

    for i in range(2,n+1):
        next = back1 + back2
        back2 = back1
        back1 = next
    return back1 + back2

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

print(fibonnacci_recu(10))
print(fibonnaci_dp(10))
print(fibonnaci_ultimate(10))
print(list(itertools.islice(fib_gen(), 10)))