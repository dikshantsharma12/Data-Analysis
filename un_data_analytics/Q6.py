""""Bar Plot of company registration by year"""
from collections import defaultdict
import matplotlib.pyplot as plt
from data_reader import maharastra_df


def registration_by_year(df):
    """Obtaing Registration count by year"""

    reg_by_year = defaultdict(int)
    for entry in df:
        if entry["DATE_OF_REGISTRATION"] == "NA":
            continue

        if int(entry["DATE_OF_REGISTRATION"][-2:]) > 22:
            reg_by_year[int("19"+entry["DATE_OF_REGISTRATION"][-2:])] += 1
        else:
            reg_by_year[int("20"+entry["DATE_OF_REGISTRATION"][-2:])] += 1

    return reg_by_year


def transform_to_plot(reg_per_year):
    """Transfroming data required for bar plot"""
    reg_per_year_sorted = dict(
        sorted(reg_per_year.items()), key=lambda item: item[0])
    del reg_per_year_sorted["key"]

    year = list(reg_per_year_sorted.keys())
    registration = list(reg_per_year_sorted.values())
    return year, registration


def plot(year, registration):
    """Bar plot of registration by year"""
    plt.bar(year, registration)
    plt.xticks(year, rotation=90, fontsize=6)
    plt.show()


def main():
    """Registration by Year"""
    data = maharastra_df()
    reg_per_year = registration_by_year(data)
    year, registration = transform_to_plot(reg_per_year)
    plot(year, registration)


if __name__ == "__main__":
    main()
