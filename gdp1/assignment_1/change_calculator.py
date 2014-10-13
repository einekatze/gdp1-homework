from collections import namedtuple

from gdp1.common.input_helpers import int_input


class Change(namedtuple("Change", "dollars quarters dimes nickels cents")):
    """A class representing change in US dollars."""

    # To make instances of Change not require more memory than regular namedtuples.
    __slots__ = ()

    def __str__(self):
        components = list()
        components.append("%i dollar%s" % (self.dollars, "" if self.dollars == 1 else "s"))
        components.append("%i quarter%s" % (self.quarters, "" if self.quarters == 1 else "s"))
        components.append("%i dime%s" % (self.dimes, "" if self.dimes == 1 else "s"))
        components.append("%i nickel%s" % (self.nickels, "" if self.nickels == 1 else "s"))
        components.append("%i cent%s" % (self.cents, "" if self.cents == 1 else "s"))
        return ", ".join(components)

    @staticmethod
    def from_cents(cents):
        """This method splits up a cent value into a tuple of higher denominations: Dollars, quarters, dimes, nickels
        and cents. The method weighs higher denominations higher than lower denominations, meaning that one dollar coins
        will be preferred over quarters, quarters will be preferred over dimes, and so on.

        @param int cents: The amount in cents.
        @return Change: The amount of change expressed in a named tuple of dollars, quarters, dimes, nickels and cents.
        """

        dollars, remainder = divmod(cents, 100)
        quarters, remainder = divmod(remainder, 25)
        dimes, remainder = divmod(remainder, 10)
        nickels, remainder = divmod(remainder, 5)

        return Change(dollars, quarters, dimes, nickels, remainder)


if __name__ == "__main__":
    print("Change for 163 cents:", Change.from_cents(163))

    print()
    print("Enter your own value in cents to calculate change containing higher denominations.")
    print(Change.from_cents(int_input("Your value: ")))
