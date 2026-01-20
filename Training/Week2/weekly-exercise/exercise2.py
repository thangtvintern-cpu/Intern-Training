# Exercise 2:


def exercise_2_2():
    for i in range(101):
        print(i)

    for i in range(101):
        if i % 7 == 0:
            print(i)

    for i in range(1, 101):
        if i % 5 == 0 and i % 3 != 0:
            print(i)

    for x in range(2, 21):
        divisors = []
        for i in range(2, x):
            if x % i == 0:
                divisors.append(i)
        print(x, divisors)


def exercise_2_3():
    i = 0
    while i <= 100:
        print(i)
        i += 1

    i = 0
    while i <= 100:
        if i % 7 == 0:
            print(i)
        i += 1


def exercise_2_5():
    count = 0
    x = 11
    while count < 20:
        if x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
            print(x)
            count += 1
        x += 1


def exercise_2_6():
    x = 1
    while True:
        if all(x % i == 0 for i in range(1, 11)):
            print(x)
            break
        x += 1


def exercise_2_7():
    x = 103
    while x != 1:
        print(x, end=" ")
        x = x // 2 if x % 2 == 0 else 3 * x + 1
    print(1)
