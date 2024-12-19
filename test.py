namn = "Anna"
ålder = 25
print(f"hej, vad heter du? {namn}. Hur gammal är du? {ålder} ")


x = 23
y = 12
z = x+y
print (z)

# Summan av x och y är:
x = 10
y = 20
summa = x+y
print (f"{summa}")

x = 42
y = str(x)
print(y)
print(type(y))

if 5 > 2:
  print("Five is greater than two!")

x = 42
text = "Talet är: " + str(x) 
print(text)


namn = "Jonas"
efternamn = "Larsson"
ålder = 39
fullnamn = namn + " " + efternamn
print(fullnamn + " " + str(ålder))

text = "Data science"
print(text[0]) #skriver ut den första bokstaven. 
print(text[1]) #skriver ut den andra bokstaven.
print(text[2])
print(text[3])
print(text[4])
print(text[-1]) #skriver ut den sista bokstaven

try:
    x = int("hej") # Försöker konvertera en sträng till heltal
except:
    print("Ett fel uppstod.")


my_list = ["jonas", "Mary", "Liam", "Lily"] #skapa en list med namn.
for names in my_list: #skriv ut hela listan
    print(names)