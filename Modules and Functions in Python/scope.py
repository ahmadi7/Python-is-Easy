def fact(n):
    """ calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def recursive_factorial(n):
    # n! can also be defined as n * (n - 1)
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def recursive_fibonacci(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)



def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result



for i in range(1, 36):
    print(i, recursive_fibonacci(i), "\t", fibonacci(i))
