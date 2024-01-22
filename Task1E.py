"""

This file represents a demonstration program for the task 1E.
This tests the function rivers_by_station_number from geo.py

"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run() -> None:
    """
    This function demonstrates the functionality of this task.
    """

    # N denotes the number of cases taken from the list of rivers ranked by number of stations.
    N = 9

    # This creates the list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # This is the function in action.
    first_N_rivers: list[tuple[str, int]] = rivers_by_station_number(stations, N)

    # This prints the result of the function.
    print(f"The first {N} rivers when ranked by the number of stations are: {first_N_rivers}.")

if __name__ == "__main__":
    run()