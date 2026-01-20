# Exercise 6: Dictionary


def print_dict(d):
    for k, v in d.items():
        print(k, v)


def histogram(lst):
    hist = {}
    for x in lst:
        hist[x] = hist.get(x, 0) + 1
    return hist


def reverse_lookup(d, value):
    return [k for k, v in d.items() if v == value]