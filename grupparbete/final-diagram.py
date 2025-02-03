import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

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

# Filtrera bort rader där "County" innehåller "Okänt" (som vi gjorde i den tidigare versionen av koden)
df_accidents = df_accidents[~df_accidents['County'].str.contains("Okänt", na=False)]

# Ta bort data för 2024 då vi saknar befolkningsdata, för att allt ska mätas rättvist
df_accidents = df_accidents[df_accidents["Year"] <= 2023]

# Aggreggera olycksdata till årsnivå
df_accidents = df_accidents.groupby(["County", "Year"]).agg({"Quantity": "sum"}).reset_index()

# Slå ihop olycksdata med befolkningsdata
merged_df = df_accidents.merge(df_population, on=["County", "Year"], how="left")

# Beräkna olyckor per 1000 invånare
merged_df["Accidents_per_1000"] = (merged_df["Quantity"] / merged_df["Population"]) * 1000

# Skapa statistik per år och län
yearly_stats = merged_df.groupby(["County", "Year"]).agg(
    skadade_per_1000=("Accidents_per_1000", "sum")
).reset_index()

# Förutsäga olyckor per 1000 invånare fram till 2028 med linjär regression
future_years = np.array(range(2024, 2029)).reshape(-1, 1)

predictions = []

if not yearly_stats.empty:
    for year in future_years.flatten():
        for county in yearly_stats["County"].unique():
            subset = yearly_stats[yearly_stats["County"] == county]
            if subset.shape[0] > 1:  # Kontrollera att det finns tillräckligt med data för att träna modellen
                X = subset["Year"].values.reshape(-1, 1)
                y = subset["skadade_per_1000"].values
                
                model = LinearRegression()
                model.fit(X, y)
                future_pred = model.predict([[year]])[0]
                
                predictions.append([county, year, future_pred])

# Skapa en DataFrame för prognosen om vi har några värden
if predictions:
    predictions_df = pd.DataFrame(predictions, columns=["County", "Year", "Predicted_skadade_per_1000"])
else:
    predictions_df = pd.DataFrame(columns=["County", "Year", "Predicted_skadade_per_1000"])

# Beräkna förändringen från 2024 till 2028 per län
df_pivot = predictions_df.pivot(index="County", columns="Year", values="Predicted_skadade_per_1000")
df_pivot["Change"] = df_pivot[2028] - df_pivot[2024]

# Hämta de fem län med störst förändring
top_5_counties = df_pivot["Change"].nlargest(5)
top_5_counties_list = top_5_counties.index.tolist()

# Filtrera data för dessa län
df_top5 = predictions_df[predictions_df["County"].isin(top_5_counties_list)]

# Skapa linjediagram
plt.figure(figsize=(10, 6))

# Plotta varje läns utveckling över åren
for county in top_5_counties_list:
    county_data = df_top5[df_top5["County"] == county]
    plt.plot(county_data["Year"], county_data["Predicted_skadade_per_1000"], marker="o", linestyle="-", label=county)

# Anpassa diagrammet
plt.legend()
plt.title("Prognos: Skadade per 1000 invånare per län (2024-2028)")
plt.xlabel("År")
plt.ylabel("Predicerade skadade per 1000 invånare")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Spara den sammanfogade datan och prognosen till en ny Excel-fil
output_file = "kombinerad_data.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    merged_df.to_excel(writer, sheet_name="Kombinerad Data", index=False)
    yearly_stats.to_excel(writer, sheet_name="Årlig Statistik", index=False)
    if not predictions_df.empty:
        predictions_df.to_excel(writer, sheet_name="Prognos 2024-2028", index=False)

# Linjediagram för skadade per 1000 invånare per län
plt.figure(figsize=(12, 6))
for county in yearly_stats["County"].unique(): #yearly_stats["County"].unique():
    subset = yearly_stats[yearly_stats["County"] == county]
    plt.plot(subset["Year"], subset["skadade_per_1000"], label=county)
plt.legend()
plt.title("Linjediagram: Skadade per 1000 invånare per län (2000-2023)")
plt.xlabel("År")
plt.ylabel("Skadade per 1000 invånare")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Horisontellt stapeldiagram för ett specifikt år (2023)
year_2023 = yearly_stats[yearly_stats["Year"] == 2023]
year_2023 = year_2023.sort_values(by="skadade_per_1000", ascending=False)
plt.figure(figsize=(12, 6))
plt.barh(year_2023["County"], year_2023["skadade_per_1000"], color="skyblue")
plt.title("Skadade per 1000 invånare per län (2023)")
plt.xlabel("Skadade per 1000 invånare")
plt.ylabel("Län")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

# Linjediagram för prognos 2024-2028 (Maskininlärning)
plt.figure(figsize=(12, 6))
for county in predictions_df["County"].unique():
    subset = predictions_df[predictions_df["County"] == county]
    plt.plot(subset["Year"], subset["Predicted_skadade_per_1000"], linestyle="--", marker="o", label=county)
plt.legend()
plt.title("Prognos: Skadade per 1000 invånare per län (2024-2028)")
plt.xlabel("År")
plt.ylabel("Predicerade skadade per 1000 invånare")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Läs in Excel-filen
file_path = "/Users/jonas/Downloads/bearbetad_data.xlsx"
xls = pd.ExcelFile(file_path)

# Läs in "Rådata"
df = pd.read_excel(xls, sheet_name="Rådata")

# Filtrera bort rader där "County" innehåller "Okänt"
df = df[~df['County'].str.contains("Okänt", na=False)]

# Ta bort kolumnen "Severity" om den finns
df = df.drop(columns=["Severity"], errors="ignore")


# 🔹 Klustring av län baserat på olycksnivå
county_accidents = df.groupby("County")["Quantity"].sum().reset_index()

# Standardisera datan
scaler = StandardScaler()
county_accidents["Quantity_Scaled"] = scaler.fit_transform(county_accidents[["Quantity"]])

# KMeans-klustring (3 kluster)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
county_accidents["Cluster"] = kmeans.fit_predict(county_accidents[["Quantity_Scaled"]])

# 🔹 Sortera klustrens nivåer
cluster_means = county_accidents.groupby("Cluster")["Quantity"].mean().sort_values()
sorted_clusters = {cluster_means.index[0]: "Lågrisk",
                   cluster_means.index[1]: "Mellannivå",
                   cluster_means.index[2]: "Högrisk"}

county_accidents["Cluster_Label"] = county_accidents["Cluster"].map(sorted_clusters)

# 🔹 Statistik per kluster
cluster_stats = county_accidents.groupby("Cluster_Label")["Quantity"].agg(["mean", "std", "count"])
print("📊 Statistik per kluster:\n", cluster_stats)

# 🔹 Scatterplot för klustringen
plt.figure(figsize=(10, 6))
cluster_colors = {"Lågrisk": "green", "Mellannivå": "orange", "Högrisk": "red"}
for label, color in cluster_colors.items():
    subset = county_accidents[county_accidents["Cluster_Label"] == label]
    plt.scatter(subset["County"], subset["Quantity"], label=label, color=color, edgecolors="black")

plt.title("Klustring av län baserat på antal olyckor", fontsize=14)
plt.xlabel("Län", fontsize=12)
plt.ylabel("Totalt antal olyckor", fontsize=12)
plt.xticks(rotation=90)
plt.legend(title="Risknivå")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()



# 🔹 Regression för framtida olycksprognoser
df_yearly = df.groupby("Year")["Quantity"].sum().reset_index()

X = df_yearly["Year"].values.reshape(-1, 1)
y = df_yearly["Quantity"].values

model = LinearRegression()
model.fit(X, y)

future_years = np.array(range(df_yearly["Year"].max() + 1, df_yearly["Year"].max() + 6)).reshape(-1, 1)
future_predictions = model.predict(future_years)

# 🔹 Skapa en DataFrame för framtida olycksprognoser
future_df = pd.DataFrame({
    "Year": future_years.flatten(),
    "Quantity": [None] * len(future_years),  # Ingen faktisk data
    "Prediction": future_predictions  # Förutsägelser
})

# 🔹 Slå ihop historisk data och framtida prognoser
df_regression = pd.concat([df_yearly, future_df], ignore_index=True)

# 🔹 Plotta regressionen
plt.figure(figsize=(10, 5))
plt.scatter(df_yearly["Year"], df_yearly["Quantity"], color="blue", label="Historiska data")
plt.plot(df_yearly["Year"], model.predict(X), color="red", linestyle="--", label="Trendlinje")
plt.plot(future_years, future_predictions, color="green", linestyle="--", label="Prognos (5 år framåt)")

plt.title("Förutsägelse av trafikolyckor (linjär regression)", fontsize=14)
plt.xlabel("År", fontsize=12)
plt.ylabel("Antal olyckor", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 🔹 Spara uppdaterad data till Excel
with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Rådata", index=False)
    county_accidents.to_excel(writer, sheet_name="Klustring av län", index=False)
    df_regression.to_excel(writer, sheet_name="Regression (Olycksprognos)", index=False)

# Bekräftelsemeddelande
print("✅ Data bearbetad och sparad!")
print("✅ Scatterplot och linjediagram finns nu med!")
print("✅ Regression lagd till - framtida olyckstrend kan nu analyseras!")