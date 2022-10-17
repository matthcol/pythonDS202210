# definition d'une fonction avec Hints
def pgcd(a : int, b : int) -> int:
    """plus grand commun diviseur de 2entiers naturels 
    strictement positifs
    """
    while b != 0:
        r = a % b
        a, b = b, r
    return a