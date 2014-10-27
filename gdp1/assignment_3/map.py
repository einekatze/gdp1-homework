import csv
from os import path

from gdp1.common.input_helpers import str_input


def import_capitals_from_csv(path):
    """Imports a dictionary that maps country names to capital names.

    @param string path: The path of the CSV file to import this data from.
    @return dict: A dictionary of the format {"Germany": "Berlin", "Finland": "Helsinki", ...}
    """
    capitals = {}

    with open(path) as capitals_file:
        reader = csv.reader(capitals_file)
        for row in reader:
            country, capital = row[0], row[1]
            capitals[country] = capital

    return capitals


def find_capital(capitals, country):
    """Tries to get the capital name for the given country. The search is case insensitive.

    @param dict capitals: A dictionary mapping country names to capital names.
    @param string country: The country name to look for (case insensitive).
    @return: The capital name if found, None otherwise.
    """
    lowercase_country = country.lower()
    for item in capitals.items():
        if item[0].lower() == lowercase_country:
            return item[1]

    return None


def main():
    basepath = path.dirname(path.realpath(__file__))
    filepath = path.join(basepath, "capitals.csv")
    capitals = import_capitals_from_csv(filepath)

    print("Hauptstadt-Finder")
    print("Diese Anwendung findet die Hauptstädte der Länder, die Sie eingeben.")
    print("Durch Eingabe von \"Ende\" wird die Anwendung beendet.")
    print()

    while True:
        entered = input("Bitte geben Sie ein Land ein: ").strip()

        if entered == "":
            continue

        if entered.lower() == "ende":
            break

        capital = find_capital(capitals, entered)
        if capital:
            print("Die Hauptstadt von %s ist %s." % (entered, capital))
        else:
            print("Keine Hauptstadt konnte für Ihre Eingabe gefunden werden.")


if __name__ == "__main__":
    main()