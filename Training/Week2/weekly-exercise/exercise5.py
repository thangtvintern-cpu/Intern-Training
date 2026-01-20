# Exercise 5: Tuples


def swap(a, b):
    return b, a


def zip_coords(x, y):
    return list(zip(x, y))


def unzip_coords(coords):
    x, y = zip(*coords)
    return list(x), list(y)


def l1_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def l2_distance(x, y):
    import math
    return math.sqrt(sum((a-b)**2 for a, b in zip(x, y)))