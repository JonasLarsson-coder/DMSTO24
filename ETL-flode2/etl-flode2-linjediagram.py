import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen
file_path = "/Users/jonas/Downloads/befolkningsforandring-filtrerad.csv"
data = pd.read_csv(file_path)

# Skapa linjediagram för "födda" och "döda"
plt.plot(data["år"], data["födda"], marker='o', color="blue", label="Födda", linestyle='-', linewidth=2)
plt.plot(data["år"], data["döda"], marker='o', color="red", label="Döda", linestyle='-', linewidth=2)

# Anpassa diagrammet
plt.title("Utveckling av Födda och Döda över tid")
plt.xlabel("År")
plt.ylabel("Antal")
plt.xticks(rotation=45, ha="right")  # Rotera årtalen för bättre läsbarhet
plt.legend()  # Visa en legend

# Visa diagrammet
plt.tight_layout()  # Justera layouten så allt får plats
plt.show()
