import pandas as pd

data = {
   "Name": ["Anna", "Björn", "Cecilia"],
   "Age": [25, 30, 27],
   "City": ["Stockholm", "Göteborg", "Malmö"]
}

df = pd.DataFrame(data)

print(df)
