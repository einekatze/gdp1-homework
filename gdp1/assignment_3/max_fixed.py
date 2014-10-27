from gdp1.common.input_helpers import int_input


def my_max(values):
    """Returns the "largest" value in the given list. If the values are not of the same type, the result may be
    undefined.

    @param list values: A list of values.
    @raises ValueError: When an empty array is passed.
    @return: The "largest" value.
    """
    if len(values) == 0:
        raise ValueError("my_max() argument is an empty sequence.")

    largest = None
    for elem in values:
        if not largest or elem > largest:
            largest = elem

    return largest


def main():
    first = int_input(" Enter the first integer value: ")
    second = int_input("Enter the second integer value: ")
    third = int_input(" Enter the third integer value: ")

    largest = my_max([first, second, third])

    print("The largest number of the three numbers you entered is %d." % largest)

if __name__ == "__main__":
    main()