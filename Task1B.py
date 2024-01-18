"""

This file represents a demonstration program for the
Task 1B - this should use the geo.py function and
correctly sort a list of MonitoringStation based on their
distances from a geographical location point.

"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import haversine

def extract_result(list: list[tuple[MonitoringStation, float]]) -> list[tuple[str, str, float]]:
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

if __name__ == "__main__":

    # Gather all stations from the cache and set up the testing point.
    stations: list[MonitoringStation] = build_station_list()
    point: tuple[float] = (
        52.2053,
        0.1218
    )

    # Compute all distances.
    distances: list[tuple[MonitoringStation, float]] = stations_by_distance(
        stations,
        point
    )

    # Print the top ten closest stations after extracting
    # the relevant data with the utility function.
    closest: list[tuple[str, str, float]] = extract_result(distances[:10])
    furthest: list[tuple[str, str, float]] = extract_result(distances[-10:])

    print(f"The closest stations are: {closest}. \n")
    print(f"The furthest stations are: {furthest}. \n")

    print(haversine.haversine((0, 0), (2, 0)))


