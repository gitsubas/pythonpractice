from math import factorial


def findfactorial(n):
    if n == 0:
        print("The factorial of zero is 1")
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        print(factorial)
findfactorial(6)
