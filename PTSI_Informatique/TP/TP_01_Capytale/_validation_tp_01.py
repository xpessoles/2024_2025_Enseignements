from capytale.autoeval import (
    Validate,
    ValidateVariables,
    ValidateFunction,
    ValidateFunctionPretty,
)
from itertools import product
import random


## Validation de la cellule d'import
cellule_import = Validate()


## Fonction somme
def somme_cor(a:int,b:int) -> int :
    return a+b
valeurs = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]
valeurs_cibles = [somme_cor(v[0],v[1]) for v in valeurs]

test_somme = ValidateFunctionPretty(
    "somme", valeurs, target_values=valeurs_cibles
)

