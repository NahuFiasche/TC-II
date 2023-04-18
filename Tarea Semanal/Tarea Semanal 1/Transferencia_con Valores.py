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
    
    R1 = 1e3
    R2 = 1e3
    R3 = 1e3
    C1 = 1e-6
        
    Tf = TransferFunction( [1,-R2/(C1*R1*R3)], [1, 1/(C1*R3)] )
    
    plt.close('all')
    
    bodePlot(Tf, fig_id=1, filter_description = 'R1 = {} K\n R2 = {} K\n R3 = {} K\nC1 = {:.1f} uF'.format(R1/1000,R2/1000,R3/1000,C1/1e-6) )
    
    pzmap(Tf, fig_id=2, filter_description = 'R1 = {} K\n R2 = {} K\n R3 = {} K\nC1 = {:.1f} uF'.format(R1/1000,R2/1000,R3/1000,C1/1e-6)) 
    
    GroupDelay(Tf, fig_id=3, filter_description = 'R1 = {} K\n R2 = {} K\n R3 = {} K\nC1 = {:.1f} uF'.format(R1/1000,R2/1000,R3/1000,C1/1e-6))