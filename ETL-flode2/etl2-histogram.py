import pandas as pd
import matplotlib.pyplot as plt

# Läs in den filtrerade CSV-filen
file_path = "/Users/jonas/Downloads/befolkningsforandring-filtrerad.csv"
data = pd.read_csv(file_path)

# Lista över kolumner att visualisera
columns_to_plot = ["födda", "döda"]

for column in columns_to_plot:
    plt.hist(data[column], bins=10, alpha=0.7, edgecolor="black", label=column)

# Anpassa diagrammet
plt.title("Histogram över födda och döda")
plt.xlabel("Antal")
plt.ylabel("Frekvens")
plt.legend()  # Visa en legend för att skilja mellan kolumner

# Visa diagrammet
plt.show()
