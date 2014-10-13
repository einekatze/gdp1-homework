from gdp1.common.input_helpers import str_input


def is_palindrome(string):
    """Returns True if the given string is a palindrome, False if it isn't.

    @param str string: The string to check.
    @return boolean: Whether the string is a palindrome.
    """

    # The property of being a palindrome doesn't depend on the case.
    lower_string = string.lower()
    one_half = len(lower_string) // 2

    for i in range(one_half):
        if lower_string[i] != lower_string[-i - 1]:
            return False

    return True


def main():
    word = str_input("Enter a word to find out whether it's a palindrome: ")
    print(is_palindrome(word))

if __name__ == "__main__":
    main()
