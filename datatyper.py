
x = "123"
y = 2

print(int(x)*y)

#eller

x = "123"
y = 2
z = int(x) * y
print(z) 

a = 5+2
b = 5 // 2
c = 5 % 2
d = 5**2
print(a, b, c, d)

x = 0.1 + 0.2
print(x)

from decimal import Decimal

x = Decimal('0.1') + Decimal('0.2')

print(x)

print("Hej" * 3)

text = "DataScience"

print(text[0])

print(text[-1])

print(text[0],text[1])

print(text[0:5])

text = " Python är roligt "

no_whitespace = text.strip()

print(no_whitespace)

fantastico = no_whitespace.replace("roligt", "fantastiskt")

print(fantastico)

UPPER = fantastico.upper()

print(UPPER)


name = input("Vad heter du? ")
age = input("Hur gammal är du? ")
svar = (name) + (age)
print(f"Hej {name}, du är {age} år gammal!")

a = "hej"
print(a)