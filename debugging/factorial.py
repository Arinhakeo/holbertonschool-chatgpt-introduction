#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Diminue n de 1 à chaque itération pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)