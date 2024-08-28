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
valeurs_somme = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]

test_somme = ValidateFunctionPretty(
    "somme", valeurs_somme, valid_function = somme_cor
)

## Fonction racine
def racine_cor(a:int) -> int :
    return a**(.5)
valeurs_racine = [random.randint(0, 30) for _ in range(5)]

test_racine_ = ValidateFunctionPretty(
    "racine", valeurs_racine, valid_function = racine_cor
)

## Fonction inv_racine
def inv_racine_cor(a:int) -> int :
    return 1/(a**(.5))
valeurs_inv_racine = [random.randint(1, 30) for _ in range(5)]

test_inv_racine = ValidateFunction(
    "inv_racine", valeurs_inv_racine, valid_function = inv_racine_cor
)

## Fonction est_pair
def est_pair_cor(a:int) -> int :
    return a%2 == 0
valeurs_est_pair = [random.randint(1, 30) for _ in range(5)]

test_est_pair = ValidateFunction(
    "est_pair", valeurs_est_pair, valid_function = est_pair_cor
)

## Fonction puissance_2_for
def puissance_2_for_cor(n:int) -> int :
    res = 1
    for i in range(n) :
        res = res*2
    return res

valeurs_puissance_2_for = [random.randint(-20, 20) for _ in range(5)]

test_puissance_2_for = ValidateFunctionPretty(
    "puissance_2_for", valeurs_puissance_2_for, valid_function = puissance_2_for_cor
)

## Fonction puissance_for
def puissance_for_cor(a:float,n:int) -> float :
    res = 1
    for i in range(n) :
        res = res*a
    return res

valeurs_puissance_for = [(random.randint(-20, 20),random.randint(-20, 20)) for _ in range(5)]

test_puissance_for = ValidateFunctionPretty(
    "puissance_for", valeurs_puissance_for, valid_function = puissance_for_cor
)


## Fonction puissance_2_while
def puissance_2_while_cor(n:int) -> int :
    res = 1
    for i in range(n) :
        res = res*2
    return res

valeurs_puissance_2_while = [random.randint(-20, 20) for _ in range(5)]

test_puissance_2_while = ValidateFunctionPretty(
    "puissance_2_while", valeurs_puissance_2_while, valid_function = puissance_2_while_cor
)

## Fonction puissance_while
def puissance_while_cor(a:float,n:int) -> float :
    res = 1
    for i in range(n) :
        res = res*a
    return res

valeurs_puissance_while = [(random.randint(-20, 20),random.randint(-20, 20)) for _ in range(5)]

test_puissance_while = ValidateFunctionPretty(
    "puissance_while", valeurs_puissance_while, valid_function = puissance_while_cor
)


##
def factoriel_while_cor(n):
    a=0
    b=1
    c=1
    while a<n-1:
        b=b*(c+1)
        c=c+1
        a=a+1
    return (b)
valeurs_factoriel_while = [random.randint(0, 6) for _ in range(5)]

test_factoriel_while = ValidateFunctionPretty(
    "factoriel_while", valeurs_factoriel_while, valid_function = factoriel_while_cor
)

def factoriel_for_cor(n):
    b = 1
    c = 1
    for i in range (n-1):
        b = b*(c+1)
        c = c+1
    return (b)
valeurs_factoriel_for = [random.randint(0, 6) for _ in range(5)]

test_factoriel_for = ValidateFunctionPretty(
    "factoriel_for", valeurs_factoriel_for, valid_function = factoriel_for_cor
)




def binomial_cor(n,k):
    a = factoriel_for_cor(n)
    b = factoriel_for_cor(k)
    c = factoriel_for_cor(n-k)
    return (a/(b*c))
valeurs_binomial = [(random.randint(0, 20),random.randint(0, 20)) for _ in range(5)]
test_binomial = ValidateFunctionPretty(
    "binomial", valeurs_binomial, valid_function = binomial_cor
)