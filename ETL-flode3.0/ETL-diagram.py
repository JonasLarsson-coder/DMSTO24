import pandas as pd
import matplotlib.pyplot as plt

"""Skapar ett histogram som visar hunr många som föds och dör varje år. Diagramet visar att det föds fler än det dör varje år"""

# Ange sökvägen till Excel-filen
excel_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.xlsx"

# Läs in data från Excel-filen
data = pd.read_excel(excel_file)

# Filtrera data för att endast visa år mellan 2003 och 2023
filtered_data = data[(data["år"] >= 2003) & (data["år"] <= 2023)]

# Skapa ett histogram
plt.figure(figsize=(12, 6))

# Skapa stapeldiagram för Födda och Döda
plt.bar(filtered_data["år"] - 0.2, filtered_data["födda"], width=0.4, color="blue", label="Födda")
plt.bar(filtered_data["år"] + 0.2, filtered_data["döda"], width=0.4, color="red", label="Döda")

# Anpassa diagrammet
plt.title("Histogram: Födda och Döda per År (2003-2023)")
plt.xlabel("År")
plt.ylabel("Antal")
plt.legend()

# Justera och tilt x-axeln för att visa årtalen korrekt
plt.xticks(filtered_data["år"], rotation=45, ha="right")

# Visa diagrammet
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
"""skapra ett linjediagram som visar hur många som föds och dör varje år. Diagramet visar att det föds fler än det dör varje år"""
# Ange sökvägen till Excel-filen
excel_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.xlsx"

# Läs in data från Excel-filen
data = pd.read_excel(excel_file)

# Filtrera data för att endast visa år mellan 2003 och 2023
filtered_data = data[(data["år"] >= 2003) & (data["år"] <= 2023)]

# Sortera data baserat på år
filtered_data = filtered_data.sort_values(by="år")

# Skapa en figur för linjediagram
plt.figure(figsize=(10, 6))

# Linjediagram för Födda (blå)
plt.plot(filtered_data["år"], filtered_data["födda"], color="blue", label="Födda", marker="o", linestyle="-", markersize=5)

# Linjediagram för Döda (röd)
plt.plot(filtered_data["år"], filtered_data["döda"], color="red", label="Döda", marker="o", linestyle="-", markersize=5)

# Anpassa diagrammet
plt.title("Linjediagram: Födda och Döda per År (2003-2023)")
plt.xlabel("År")
plt.ylabel("Antal")
plt.legend()

# Ställ in så att x-axeln endast visar heltal
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# Visa diagrammet
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Ange sökvägen till Excel-filen
excel_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.xlsx"

# Läs in data från Excel-filen
data = pd.read_excel(excel_file)

# Skapa en figur för scatterplot
plt.figure(figsize=(10, 6))

# Skapa scatterplot för "födda" med blå färg
plt.scatter(data["år"], data["födda"], color="blue", label="Födda", alpha=0.7, edgecolor="black")

# Skapa scatterplot för "döda" med röd färg
plt.scatter(data["år"], data["döda"], color="red", label="Döda", alpha=0.7, edgecolor="black")

# Anpassa diagrammet
plt.title("Scatterplot: Födda och Döda per År")
plt.xlabel("År")
plt.ylabel("Antal")
plt.legend()

# Visa diagrammet
plt.grid(True)
plt.tight_layout()
plt.show()


"""skapar ett stapeldiagram för skillnaden mellan födda och döda varje år. Staplarna visar hur många fler som föds än som dör varje år"""
import pandas as pd
import matplotlib.pyplot as plt

# Ange sökvägen till Excel-filen
excel_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.xlsx"

# Läs in data från Excel-filen
data = pd.read_excel(excel_file)

# Filtrera data för att endast visa år mellan 2003 och 2023 och skapa en kopia för att undvika varningen
filtered_data = data[(data["år"] >= 2003) & (data["år"] <= 2023)].copy()

# Skriv ut alla årtal i konsolen
print("Alla årtal:")
print(filtered_data["år"].tolist())

# Beräkna skillnaden mellan födda och döda
filtered_data["skillnad"] = filtered_data["födda"] - filtered_data["döda"]

# Skapa ett diagram för skillnaden mellan födda och döda varje år
plt.figure(figsize=(10, 6))

# Skapa ett stapeldiagram
plt.bar(filtered_data["år"], filtered_data["skillnad"], color="skyblue")

# Anpassa diagrammet
plt.title("Skillnad mellan Födda och Döda per År (2003-2023)")
plt.xlabel("År")
plt.ylabel("Skillnad (Födda - Döda)")

# Sätt alla årtal på x-axeln
plt.xticks(filtered_data["år"], rotation=45, ha="right")

# Visa diagrammet
plt.tight_layout()
plt.show()
