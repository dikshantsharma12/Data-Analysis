from collections import defaultdict
import matplotlib.pyplot as plt
from data_reader import maharastra_df

maharashtra_data = maharastra_df()


def registration_count_over_year():
    """"Plot a Grouped Bar Plot by aggregating registration counts over ...

    Year of registration
    Principal Business Activity
    Plot only top 5 Prinicipal Business Activity for last 10 years"""

    aggregation = defaultdict(lambda: defaultdict(int))

    for data in maharashtra_data:
        if data["DATE_OF_REGISTRATION"] != "NA":
            year = int(data["DATE_OF_REGISTRATION"][-2:])

            if year >= 13 and year <= 22:
                year = "20"+str(year)
                aggregation[year][data["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]] += 1

    return aggregation


def transform_data_to_plot(registration_data):
    """Tranfromation of data required for grouped bar plot"""

    registration_data = dict(sorted(registration_data.items()))

    for key, value in registration_data.items():

        registration_data[key] = dict(
            sorted(registration_data[key].items(), key=lambda item: item[1], reverse=1))

    temp = dict()
    data = []
    data1 = []
    h_label = []
    for key, value in registration_data.items():
        d1 = list(value.keys())[:5]
        d2 = list(value.values())[:5]
        data.append(d2)
        data1.append(d2.copy())
        h_label.append(d1)
        temp[key] = [d1, d2]

    years = list(temp.keys())
    data_by_year = []
    for i in range(5):
        tem = []
        for j in range(10):
            tem.append(data[j].pop(0))
        data_by_year.append(tem)

    return data_by_year, years, data1, h_label


def add_label(data, h_label):
    """Adding bar labels"""
    w = 0.16
    x_pos = []
    x_pos.append([x for x in range(-5, 5)])
    for i in range(4):
        temp = []
        for j in x_pos[i]:
            temp.append(j+w)
        x_pos.append(temp)
    label_pos = []
    for i in range(10):
        temp = []
        for j in range(5):
            temp.append(x_pos[j].pop(0))
        label_pos.append(temp)
    print(len(data[1]))
    for i in range(10):
        for j in range(5):
            data_to_fill = h_label[i][j]+" - {}".format(data[i][j])
            plt.text(label_pos[i][j], data[i][j]*1.01, data_to_fill,
                     ha='center', rotation=90, fontsize=5, fontweight="bold")


def plot(data_to_year, year, data, h_label):
    """Grouped bar plot"""

    w = 0.16
    x_pos = []
    x_pos.append([x for x in range(-5, 5)])
    for i in range(4):
        temp = []
        for j in x_pos[i]:
            temp.append(j+w)
        x_pos.append(temp)

    for i in range(5):

        plt.bar(x_pos[i], data_to_year[i], w)
    add_label(data, h_label)
    plt.xticks(x_pos[2], year)
    plt.tight_layout()
    plt.show()


def main():
    """Plot a Grouped Bar Plot by aggregating registration counts over ...

        Year of registration
        Principal Business Activity
        Plot only top 5 Prinicipal Business Activity for last 10 years"""

    registration_data = registration_count_over_year()

    data_by_year, year, data, h_label = transform_data_to_plot(
        registration_data)

    plot(data_by_year, year, data, h_label)


if __name__ == "__main__":
    main()
