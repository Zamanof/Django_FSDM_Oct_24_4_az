# LEGB
# Local
# Enclosing
# Global
# Built-n
from math import pi as PI

print(f"Built in: {PI}")

def foo():
    # global PI
    PI = "Salam"
    def bar():
        nonlocal PI
        PI = True
        print(f"Local: {PI}")

    bar()
    print(f"Enclosing: {PI}")

PI = 3.14

print(f"Global: {PI}")

foo()

print(f"Global: {PI}")
