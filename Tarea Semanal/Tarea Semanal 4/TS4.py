#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:40:35 2023

@author: nahu
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot, analyze_sys

den = np.polymul([1, 0.794], [1, 0.794, 0.794**2])

num = [1, 0, 0, 0]

Tf = TransferFunction(num,den)

bodePlot(Tf, fig_id=1)

pzmap(Tf, fig_id=2) 

GroupDelay(Tf, fig_id=3)