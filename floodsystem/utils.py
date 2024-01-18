# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""

This module contains utility functions.

"""

from .station import MonitoringStation

def sorted_by_key(x: list[any], i: int, reverse = False) -> list[any]:
    """
    
    For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key = key, reverse = reverse)

def extract_station_names(data: list[MonitoringStation]) -> list[str]:
    """
    
    Given an input list of data representing
    MonitoringStation objects, return the names of all
    stations within that list, sorted in lexicographical order.

    Parameters:

    data:   a list of all the stations

    Return:

    list[str]
    
    """

    stations: list[str] = [station.name for station in data]
    stations.sort()
    return stations

def prettified_distance_data(list: list[tuple[MonitoringStation, float]]) -> list[tuple[str, str, float]]:
    """
    
    This utility function takes a list of tuples and extracts
    the required data for processing within this task, i.e.
    from the list of tuples containing MonitoringStation objects
    and the distances themselves, it extracts a list of tuples
    containing the name, town, and distance for each station
    relative to the specified point a-priori.

    Parameters:

    list:   a list of tuples containing each MonitoringStation
            object and its distance relative to a specified
            point

    Returns:

    list[tuple[str, str, float]]
    
    """
    results: list[tuple[str, str, float]] = []

    for entry in list:
        station: MonitoringStation = entry[0]
        distance: float = entry[1]

        result = (
            station.name,
            station.town,
            distance
        )

        results.append(result)

    return results
