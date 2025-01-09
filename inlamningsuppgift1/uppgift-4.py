"""Fibonacci’s talföljd är en talföljd där varje tal är summan av de två föregående talen. Talföljden börjar med 0 och 1. De första talen i talföljden är:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."""

#Skriv en funktion fibonacci(n: int) -> List[int] som returnerar en lista med de n första talen i Fibonacci’s talföljd.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))


"""PASS i PYTEST"""