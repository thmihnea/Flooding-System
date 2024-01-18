"""

This file represents a demonstration program for the
Task 1B - this should use the geo.py function and
correctly sort a list of MonitoringStation based on their
distances from a geographical location point.

"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import prettified_distance_data
import haversine

def run():
    """
    This function demonstrates the functionality of this task.
    """

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
    closest: list[tuple[str, str, float]] = prettified_distance_data(distances[:10])
    furthest: list[tuple[str, str, float]] = prettified_distance_data(distances[-10:])

    print(f"The closest stations are: {closest}. \n")
    print(f"The furthest stations are: {furthest}. \n")

if __name__ == "__main__":
    run()


