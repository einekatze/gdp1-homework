def main():
    celsius_with_fahrenheit = lambda c: (c, 9 / 5 * c + 32)
    fahrenheit_with_celsius = lambda f: (f, 5 / 9 * (f - 32))

    # With map:
    cf = list(map(celsius_with_fahrenheit, range(-10, 51, 2)))
    fc = list(map(fahrenheit_with_celsius, range(0, 101, 5)))

    # With list comprehensions:
    # cf = [celsius_with_fahrenheit(c) for c in range(-10, 51, 2)]
    # fc = [fahrenheit_with_celsius(f) for f in range(0, 101, 5)]

    print("Celsius to Fahrenheit conversions for -10°C to 50°C:")
    for conversion in cf:
        print("%5.1f°C = %6.1f°F" % conversion)

    print()
    print("Fahrenheit to Celsius conversions for 0°F to 100°F:")
    for conversion in fc:
        print("%5.1f°F = %6.1f°C" % conversion)


if __name__ == "__main__":
    main()