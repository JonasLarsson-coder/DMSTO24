"""det här är ett exempel på ett dictionare"""

person = {
    "name": "Jonas",
    "Age": 40,
    "city": "Göteborg"
}

print(person)
#skriver ut hela listan

print(person["name"])
#skriver ut endas namnet

print(person["Age"])
#skriver ut Age

print(person["city"])
#skriver ut city

"""Lägg till ett nytt nyckelvärde-par"""

person["profession"] = "Engineer"
print(person)
#Profession har nu lagts till i dictionaryn "person"

person["Age"] = 39
print(person)
#Age har nu uppdaterats till 39     