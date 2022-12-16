from collections import defaultdict
import matplotlib.pyplot as plt
from data_reader import population_data


def population_over_year(data):
    """ India population over years """

    india_population_over_year = defaultdict(int)

    for entry in data:

        region = entry["Region"].lower()

        if region == "india":
            year = entry["Year"]
            population = float(entry["Population"])/10000
            population = float('{:.2f}'.format(population))
            india_population_over_year[year] = population

    return india_population_over_year


def plot(data_to_plot):
    """ Bar Plot of 'Population of India' vs. 'Years.' """

    year = list(data_to_plot.keys())
    population = list(data_to_plot.values())

    plt.bar(year, population)
    plt.xticks(rotation=90)
    plt.ylabel("Population in Crore")
    plt.xlabel("Years")
    plt.tight_layout()
    plt.show()


def main():
    """Main Function"""
    data = population_data()
    data_to_plot = population_over_year(data)
    plot(data_to_plot)


if __name__ == "__main__":
    main()
