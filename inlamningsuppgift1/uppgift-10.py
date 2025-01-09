
# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.


def celsius_to_fahrenheit(celsius):
    # Formeln för att konvertera Celsius till Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


print(celsius_to_fahrenheit(5))   
print(celsius_to_fahrenheit(2))  
print(celsius_to_fahrenheit(-3))  
print(celsius_to_fahrenheit(30))

"""PASS i PYTEST!"""
