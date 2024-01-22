"""

This file represents a demonstration program for the task 1F.
This tests the method typical_range_consistent which provides a True/False
depending on whether the typical range is a valid input
This also tests the function inconsistent_typical_range_stations
which provides a list of all stations with inconsistent data regarding 
their typical range.

"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run() -> None:
    """
    This function demonstrates the functionality of this task.
    """

    # Builds station list.
    stations: list[MonitoringStation] = build_station_list()

    # Executes test function.
    inconsistent: list[str] = [station.name for station in inconsistent_typical_range_stations(stations)]

    # Prints required output.
    print(f"Inconsistent stations: {sorted(inconsistent)}")

if __name__ == "__main__":
    run()