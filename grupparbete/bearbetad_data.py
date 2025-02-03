"""Ta bort skadade kolumnen, för den tillför inga unika värden. enl dokumentationen för kolumnen skulle den datan vara specifik.
Räkna ut procentull fördelning av dom olika typerna av olyckor per län
Vi vill ta bort "okända" för den datan är inte användbar
#Har kollat  https://www.dataportal.se/datasets/272_5269 men inte hittat något mer användbart. 
#Klustring av grupper (län)
#Visualisera data med hjälp av nya diagram t.ex--> årsvis redovisning av olyckor (10 största länen)
#Har undersökt SMHI öppen data för att försöka kombinera--> Deras data är utformad på ett helt annat sätt och inte applicerbar för oss."""



import pandas as pd

file_path = "/Users/jonas/Desktop/Studier/Data Manager, TUC 2024/DataScience/grupparbete/bearbetad_data_filtrerad.csv"  # Ändra sökvägen vid behov

df = pd.read_csv(file_path)

print(df["County"].unique())



