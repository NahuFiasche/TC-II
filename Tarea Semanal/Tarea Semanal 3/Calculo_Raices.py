#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:48:47 2023

@author: nahu
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

E = 0.5088
a = 1
b = 2*E**(-1/3)
c = 2*E**(-2/3)
d = 1/E

raices = np.roots([a,b,c,d])