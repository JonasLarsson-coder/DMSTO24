
def count_letters(string):
    # Skapa en tom dictionary för att lagra bokstäver och deras antal
    letter_count = {}
    
    # Iterera över varje tecken i strängen
    for char in string:
        # Kontrollera om tecknet är en bokstav
        if char.isalpha():
            char = char.lower()  # Gör bokstaven gemen för att ignorera skiftläge
            # Öka räkningen för bokstaven
            letter_count[char] = letter_count.get(char, 0) + 1
    
    return letter_count


print(count_letters("Jag heter Jonas"))
