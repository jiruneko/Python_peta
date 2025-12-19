X = 99

# def func():
#     X = 88
# print(X)

# a = "Helloaaaaaaa"

# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")

# def func(Y):
#     z = x + Y
#     return z

# print(func(1))

# X = 88

# def func():
#     global X
#     X = 99

# func()
# print(X)

# y, z = 1, 2
# def all_global():
#     global x
#     x = y + z

# print(x)

# import first
# print(first.X)
# first.X = 88

def f1():
    X = 88
    def f2():
        print(X + 1)
    f2()

f1()

def f1():
    X = 88
    def f2():
        print(X + 1)
    return f2

action = f1()
action()