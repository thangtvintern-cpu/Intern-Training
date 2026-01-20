# Exercise 1.1 & 1.2
def exercise_1_1_and_1_2():
    print(3 + 1)
    print(3 * 3)
    print(2 ** 3)
    print("Hello, world!")


# Exercise 1.3
def exercise_1_3():
    print('py' + 'thon')
    print('py' * 3 + 'thon')
    try:
        print('py' - 'py')
    except TypeError as e:
        print(e)
    try:
        print('3' + 3)
    except TypeError as e:
        print(e)
    print(3 * '3')
    try:
        print(a)
    except NameError as e:
        print(e)
    a = 3
    print(a)


# Exercise 1.4
def exercise_1_4():
    print(1 == 1)
    print(1 == True)
    print(0 == True)
    print(0 == False)
    print(3 == 1 * 3)
    print((3 == 1) * 3)
    print((3 == 3) * 4 + 3 == 1)
    print(3**5 >= 4**4)


# Exercise 1.5
def exercise_1_5():
    print(5 / 3)
    print(5 % 3)
    print(5.0 / 3)
    print(5 / 3.0)
    print(5.2 % 3)
    print(2001 ** 200)


# Exercise 1.6
def exercise_1_6():
    print(2000.3 ** 200)
    print(1.0 + 1.0 - 1.0)
    print(1.0 + 1.0e20 - 1.0e20)


# Exercise 1.7
def exercise_1_7():
    name = "John Doe"
    print("Hello, " + name + "!")


# Exercise 1.8
def exercise_1_8():
    print(float(123))
    print(float('123'))
    print(float('123.23'))
    print(int(123.23))
    try:
        print(int('123.23'))
    except ValueError as e:
        print(e)
    print(int(float('123.23')))
    print(str(12))
    print(str(12.2))
    print(bool('a'))
    print(bool(0))
    print(bool(0.1))
