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
R2_lista = [1, 2, 3]
R1 = 2




plt.close('all')

for i in range(len(R2_lista)):
    
    Tf = TransferFunction( [1,-R2_lista[i]/R1], [1, 1] )

    bodePlot(Tf, fig_id=1, filter_description = 'R2/R1 = {}'.format(R2_lista[i]/R1) )

    pzmap(Tf, fig_id=2, filter_description = 'R2/R1 = {}'.format(R2_lista[i]/R1)) #S plane pole/zero plot

    GroupDelay(Tf, fig_id=3, filter_description = 'R2/R1 = {}'.format(R2_lista[i]/R1))