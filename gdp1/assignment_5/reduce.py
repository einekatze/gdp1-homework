from functools import reduce
from gdp1.common.input_helpers import float_list_input


def arithmetic_mean(enum):
    if len(enum) == 0:
        return None

    return reduce(lambda acc, val: acc + val, enum) / len(enum)


def main():
    print("Please enter a list of floats. When done, enter \"end\".")
    floats = float_list_input("Enter a float or \"end\": ")

    if len(floats):
        print("The arithmetic mean of your entered numbers is %.2f, rounded to two digits."
              % arithmetic_mean(floats))


if __name__ == "__main__":
    main()