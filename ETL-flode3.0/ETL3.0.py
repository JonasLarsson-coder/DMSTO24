import pandas as pd

# Ange filvägar
input_file = "/Users/jonas/Downloads/befolkningsforandring-helar.csv"  # Original CSV-fil
csv_output_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.csv"  # CSV med kommatecken
excel_output_file = "/Users/jonas/Downloads/befolkningsforandring-filtrerad2.xlsx"  # Excel-fil

# Läs in CSV-fil och justera separator (ändra sep om nödvändigt)
data = pd.read_csv(input_file, sep=";")  # Om filen har semikolon som separator

# Välj endast de kolumner du vill behålla
columns_to_keep = ["år", "födda", "döda"]  # Anpassa efter filens exakta kolumnnamn
filtered_data = data[columns_to_keep]

# Spara den filtrerade datan med kommatecken som separator
filtered_data.to_csv(csv_output_file, sep=",", index=False)

# Spara till en Excel-fil
filtered_data.to_excel(excel_output_file, index=False, sheet_name="Befolkningsdata")

print(f"CSV-filen har sparats som {csv_output_file} med kommatecken.")
print(f"Excel-filen har sparats som {excel_output_file}.")


"""konvertarade skiljeteceken från ; till , och sparade filen som en ny csv fil och en excel fil"""
#rensade bort onödiga kolumner och sparade filen som en ny csv fil och en excel fil
#kolumnerna som behölls var år, födda och döda, dessa sparades i en ny csv fil och en excel fil.
#ecell-filen sparas och används till att skapa diagram. 