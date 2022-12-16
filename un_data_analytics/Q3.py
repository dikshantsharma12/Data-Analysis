
from data_reader import population_data
from collections import defaultdict
import matplotlib.pyplot as plt


def population_over_year(data, saarc_countries):
    """ SAARC countries population over years """

    saarc_population_over_year = defaultdict(int)

    for entry in data:

        region = entry["Region"].capitalize()

        if region in saarc_countries:
            year = entry["Year"]
            population = float(entry["Population"])/10000
            population = float('{:.2f}'.format(population))
            saarc_population_over_year[year] += population

    return saarc_population_over_year


def plot(data_to_plot):
    """ Bar Plot of SAARC Countries population """

    year = list(data_to_plot.keys())
    population = list(data_to_plot.values())

    plt.bar(year, population)
    plt.xticks(rotation=90)
    plt.ylabel("Population of SAARC Countries in Crore")
    plt.xlabel("Years")
    plt.tight_layout()
    plt.show()


def main():

    data = population_data()
    saarc_countries = ["Afghanistan", "Bangladesh", "Bhutan",
                       "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]
    data_to_plot = population_over_year(data, saarc_countries)
    plot(data_to_plot)


if __name__ == "__main__":
    main()
