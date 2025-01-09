
def validate_password(password):
    # Kontrollera att lösenordet är minst 8 tecken långt
    if len(password) < 8:
        return False
    
    # Kontrollera att lösenordet innehåller minst en siffra
    if not any(char.isdigit() for char in password):
        return False
    
    # Lösenordet uppfyller båda kraven
    return True
print(validate_password("password123"))  # True
print(validate_password("password"))  # False

"""PASS i PYTEST"""