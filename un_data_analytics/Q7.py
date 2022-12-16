from collections import defaultdict
import matplotlib.pyplot as plt
from data_reader import maharastra_df, pincode


def registration_by_district(year, maharashtra_data, pincode_data):
    """Company registration in the year 2015 by the district."""

    reg_by_dictrict = defaultdict(int)
    pincode_and_district = dict()

    year = year[-2:]
    for entry in pincode_data:
        pincode_and_district[entry["Pin Code"][:4]] = entry["District"]

    pincode_list = list(pincode_and_district.keys())

    for entry in maharashtra_data:

        if year == entry["DATE_OF_REGISTRATION"][-2:] and entry["DATE_OF_REGISTRATION"] != "NA":

            entry_data = entry["Registered_Office_Address"].strip().split(",")

            raw_pincode = entry_data[-1].strip().split(" ")
            district_pincode = raw_pincode[-1][:4]

            if district_pincode in pincode_list:
                reg_by_dictrict[pincode_and_district[district_pincode]] += 1

    return reg_by_dictrict


def transfrom_to_plot(data_to_plot):
    """Transformation of data to plot"""
    data_to_plot = dict(sorted(data_to_plot.items(),
                        key=lambda item: item[1], reverse=1))
    district = list(data_to_plot.keys())
    registration = list(data_to_plot.values())

    return district, registration


def plot(district, registration):
    """Bar plot of registration by district"""

    plt.bar(district, registration)
    plt.xticks(district, rotation=90, fontsize=6)
    plt.tight_layout()
    plt.show()


def main():
    """Count the registration by the district."""

    year = 2015
    maharashtra_data = maharastra_df()
    pincode_data = pincode()
    reg_by_dictrict_output = registration_by_district(
        str(year), maharashtra_data, pincode_data)
    district, registration = transfrom_to_plot(reg_by_dictrict_output)
    plot(district, registration)


if __name__ == "__main__":
    main()
