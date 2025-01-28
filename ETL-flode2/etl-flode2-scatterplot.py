import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen
file_path = "/Users/jonas/Downloads/befolkningsforandring-filtrerad.csv"
data = pd.read_csv(file_path)

# Skapa ett scatter plot
plt.scatter(data["år"], data["födda"], color="blue", label="Födda", alpha=0.7)
plt.scatter(data["år"], data["döda"], color="red", label="Döda", alpha=0.7)

# Anpassa diagrammet
plt.title("Scatter Plot: Födda och Döda över tid")
plt.xlabel("År")
plt.ylabel("Antal")
plt.xticks(rotation=45, ha="right")  # Rotera årtalen för bättre läsbarhet
plt.legend()  # Visa en legend

# Visa diagrammet
plt.tight_layout()  # Justera layouten så allt får plats
plt.show()
