# Exercise 3:


def hello_world():
    print("Hello, world!")


def hello_name(name):
    print("Hello, " + name + "!")


def polynomial(x):
    return 3*x**2 - x + 2


def my_max_if_else(x, y):
    if x > y:
        return x
    else:
        return y


def my_max_if(x, y):
    if x > y:
        return x
    return y


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(n):
    return [i for i in range(2, n+1) if is_prime(i)]


def first_n_primes(n):
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


def root(f, a, b):
    if f(a) * f(b) > 0:
        print("function evals have same sign")
        return None
    for _ in range(100):
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2

