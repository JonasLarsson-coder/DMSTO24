import csv
with open("products.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

data[0].append("category") 

for i in range(1,len(data)):
    data[i].append("Fruits")

for i in range(1, len(data)):
    data[i].append("Fruits")

for i in range(len(data)):
    print(data[i])

with open("new-producs.csv", "w") as new_products:
    writer = csv.writer(new_products)
    writer.writerows(data)


  
  