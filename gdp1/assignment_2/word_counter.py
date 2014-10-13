from gdp1.common.input_helpers import str_input


def main():
    word_1 = str_input("Enter a word: ",)
    word_2 = str_input("Enter another word: ")

    if len(word_1) + len(word_2) > 29:
        print("The summed length of both words must not exceed 29 characters. Exiting.")
        exit(1)

    i = 30 - len(word_1) - len(word_2)

    print(word_1, end="")

    while i != 0:
        i -= 1
        print(".", end="")

    print(word_2)


if __name__ == "__main__":
    main()
