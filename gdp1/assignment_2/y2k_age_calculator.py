from gdp1.common.input_helpers import int_input


def main():
    year_of_birth = int_input("Enter your year of birth (yy): ", minmax=(0, 99))
    current_year = int_input("Enter the current year   (yy): ", minmax=(0, 99))

    if year_of_birth > current_year:
        # e.g. 100 - 95 + 14 = 19
        age = 100 - year_of_birth + current_year
    else:
        age = current_year - year_of_birth

    print("You are approximately %i years old." % age)

if __name__ == "__main__":
    main()