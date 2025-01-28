import pandas as pd

# Läs in CSV-filen
file_path = ("/Users/jonas/Downloads/befolkningsforandring-komma.csv")
data = pd.read_csv(file_path)  

# Välj de kolumner du vill behålla
columns_to_keep = ["år", "födda", "döda"]  # Anpassa efter dina kolumnnamn
filtered_data = data[columns_to_keep]

# Spara det filtrerade resultatet till en ny CSV-fil med kommatecken som avgränsare
output_file_path = "/Users/jonas/Downloads/befolkningsforandring-filtrerad.csv"
filtered_data.to_csv(output_file_path, sep=",", index=False)

print(f"Den filtrerade CSV-filen har sparats till {output_file_path}.")
