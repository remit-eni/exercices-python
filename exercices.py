"""
Exercices.

Implémentez les méthodes ci-dessous.
Pour executer vos tests il vous faudra utiliser pytest
"""
from pip._vendor.msgpack.fallback import xrange
import math


def htc_to_ttc(htc_cost: float, discount_rate: float = 0) -> float:
    taxe = 1.206

    if (discount_rate != 0):
        taxe = taxe - (taxe * discount_rate)
    if (discount_rate < 0 and discount_rate > 1):
        print(Exception)

    ttc = round(htc_cost * taxe, 2)
    return ttc

    """
    Exercice 1 :
    Calcule le coût TTC d'un produit.
    discount_rate : taux de réduction compris entre 0 et 1
    Taux de taxes : 20.6 % g
    Retourne un float arrondi à deux décimales
    """


def divisors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    if factors == [1, n]:
        return 'PREMIER'

    return factors
    """
    Exercice 2 :
    A partir d'un nombre donné,
    retourne ses diviseurs (sans répétition)
    s’il y en a, ou « PREMIER » s’il n’y en a pas.
    """
