from gdp1.common.input_helpers import int_input, float_input


def request_floats(count):
    """Requests the given amount of floats from the user.

    @param int count: The amount of floats to request.
    @return list: A list of floats that the user entered.
    """
    numbers = []
    digits = "%" + str(len(str(count))) + "d"
    prompt = "Enter number " + digits + " of %d: "

    for i in range(count):
        number = float_input(prompt % (i + 1, count))
        numbers.append(number)

    return numbers


def maximum(enum):
    """Returns the greatest value in the given list.

    @return: The greatest value.
    """
    greatest = None
    for elem in enum:
        if greatest is None or elem > greatest:
            greatest = elem

    return greatest


def main():
    n = int_input("Enter the amount of numbers you wish to enter (n >= 2): ", min=2)
    floats = request_floats(n)
    greatest = maximum(floats)
    print("The greatest value is: ", greatest)

if __name__ == "__main__":
    main()