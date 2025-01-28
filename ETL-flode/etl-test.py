import pandas as pd 
import csv

data = pd.read_csv("KIR-data.csv")


def transform(data):
        # 1. Filtrera bort rader med saknade värden i viktiga kolumner
        data = data.dropna(subset=['YearKey', 'MonthKey', 'WeekKey', 'Date', 'Ålder', 'KVINNOR', 'MAN', 'TOTAL'])
        
        # 2. Kontrollera att summan av 'Women' och 'Men' matchar 'Total'
        data['calculated_total'] = data['KVINNOR'] + data['MAN']
        data = data[data['calculated_total'] == data['TOTAL']]
        data.drop(columns=['calculated_total'], inplace=True)

        # 3. Lägg till en kolumn som beräknar könsfördelning (% kvinnor)
        data['percent_KVINNOR'] = (data['KVINNOR'] / data['TOTAL']) * 100
        
        # 4. Lägg till en kolumn för ålder om 5 år
        data['age_in_5_years'] = data['Ålder'] + 5

        # 5. Gruppera data efter år och månad och summera totalt antal personer
        summary = data.groupby(['YearKey', 'MonthKey']).agg({
            'TOTAL': 'sum',
            'KVINNOR': 'sum',
            'MAN': 'sum'
        }).reset_index()
        summary['percent_KVINNOR'] = (summary['KVINNOR'] / summary['TOTAL']) * 100

      


        
data.to_csv("KIR-data-transformed.csv", index=False)
print("Data saved to KIR-data-transformed.csv")