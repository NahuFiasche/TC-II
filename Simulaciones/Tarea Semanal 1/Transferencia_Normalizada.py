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

# Asigno valores a R2 y R1 (La consigna no aclara con que valores simular)
R2 = 1
R1 = 2

Tf = TransferFunction( [1,-R2/R1], [1, 1] )


plt.close('all')

bodePlot(Tf, fig_id=1, filter_description = 'R1={}K, R2={}K'.format(R1,R2) )

pzmap(Tf, fig_id=2, filter_description = 'R1={}K, R2={}K'.format(R1,R2)) #S plane pole/zero plot

GroupDelay(Tf, fig_id=3, filter_description = 'R1={}K, R2={}K'.format(R1,R2))