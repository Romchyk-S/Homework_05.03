# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

# function analysis available here: https://colab.research.google.com/drive/17fBCQSuBXJ8eQ2hFQspdOYY4Nhg6lnh2

def func_0():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$periodic, \ 2\pi_k$"
    
    title = "$2*sinx$"
    
    return x, 2*np.sin(x), label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$periodic, \ \pi_k$"
    
    title = "$sin(2x)$"
    
    return x, np.sin(2*x), label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$periodic, \ 2\pi_k$"
    
    title = "$sin(2x+\pi/4)$"
    
    return x, np.sin(2*x+np.pi/4), label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$periodic, \ 2\pi_k$"
    
    title = "$3*sinx+4*cosx$"
    
    return x, 3*np.sin(x)+4*np.cos(x), label, title

def func_4():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$periodic, \ \pi_k$"
    
    title = "$sin^2(x)$"
    
    return x, np.power(np.sin(x), 2), label, title

def func_5():
    
    label = "non-periodic"
    
    title = "$sin(x^2)$"
    
    x = np.arange(-10, 10, 0.1)
    
    return x, np.sin(x**2), label, title

def func_6():
    
    x = np.arange(0, 8*np.pi, 0.1)

    y = (np.piecewise(x, [(x < 2.49), ((x >= 2.49) & (x <= 2.51)), (x>2.51)],
                      [lambda x: np.tan(np.sqrt(x)), np.nan, lambda x: np.tan(np.sqrt(x))]))
    
    # не зміг зробити piecewise.
    
    label = "$non-periodic$"
    
    title = "$tan\sqrt{x}$"
    
    return x, y, label, title

def func_7():
    
    label = "$non-periodic$"
    
    title = "$\sqrt{tan x}$"
    
    x = np.arange(0, 8*np.pi, 0.1)
    
    return x, np.sqrt(np.tan(x)), label, title