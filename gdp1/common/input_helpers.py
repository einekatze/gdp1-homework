def int_input(prompt="", minmax=None, min=None, max=None):
    """Uses `input(prompt)` to request an int value from the user, retrying if the user does not enter a valid value.

    @param str prompt: The prompt to display.
    @param tuple minmax: A tuple of the form (min, max) specifying the inclusive range the number must lie in.
                         Optional.
    @return int: The entered value.
    """
    while True:
        try:
            string = input(prompt)
            if not len(string.strip()):
                continue

            num = int(string)
            if minmax and (num < minmax[0] or num > minmax[1]):
                print("Invalid input. The value must be a number from %i to %i." % minmax)
                continue
            elif min is not None and max is not None and (num < min or num > max):
                print("Invalid input. The value must be a number from %i to %i." % (min, max))
                continue
            elif min is not None and num < min:
                print("Invalid input. The value must be a number greater or equal to %i." % min)
                continue
            elif max is not None and num > max:
                print("Invalid input. The value must be a number less or equal to %i." % max)
                continue

            return num
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def float_input(prompt=""):
    """Uses `input(prompt)` to request a float value from the user, retrying if the user does not enter a valid value.

     @param str prompt: The prompt to display.
     @return float: The entered value.
    """
    while True:
        try:
            string = input(prompt)
            if not len(string.strip()):
                continue
            return float(string)
        except ValueError:
            print("Invalid input. Please enter a float value.")


def str_input(prompt="", max_length=0):
    """Uses `input(prompt)` to request a str value from the user, retrying if the user doesn't enter anything or
    only enters whitespace.

     @param str prompt: The prompt to display.
     @param int max_length: The maximum length of the string. Defaults to no length limit.
     @return str: The entered value.
    """

    while True:
        string = input(prompt)
        if not len(string.strip()):
            continue
        if max_length != 0 and len(string) > max_length:
            print("Your text is too long. It must not exceed a length of %i characters." % max_length)
        return string
