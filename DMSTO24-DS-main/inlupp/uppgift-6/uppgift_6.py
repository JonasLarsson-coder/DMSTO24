# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n, limit):
    # Skapa en lista med multiplikationstabellen för n upp till limit
    return [n * i for i in range(1, limit + 1)]

print(multiplication_table(5, 10))
#5ans multiplikationstabell, 5*1 upp till 5*10