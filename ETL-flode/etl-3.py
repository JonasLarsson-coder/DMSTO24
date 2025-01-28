import matplotlib.pyplot as plt
import pandas as pd
import csv
dataFrame = pd.read_csv("/Users/jonas/Desktop/Studier/Data Manager, TUC 2024/DataScience/ETL-flode/KIR-data.csv")
print(dataFrame["Ålder"])

plt.hist(dataFrame["Ålder"])
plt.title("Fördelning av ålder")
plt.show()