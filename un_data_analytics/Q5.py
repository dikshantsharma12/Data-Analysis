import matplotlib.pyplot as plt
from data_reader import maharastra_df


def authorized_cap(df):
    """Compute Authorized cap  with Interval"""
    dic = {
        "<=1L": 0, "1L to 10L": 0, "10L to 1CR": 0, "1CR to 10CR": 0, ">10CR": 0
    }
    temp = []
    for item in df:
        if float(item["AUTHORIZED_CAP"]) >= 0 and float(item["AUTHORIZED_CAP"]) <= 1e5:
            dic["<=1L"] += 1
        elif float(item["AUTHORIZED_CAP"]) > 1e5 and float(item["AUTHORIZED_CAP"]) <= 1e6:
            dic["1L to 10L"] += 1
        elif float(item["AUTHORIZED_CAP"]) > 1e6 and float(item["AUTHORIZED_CAP"]) <= 1e7:
            dic["10L to 1CR"] += 1
        elif float(item["AUTHORIZED_CAP"]) > 1e7 and float(item["AUTHORIZED_CAP"]) <= 1e8:
            dic["1CR to 10CR"] += 1
        else:
            dic[">10CR"] += 1
        temp.append(float(item["AUTHORIZED_CAP"]))

    return dic


def plot(data_to_plot):
    """plot Histogram"""
    authorized_cap_data = list(data_to_plot.keys())
    authorized_cap_value = list(data_to_plot.values())

    plt.bar(authorized_cap_data, authorized_cap_value, width=1.0, color="pink")
    plt.plot(authorized_cap_data, authorized_cap_value, color="black")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend()
    plt.show()


def main():
    """ Plot a histogram on the "Authorized Capital" (column: AUTHORIZED_CAP)
            with the following intervals
            [ <= 1L ,  1L to 10L , 10L to 1Cr , 1Cr to 10Cr , > 10Cr ]"""

    maharashtra_data = maharastra_df()
    data_to_plot = authorized_cap(maharashtra_data)
    plot(data_to_plot)


if __name__ == "__main__":
    main()
