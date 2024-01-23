'''

This submodule is designed to focus on plotting using Matplotlib

'''


import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation



def plot_water_levels(station, dates, levels):
    t = dates    
    lower_bound = station.typical_range[0]
    upper_bound = station.typical_range[1]
    plt.plot(t, levels)
    plt.axhline(lower_bound)
    plt.axhline(upper_bound)
    plt.xlabel('date')
    plt.xticks(rotation = 45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()