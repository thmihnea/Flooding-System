import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """
    
    Given the dates and the water levels for a certain
    station object, return a p-degree least-squares 
    best-fit approximation for the polynomial describing the 
    level = level(date) dependency.

    Parameters:

    dates:      The dates for each level
    levels:     The water levels registered
    p:          The degree of the polynomial

    Returns:

    A tuple containing the polyfit representation and the
    shifting factor.
    
    """
    
    dates_formatted = matplotlib.dates.date2num(dates)
    
    shift_factor = dates_formatted[0]
    shifted_dates = []
    for i in range(len(dates_formatted)):
        shifted_dates.append(dates_formatted[i] - dates_formatted[0]) 
    
    # Find coefficients of best-fit polynomial f(x) of degree p.
    p_coeff = np.polyfit(shifted_dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # i.e. - poly(0.3).
    poly = np.poly1d(p_coeff)
    return (poly, shift_factor)
