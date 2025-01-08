# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

numbers = [1, 2, 3]
from typing import List

def sum_list(numbers: List [int]) -> int:
    """
    Returnerar summan av alla siffror i listan.
    """
    return sum(numbers)
print(sum_list(numbers))