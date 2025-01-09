# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).


def is_palindrome(string):
    # Ta bort mellanslag och gör strängen gemen
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Kontrollera om strängen är samma framifrån och bakifrån
    return cleaned_string == cleaned_string[::-1]


print(is_palindrome("Anna"))             # True
print(is_palindrome("Hello"))            # False

"""PASS i PYTEST!"""
