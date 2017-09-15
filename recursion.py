# http://www.cs.cmu.edu/~tcortina/activate/ct/lab8ques.pdf


def sum_(x):
    if x is None:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return x[0] + sum_(x[1:])


def fibonacci(n):
    """O(2^n)"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print("Sum: ", sum_([4 ,5, 6]))
    print("Fibonacci: ", fibonacci(5))
    print("Factorial: ", factorial(5))