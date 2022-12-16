from data_reader import population_data
from collections import defaultdict
import matplotlib.pyplot as plt


def population_of_asean(data, asean_countries):
    """ Population of ASEAN countries in year 2014"""

    asean_population = defaultdict(int)

    for entry in data:

        year = str(entry["Year"])
        region = entry["Region"].capitalize()
        population = float(entry["Population"])/10000
        population = float('{:.2f}'.format(population))

        if year == "2014" and region in asean_countries:
            asean_population[region] = population

    return asean_population


def plot(data_to_plot):
    """ Bar Chat of the population of ASEAN countries """

    country = list(data_to_plot.keys())
    population = list(data_to_plot.values())

    plt.bar(country, population)
    plt.xticks(rotation=90)
    plt.ylabel("Population in Crore")
    plt.xlabel("Years")
    plt.tight_layout()
    plt.show()


def main():

    data = population_data()
    asean_countries = ["Indonesia", "Malaysia", "Philippines", "Singapore",
                       "Thailand", "Vietnam", "Laos", "Cambodia", "Brunei", "Myanmar"]
    data_to_plot = population_of_asean(data, asean_countries)
    plot(data_to_plot)


if __name__ == "__main__":
    main()
