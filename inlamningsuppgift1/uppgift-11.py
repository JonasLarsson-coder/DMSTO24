# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text

def word_count(text):
    # Dela upp texten i ord baserat på mellanslag
    words = text.split()
    # Returnera antalet ord
    return len(words)
print(word_count("hur många ord är det i den här meningen?"))
#Returnerar 9, vilket är antal ord i meningen.

"""PASS i PYTEST!"""
