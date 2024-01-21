"""

This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from .station import MonitoringStation
import warnings
from haversine import haversine
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations:  list[MonitoringStation],
                         p:         tuple[float]) -> list[tuple[MonitoringStation, float]]:
    """
    
    Given a list of stations and a coordinate, return
    a list of tuples that contains the station itself and
    the distance between the station and the said point.
    Note that this list is sorted by the distance.

    Parameters:

    stations:   a list of MonitoringStation objects
    p:          the location from which we calculate the
                distance given as a tuple of floats

    Returns:
    
    list[tuple[MonitoringStation, float]]:  a list of tuples containing
                                            each station and the distance

    """

    if not isinstance(stations, list):
        raise RuntimeError("The specified stations parameter is not of type list[MonitoringStation]!")
    
    if not isinstance(p, tuple):
        raise RuntimeError("The specified geolocation parameter is not of type tuple[float]!")
    
    if len(stations) == 0:
        warnings.warn("The program provided an empty station list as a parameter inside geo.py!")
        return []

    station_list: list[tuple[MonitoringStation, float]] = []

    for station in stations:
        station_location = station.coord
        distance = haversine(station_location, p)
        station_list.append(
            (station, distance)
        )

    station_list = sorted_by_key(station_list, 1)
    return station_list

def stations_within_radius(stations: list[MonitoringStation],
                           centre: tuple[float],
                           r: float) -> list[MonitoringStation]:
    
    """
    
    Given a list of stations, return all stations
    that are within the specified radius (in kilometres)
    from the centre point (as a geolocation tuple of latitude
    and longitude).

    Parameters:

    stations:   a list containing the stations
    centre:     the tuple containing the location
                of the centre point
    r:          the radius within the search is
                performed

    Return:

    list[MonitoringStation]:    a list containing each MonitoringStation
    
    """

    if not isinstance(stations, list):
        raise RuntimeError("The given object is not of type list[MonitoringStation]!")
    
    if not isinstance(centre, tuple):
        raise RuntimeError("The specified centre is not of type tuple[float]!")
    
    if not isinstance(r, float):
        raise RuntimeError("The specified radius is not of type float!")
    
    sorted_stations: list[tuple[MonitoringStation, float]] = stations_by_distance(
        stations,
        centre
    )

    result: list[MonitoringStation] = []

    for entry in sorted_stations:
        if entry[1] > r:
            break
        result.append(entry[0])

    return result

def rivers_with_station(stations: list[MonitoringStation]) -> set[str]:
    """
    
    Given a list of MonitoringStation objects, return a set
    of strings containing the unique rivers that belong to
    at least a station. 
    Note that since this is a set, it will contain no duplicates.

    Parameters:

    stations:   the list containing all the station objects

    Return:

    set[str]:   a set containing each individual river

    """

    if not isinstance(stations, list):
        raise RuntimeError("The given object is not of type list[MonitoringStation]!")
    
    rivers: set[str] = set()

    for station in stations:
        rivers.add(station.river)

    return rivers

def stations_by_river(stations: list[MonitoringStation]) -> dict[str, list[MonitoringStation]]:
    """
    
    Given a list of MonitoringStation objects, this
    function returns a dictionary containing Key-Value
    pairs consisting of rivers (the key) and a list
    of stations (the value). This represents a mapping
    between a river and the stations that cross it.

    Parameters:

    stations:   the aforementioned list of objects

    Return:

    dict[str, list[MonitoringStation]]: a dictionary of river names
                                        mapped to their stations
    
    """

    if not isinstance(stations, list):
        raise RuntimeError("The given object is not of type list[MonitoringStation]!")
    
    table: dict[str, list[MonitoringStation]] = dict()
    
    for station in stations:
        river: str = station.river

        if river not in table:
            table[river] = [station]
        else:
            table[river].append(station)

    return table

def rivers_by_station_number(stations: list[MonitoringStation], N: float) -> list[tuple]:
    '''
    
    Gives a list of tuples, with the first term of the tuple being the river name
    and the second term in the tuple being the number of stations on that river. 

    Parameters:
    
    stations: a list of monitoringstation objects

    N: the number of rivers from the top of the list which are given

    Return:

    the sorted list of tuples
    
    '''
    river_table: dict[str, list[MonitoringStation]] = stations_by_river(stations)
    stations: list[MonitoringStation] = build_station_list()
    rivers: list[str] = rivers_with_station(stations)
    list_of_rivers_and_number_of_stations = []
    for river in rivers:
        station_list: list[str] = [station.name for station in river_table[river]]
        list_of_rivers_and_number_of_stations.append((river, int(len(station_list))))
    sorted_list = sorted(list_of_rivers_and_number_of_stations, key = lambda N: N[1], reverse = True)
    n = 0
    while n == 0:
        if sorted_list[N-1][1] == sorted_list[N][1]:
            N +=1
        else:
            n = 1
    first_N_sorted = []
    for i in range(N):
        first_N_sorted.append(sorted_list[i])
    return(first_N_sorted)