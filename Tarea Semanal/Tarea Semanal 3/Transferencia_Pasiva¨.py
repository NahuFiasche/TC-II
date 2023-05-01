#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:30:37 2023

@author: nahu
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

Tf = TransferFunction([1.96] , [1, 2.5, 3.14, 1.96])

bodePlot(Tf, fig_id=1)

pzmap(Tf, fig_id=2) 

GroupDelay(Tf, fig_id=3)