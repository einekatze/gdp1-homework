def collatz(n, acc=None):
    if n <= 0:
        raise ValueError("Collatz must be called with n > 0.")

    if acc:
        acc.append(n)
    else:
        acc = [n]

    if acc[-3:] == [4, 2, 1]:
        return acc

    if n % 2 == 0:
        new_n = n // 2
    else:
        new_n = 3 * n + 1

    return collatz(new_n, acc)


def main():
    print(collatz(1))


if __name__ == "__main__":
    main()