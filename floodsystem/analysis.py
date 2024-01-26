import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    
    dates_formatted = matplotlib.dates.date2num(dates)
    
    shift_factor = dates_formatted[0]
    shifted_dates = []
    for i in range(len(dates_formatted)):
        shifted_dates.append(dates_formatted[i] - dates_formatted[0]) 
    
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(shifted_dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return (poly, shift_factor)
