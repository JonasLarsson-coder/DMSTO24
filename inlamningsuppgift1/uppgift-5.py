"""Uppgift 5

Filtrera udda tal från en lista
Beskrivning:
Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan."""


siffror = [1, 2, 3, 4] #lista med olika tal

from typing import List

def filter_odd(siffror: List [int]) -> int:
    """returnerar en lista med alla jämna tal från den givna listan"""
    return siffror % 2 != 0
print (filter_odd( siffror))


"""PASS i PYTEST"""
