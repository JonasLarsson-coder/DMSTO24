"""Skap ett ETL-flöde"""
#1. Extrahera data
import csv  
import pandas as pd
with open ("KIR-data.csv", "r") as file:
    dataFrame = csv.reader("KIR-data.csv")
    for row in dataFrame:
        print(row)
#läser in csv-filen och skriver ut varje rad i filen.

#2.transfom och bearbeta data

def transfom_data(data):
    filterd_data = data[data["Ålder"] > 30]

    #Lägg till en kolumn med beräknasd data
    filterd_data['Ålder_om_10_år'] = filterd_data['Ålder'] + 10

    print("Data transformed successfully!")
    return filterd_data
#3.Load, spara transfomerad data till en ny CSV fil

def load(data):
    data.to_csv("transformed_data.csv", index=False)
    print("Data saved to file successfully!")