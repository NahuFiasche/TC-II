from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS

from pytc2.general import print_subtitle

# Declaración de Variables

n = 3 #Orden del Filtro
alpha_max = 0.5 #Máxima atenuación en la Banda de paso

# Cálculo de la Transferencia

[z, p, k] = sig.cheb1ap(n, alpha_max) #Obtención de los polos, ceros y ganancia de la transferencia

[num, den] = sig.zpk2tf(z, p, k) #Calculo del numerador y denominador a partir de los polos y ceros

Hlp = TransferFunction(num, den) #Transferencia calculada

this_sos = tf2sos_analog(num, den) #Factorización de la transferencia en secciones de Orden 2

# Ploteo

pretty_print_SOS(this_sos, mode='omegayq')
print("z = ", z, "\n", "p = ", p, "\n", "k =", k)
analyze_sys(Hlp, "Chebyshev")
  
