"""

This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from .station import MonitoringStation
import warnings
from haversine import haversine

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
    
    list[tuple[MonitoringStation, float]]

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



