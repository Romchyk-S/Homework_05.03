# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

def func_0():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "periodic or not, period"
    
    title = "$2*sinx$"
    
    return x, 2*np.sin(x), label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "periodic or not, period"
    
    title = "sin(2x)$"
    
    return x, np.sin(2*x), label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)
    
    # x = np.setdiff1d(x, [0])
    
    # y = np.piecewise(x, [(x < -0.01), ((x >= -0.01) & (x <= 0.01)), (x > 0.01)],
    #                 [lambda x: np.abs(x)/x, np.nan, lambda x: np.abs(x)/x])
    
    label = "periodic or not, period"
    
    title = "$sin(2x+\pi/4)$"
    
    return x, np.sin(2*x+np.pi/4), label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "periodic or not, period"
    
    # y = np.piecewise(x, [(x < -1.01), (x >= -1.01) & (x <= 1.01), (x > 1.01)],
    #                 [lambda x: np.log2(x**2-1), np.nan, lambda x: np.log2(x**2-1)])
    
    title = "$3*sinx+4*cosx$"
    
    return x, 3*np.sin(x)+4*np.cos(x), label, title

def func_4():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "periodic or not, period"
    
    title = "$sin^2(x)$"
    
    return x, np.power(np.sin(x), 2), label, title

def func_5():
    
    label = "periodic or not, period"
    
    title = "$sin(x^2)$"
    
    x = np.arange(-10, 10, 0.1)
    
    return x, np.sin(x**2), label, title

def func_6():
    
    x = np.arange(-10, 10, 0.1)
    
    # x = np.setdiff1d(x, [-2, 2])
    
    label = "periodic or not, period"
    
    title = "$tan\sqrt{x}$"
    
    # y = np.piecewise(x, [(x < -2.01), (x >= -2.01) & (x <= -1.99), (x>-1.99) & (x < 1.99), (x>=1.99) & (x<=2.01), (x > 2.01)],
    #                 [lambda x: x**3/(x**2-4), np.nan, lambda x: x**3/(x**2-4),np.nan,  lambda x: x**3/(x**2-4)])
    
    
    return x, np.tan(np.sqrt(x)), label, title

def func_7():
    
    label = "periodic or not, period"
    
    title = "$\sqrt{tan x}$"
    
    x = np.arange(-10, 10, 0.1)
    
    return x, np.sqrt(np.tan(x)), label, title

# def func_8():
    
#     x = np.arange(-10, 10, 0.1)
    
#     label = "$x \in \Re$"
    
#     title = "$2^x-2^{-x}$"
    
#     return x, 2**x-2**(-x), label, title