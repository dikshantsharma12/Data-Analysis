import csv
def maharastra_df():
    try:
        df=open("Maharashtra.csv","r",encoding='latin1')
        df=csv.DictReader(df)
        return df
    except IOError:
        print("File Not Found")

    

def pincode():
    try:
        pincode_df=open("pincode.csv","r")
        pincode_df=csv.DictReader(pincode_df)
        return pincode_df
    except IOError:
        print("Pincode Data Not Found")

    
