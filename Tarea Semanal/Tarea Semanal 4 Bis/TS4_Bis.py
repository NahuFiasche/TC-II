# M�dulos externos

import sympy as sp
from sympy.abc import s
# Ahora importamos las funciones de PyTC2

from pytc2.sistemas_lineales import analyze_sys, parametrize_sos, pretty_print_lti, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS
from pytc2.general import print_latex, print_subtitle
import numpy as np
import scipy.signal as sig
from IPython.display import display, Markdown

# Librer�as externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot, analyze_sys


# coeficientes de la transferencia Pasabajos Prototipo
Tlp_num = np.array([3.16])
den_aux = np.polymul([1, 1], [1, 1, 1])
Tlp_den = np.array(den_aux)

# Q de la transformaci�n
Q_bp = 20/9

# Transformaci�n y Visualizaci�n de Pasabajos Prototipo a Pasabanda Requerido
num_pbanda, den_pbanda = sig.lp2bp(Tlp_num, Tlp_den, bw = 1/Q_bp)

display(Markdown('### Filtro pasabanda de Orden 6 normalizado' ))

pretty_print_lti(num_pbanda, den_pbanda)

#Factorizaci�n y Visualizaci�n
sos_Tf = tf2sos_analog(num_pbanda, den_pbanda)

display(Markdown('### Filtro pasabanda de Orden 6 Factorizado y Normalizado' ))

pretty_print_SOS(sos_Tf)

# Simulaci�n Num�rica

display(Markdown('### Simulaci�n Num�rica' ))

Tf = TransferFunction(num_pbanda,den_pbanda)

analyze_sys( sos_Tf, 'TS4 Bis' )
