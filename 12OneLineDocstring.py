# one line docstring
import math


def quadratic(a, b, c):
    """Use the quadratic formula to solve for x."""
    x_1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x_2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x_1, x_2


def main():
    """Solve the quadratic equation for x."""
    a = float(input("What is the a value?"))
    b = float(input("What is the b value?"))
    c = float(input("What is the c value?"))
    x_1, x_2 = quadratic(a, b, c)
    print("The x values are:", x_1, x_2)


if __name__ == '__main__':
    main()