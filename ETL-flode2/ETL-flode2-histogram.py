import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Läs in CSV-filen
file_path = "/Users/jonas/Downloads/befolkningsforandring-filtrerad.csv"
data = pd.read_csv(file_path)

# Skapa en position för varje år (x-axel)
x = np.arange(len(data["år"]))  # Antalet år
width = 0.4  # Bredden på varje stapel

# Skapa staplar för "födda" och "döda"
plt.bar(x - width/2, data["födda"], width, color="blue", label="Födda")
plt.bar(x + width/2, data["döda"], width, color="red", label="Döda")

# Anpassa diagrammet
plt.title("Antal födda och döda per år")
plt.xlabel("År")
plt.ylabel("Antal")
plt.xticks(x, data["år"], rotation=45, ha="right")  # Rotera årtalen 45 grader och justera horisontellt

# Lägg till legend och justera layouten
plt.legend()
plt.tight_layout()

# Visa diagrammet
plt.show()
