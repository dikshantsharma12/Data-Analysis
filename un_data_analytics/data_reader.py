import csv

def population_data():
    """Fucntion to read data"""
    try:
        data=open("population.csv","r")
        data=csv.DictReader(data)
        return data
    except IOError:
        print("Data not found!")