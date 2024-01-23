import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation

def plot_water_levels(station: list[MonitoringStation], dates: list, levels: list):   

    '''

    Given a MonitoringStation object, return 
    a MatPlotLib plot showing the variation of the water 
    level at the station over the given time 
    period.

    Parameters:

    station: The MonitoringStation object
    dates: The selection of dates/times from which the data is taken
    levels: The historical water levels across the time period

    '''

    lower_bound = station.typical_range[0]
    upper_bound = station.typical_range[1]
    plt.plot(dates, levels)
    plt.axhline(lower_bound)
    plt.axhline(upper_bound)
    plt.xlabel('date')
    plt.xticks(rotation = 45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()