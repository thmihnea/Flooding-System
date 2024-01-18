# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""

This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key
from station import MonitoringStation
import stationdata
import haversine

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

    station_list: list[tuple[MonitoringStation, float]] = []

    for station in stations:
        station_location = station.coord
        distance = haversine.haversine(station_location, p)
        station_list.append(
            (station.name, distance)
        )

    station_list = sorted_by_key(station_list, 1)



