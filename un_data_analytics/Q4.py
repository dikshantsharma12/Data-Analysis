from collections import defaultdict
import matplotlib.pyplot as plt
from data_reader import population_data


def population_by_year(data, asean_countries):
    """ Computing Population per year for saarc countries over year 2004 to 2014"""

    population_per_year = defaultdict(lambda: defaultdict(int))

    for entry in data:
        year = int(entry["Year"])
        if year >= 2004 and year <= 2014:

            country = entry["Region"]
            if country in asean_countries:

                population = float(entry["Population"])/10000
                population = float("{:.2f}".format(population))
                population_per_year[year][country] = population

    return population_per_year

def transfrom_data_to_plot(population_per_year):
    """Transfromation of data for plotting"""
    year=[]
    temp=defaultdict(list)
    for key,value in population_per_year.items():
        year.append(key)
        for con,pop in value.items():
            temp[con].append(pop)

    country=list(temp.keys())
    population=list(temp.values())

    return country,year,population

def plot(year,country,population):
    """Plot Population of ASEAN countries by year using bar plot"""

    w=0.08
    bars=[]
    bars.append([x for x in range(-5,6)])
    for i in range(len(country)-1):
        temp=[]
        for j in bars[i]:
            temp.append(j+w)
        bars.append(temp) 
    
    for i in range(10):
        
        plt.bar(bars[i],population[i],w,label=country[i])

    plt.xticks(bars[5],year)
    plt.legend()
    plt.show()
def main():
    """Plot population of ASEAN countries as groups over the years 2004 - 2014."""

    data = population_data()
    asean_countries = ["Indonesia", "Malaysia", "Philippines", "Singapore",
                       "Thailand", "Vietnam", "Laos", "Cambodia", "Brunei", "Myanmar"]
    population_per_year = population_by_year(data, asean_countries)
    country,year,population=transfrom_data_to_plot(population_per_year)

    plot(year,country,population)

if __name__ == "__main__":
    main()
