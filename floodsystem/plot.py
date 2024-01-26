import matplotlib.pyplot as plt
from .station import MonitoringStation
from .analysis import polyfit
import matplotlib

def plot_water_levels(station: list[MonitoringStation], dates: list, levels: list) -> None:   

    """

    Given a MonitoringStation object, return 
    a MatPlotLib plot showing the variation of the water 
    level at the station over the given time 
    period.

    Parameters:

    station: The MonitoringStation object
    dates: The selection of dates/times from which the data is taken
    levels: The historical water levels across the time period

    """

    # Retrieve lower and upper bound for typical range.
    lower_bound: float = station.typical_range[0]
    upper_bound: float = station.typical_range[1]

    # Prepare plotting data.
    plt.plot(dates, levels)
    plt.axhline(lower_bound)
    plt.axhline(upper_bound)
    plt.xlabel('date')
    plt.xticks(rotation = 45)
    plt.title(station.name)

    # Plot.
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

    # Retrieve lower and upper bound for typical range.
    lower_bound: float = station.typical_range[0]
    upper_bound: float = station.typical_range[1]
    # Plot raw data.
    plt.plot(dates, levels)
    plt.axhline(lower_bound)
    plt.axhline(upper_bound)
    plt.xlabel('date')
    plt.xticks(rotation = 45)
    plt.title(station.name)

    poly, d0 = polyfit(dates, levels, p)
    dates  = matplotlib.dates.date2num(dates)
    plt.plot(dates, poly(dates - d0))
    # Plot.
    plt.tight_layout()
    plt.show()