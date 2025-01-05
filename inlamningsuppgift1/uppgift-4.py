"""Fibonacci’s talföljd är en talföljd där varje tal är summan av de två föregående talen. Talföljden börjar med 0 och 1. De första talen i talföljden är:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."""

#Skriv en funktion fibonacci(n: int) -> List[int] som returnerar en lista med de n första talen i Fibonacci’s talföljd.

fibonaccitalet = 0
tal2 = 1
tal3 = fibonaccitalet + tal2
while fibonaccitalet < 100:
   print(fibonaccitalet)
   fibonaccitalet= tal2
   tal2 = tal3
   tal3 = fibonaccitalet+ tal2


   # OBS!!!! EJ KLAR!