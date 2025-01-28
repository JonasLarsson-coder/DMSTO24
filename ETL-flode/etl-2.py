import csv  
import pandas as pd

result = pd.read_csv("KIR-data.csv")

def transfom_data(data):
    filterd_data = data[data["Ålder"] > 100]

    #Lägg till en kolumn med beräknasd data
    filterd_data['Ålder_om_10_år'] = filterd_data['Ålder'] + 10

    print("Data transformed successfully!")
    return filterd_data
#3.Load, spara transfomerad data till en ny CSV fil

def load(data):
    data.to_csv("transformed_data.csv", index=False)
    print("Data saved to file successfully!")

    print(data.head())  

