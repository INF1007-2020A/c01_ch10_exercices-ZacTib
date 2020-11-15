#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *
from sympy import exp


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0

def creer_graphe():
    abscisses = np.linspace(-1, 1, num=250)
    ordonnee = [x**2 * math.sin(1/x**2) + x for x in abscisses]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(abscisses, ordonnee)
    ax.set_title('Fonction')
    ax.set_ylabel('Ordonnée')
    ax.set_xlabel('Abscisse')
    ax.set_xlim(xmin=-1, xmax=1)
    fig.tight_layout()
    plt.show()

    return None

def integrale():

    x = Symbol('x')
    a = integrate(exp(-x**2), (x, -math.inf, math.inf))
    print(a)
    absisses = np.linspace(-4, 4, num=250)
    ordonnee = [exp(-x**2) for x in absisses]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(absisses, ordonnee)
    ax.set_title('Fonction')
    ax.set_ylabel('Ordonnée')
    ax.set_xlabel('Absisse')
    ax.set_xlim(xmin=-4, xmax=4)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    creer_graphe()
    integrale()

    pass
