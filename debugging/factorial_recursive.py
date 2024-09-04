#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le facteuriel d'un nombre entier non négatif.

    Description de la fonction:
        La fonction `factorial` calcule le produit de tous les entiers positifs
        jusqu'à `n` en utilisant la récursion. Le cas de base est `n == 0`,
        pour lequel la fonction retourne 1, car 0! est défini comme étant égal à 1.

    Paramètres:
        n (int): Un entier non négatif dont nous souhaitons calculer le facteuriel.

    Valeurs de retour:
        int: Le facteuriel de `n`. Si `n` est 0, la fonction retourne 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérifie si un argument est passé en ligne de commande
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

# Convertit l'argument en entier et calcule le facteuriel
try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Le nombre doit être un entier non négatif.")
except ValueError as e:
    print(f"Erreur: {e}")
    sys.exit(1)

f = factorial(number)
print(f)
