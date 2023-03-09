import sys


def foo1():
    try:
        return 1
    finally:
        return 2


def foo2():
    try:
        return None
    finally:
        return "Hello Python"


k = foo1()
print(k)

s = foo2()
print(s)

sys.exit()
