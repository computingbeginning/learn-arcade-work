def f(n):
    if n == 1:
        return 6
    elif n > 1:
        return (1 / 2) * f(n - 1) + 4


def main():
    result = f(10)
    print(result)


main()
