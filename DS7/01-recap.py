

with open("data.csv", "w") as file:
    # Vi skriver till filen, rad 1, rubrikerna:
    file.write("Name,Age,City\n")
# Nu är filen stängd.    

#Öppnar filen igen, med append ("a")
with open("data.csv", "a") as file:
    # \n gör ett radbryt.  
    file.write("Anna, 25, Stockholm\n")
    file.write("Björn, 30, Göteborg\n")
    file.write("Jonas, 40, Göteborg\n")
    file.write("Lily, 12, Stockholm\n")
    file.write("Liam, 14, Stockholm\n")
    file.write("Olof, 56, Malmö\n")

# Öpnna i läsläge.
with open("data.csv") as file:
    #skriv ut innehållet.
    print(file.read())

print("Rad för rad:")
#vi kanske vill jobba med rad för rad.
with open ("data.csv") as file:
    #loopa igenom rad för rad.
    for line in file:
        # Do something
        # "strip" tar bort den extra radbrytningen.
        print(line.strip())
        letaEfter = "Jonas"
        if letaEfter in line:
            print(f"{letaEfter} är bäst!")
            print(f"Hela raden: {line}")