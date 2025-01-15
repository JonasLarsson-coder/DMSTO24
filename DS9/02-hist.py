

import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("/Users/jonas/Desktop/Studier/Data Manager, TUC 2024/DataScience/DS9/Data-Visualization")
print(dataFrame["Age"].head())

plt.hist(dataFrame["Age"].dropna())
plt.title("Fördelning av ålder")
plt.show()