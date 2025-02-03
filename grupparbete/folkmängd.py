import pandas as pd
 
# Ladda in befolkningsdata
file_path = "/Users/jonas/Downloads/folkmängd.csv"  # Uppdatera sökvägen om nödvändigt
df_population = pd.read_csv(file_path, encoding="latin1")
 
# Filtrera data för åren 2000-2023
df_population = df_population[df_population["år"].between(2000, 2023)]
 
# Ta bort länskoder från "region"-kolumnen så att den matchar olycksdata
df_population["region"] = df_population["region"].str.split(" ", n=1).str[1]  # Tar bort länskoden
 
# Byt namn på kolumner för att matcha olycksdata
df_population.rename(columns={"region": "County", "år": "Year", "Folkmängd": "Population"}, inplace=True)
 
# Ladda in olycksdata
accident_file = "/Users/jonas/Downloads/bearbetad_data.xlsx"
df_accidents = pd.read_excel(accident_file, sheet_name="Rådata")
 
# Filtrera bort rader där "County" innehåller "Okänt"
df_accidents = df_accidents[~df_accidents['County'].str.contains("Okänt", na=False)]
 
# Ta bort data för 2024 då vi saknar befolkningsdata
df_accidents = df_accidents[df_accidents["Year"] <= 2023]
 
# Aggreggera olycksdata till årsnivå
df_accidents = df_accidents.groupby(["County", "Year"]).agg({"Quantity": "sum"}).reset_index()
 
# Slå ihop olycksdata med befolkningsdata
merged_df = df_accidents.merge(df_population, on=["County", "Year"], how="left")
 
# Beräkna olyckor per 1000 invånare
merged_df["Accidents_per_1000"] = (merged_df["Quantity"] / merged_df["Population"]) * 1000
 
# Skapa statistik per år
yearly_stats = merged_df.groupby("Year").agg(
    total_accidents=("Quantity", "sum"),
    mean_accidents_per_1000=("Accidents_per_1000", "mean"),
    total_population=("Population", "sum")
).reset_index()
 
# Spara den sammanfogade datan och statistiken till en ny Excel-fil
output_file = "kombinerad_data.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    merged_df.to_excel(writer, sheet_name="Kombinerad Data", index=False)
    yearly_stats.to_excel(writer, sheet_name="Årlig Statistik", index=False)
 
print(f"Kombinerad data och statistik sparad som {output_file}")
 
 