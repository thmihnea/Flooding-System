from .station import MonitoringStation

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