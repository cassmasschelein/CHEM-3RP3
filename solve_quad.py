# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:24:26 2019

@author: cassi
"""

import numpy as np
import matplotlib.pyplot as plt
​
def least_square_solve(A, b):
    """to solve Ax = b with least square"""
    assert A.shape[0] == b.shape[0]
    assert A.ndim == 2
    assert b.ndim == 1
    return np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), b)
​
def reaction_fit(ener_r, ener_ts, ener_p, t=0.5):
    """iteratively solve the fitting problem with given energy
    """
    b_v = np.array([ener_p - ener_r, 0, 0, ener_ts - ener_r])
    A = generate_init(t)
    a, b, c = least_square_solve(A, b_v)
    answer = (- 3 * b - np.sqrt(9 * b ** 2 - 32 * a * c)) / (8 * a)
    while answer - t > 1e-5:
        t = answer
        A = generate_init(t)
        a, b, c = least_square_solve(A, b_v)
        answer = (- 3 * b - np.sqrt(9 * b ** 2 - 32 * a * c)) / (8 * a)
    return a, b, c
​
def quartic_function(a, b, c):
    """Quartic function model
    """
    def function(x):
        return a * x**4 + b * x**3 + c * x**2
    return function
​
def quartic_deriv(a, b, c):
    """Quartic function derivative model
    """
    def deriv(x):
        return 4 * a * x**3 + 3 * b * x**2 + 2 * c * x
    return deriv
​
​
def generate_init(t):
    A = np.array([[1, 1, 1],
                  [4, 3, 2],
                  [4 * t**3, 3 * t**2,2*t],
                  [t**4, t**3, t**2]])
    return A
​
def draw_graph(a, b, c):
    """draw graph with matplotlib
    """
    func = np.vectorize(quartic_function(a, b, c))
    plt.figure()
    x = np.arange(-0.1, 1.1, 0.01)
    y = func(x)
    plt.plot(x, y)
    plt.show()
​
def solve_and_draw(e_r, e_ts, e_p):
    """high level API for solve fitting problem and draw graph
​
    Arguments
    ---------
    e_r : float
        energy for reactant
    e_ts : float
        energy for transition state
    e_p : float
        energy for product
    """
    draw_graph(*reaction_fit(e_r, e_ts, e_p))