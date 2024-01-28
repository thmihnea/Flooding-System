from .station import MonitoringStation
from .utils import sorted_by_key
from .datafetcher import fetch_just_levels, fetch_measure_levels
import datetime

def stations_level_over_threshold(stations: list[MonitoringStation], tol: float):
    """
    
    Given a list of MonitoringStation objects, return a
    list of tuples containing (station, level) pairs, 
    containing each station objects and its relative water level,
    if the certain station's level is above the tolerance.

    Parameters:

    stations:   The list of MonitoringStation objects
    tol:        The float that describes our accepted
                tolerance level

    Return:

    list[tuple[MonitoringStation, float]]:  the list of tuples
    
    """
    return [(station, station.relative_water_level()) 
            for station in stations if 
            station.latest_level != None and 
            station.relative_water_level() != None and 
            station.relative_water_level() > tol]


def stations_highest_rel_level(stations: list[MonitoringStation], 
                               N: int) -> list[MonitoringStation]:
    """

    Given a list of MonitoringStation objects, return the
    first N stations that are at the highest risk of flooding,
    i.e. the first N stations with the highest relative water level.

    Parameters:

    stations:   The list of all MonitoringStation objects provied
    N:          The number of elements we are interested in

    Return:

    The first N stations with the highest relative water level.

    """
    result: list[tuple[MonitoringStation, float]] = [(station, station.relative_water_level()) 
                                                     for station in stations 
                                                     if station.latest_level != None 
                                                     and station.relative_water_level() != None
                                                     and station.latest_level < 1000]
    return [entry[0] for entry in sorted_by_key(result, 1, True)][:N]

def flood_characterisation(station):


    '''
    
    Given a specific station, will return a 
    specific risk level based on that stations data. 

    Parameters:

    station: The MonitoringStation object provided

    Return:

    The risk level of that station
    
    '''

    # Sets up time.
    dt: int = 2
    dt = datetime.timedelta(days=dt)

    # Sets up risk characteristic. 
    characteristic = "none"

    # Classifies all stations with a current level within the typical range as low risk.
    if type(station.typical_range) == tuple and type(station.latest_level) == float: 
        if station.latest_level > station.typical_range[1]:
            characteristic = 'at risk'
        else:
            characteristic = 'low risk'

    # For all at risk stations, categorises them into diffferent risk levels based on their average level over the past 2 days. 
    if characteristic  == 'at risk':
        levels   = fetch_just_levels(station.measure_id, dt)
        if levels != []:
            try:
                average = sum(levels)/len(levels)
                if average/station.typical_range[1] < 1.2:
                    characteristic = 'medium risk'
                elif average/station.typical_range[1] < 2:
                    characteristic = 'high risk'
                else:
                    characteristic = 'severe risk'
            except:
                pass    
        else:
            characteristic = 'low risk'
    return characteristic