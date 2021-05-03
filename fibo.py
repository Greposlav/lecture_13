def recursive_nth_fibo(n):
    if n < 0:
        raise ValueError("Nezadal jsi kladne cislo.")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    m = input("Zadejte cislo:")
    print(f"{m}-tý prvek Fibonacciho posloupnosti je: {recursive_nth_fibo(int(m))}")


if __name__ == '__main__':
    main()
