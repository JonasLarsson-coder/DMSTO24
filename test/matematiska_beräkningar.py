

x = 10
y =  3

print(x+y, x-y, x*y, x/y, x//y, x%y)

#konvertera ett flyttal till heltal
x = 3.14
print(int(x))

#konvertera ett heltal till ett flyttal
x = 5
print(float(x))

x = 0.1
y = 0.2
print(round(x+y, 1))

x = input("Skriv första talet: ") 
y = input("Skriv andra talet: ") 
summa = int(x) + int(y) 
print(f"Summan är: {summa}")


x = 42
text = "Talet är: " + str(x) 
print(text)



try:
    x = int("hej") # Försöker konvertera en sträng till heltal
except:
    print("Ett fel uppstod.")