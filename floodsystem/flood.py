from .station import MonitoringStation
from .utils import sorted_by_key

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
                                                     and station.relative_water_level() != None]
    return [entry[0] for entry in sorted_by_key(result, 1, True)][:N]