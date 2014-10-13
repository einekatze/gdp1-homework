from gdp1.common.input_helpers import *


def main():
    print("Application for calculating means of two real values")
    print()

    x = float_input("Please enter the first real value: ")
    y = float_input("Please enter the second real value: ")

    # The harmonic mean is defined as zero iff one or both of the values are zero.
    arithmetic_mean = (x + y) / 2
    harmonic_mean = 2 / (1 / x + 1 / y) if x != 0 and y != 0 else 0.0

    print()
    print("The arithmetic mean is: ", arithmetic_mean)
    print("  The harmonic mean is: ", harmonic_mean)


if __name__ == "__main__":
    main()