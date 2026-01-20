# Exercise 4: Lists


def print_list(lst):
    for x in lst:
        print(x)


def print_list_reverse(lst):
    for x in lst[::-1]:
        print(x)


def my_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def set_first_elem_to_zero(l):
    l[0] = 0
    return l


def myfilter(func, iterable):
    return [x for x in iterable if func(x)]


def flatten(lst):
    return [item for sub in lst for item in sub]


def longest_word(text):
    import string
    words = [w.strip(string.punctuation) for w in text.split()]
    return max(words, key=len)


def collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        seq.append(n)
    return seq


def longest_collatz(limit):
    return max(range(1, limit), key=lambda x: len(collatz(x)))


def pivot(x, ys):
    return [y for y in ys if y < x] + [x] + [y for y in ys if y >= x]


primes_lambda = lambda n: [x for x in range(2, n+1)
                           if all(x % i for i in range(2, int(x**0.5)+1))]