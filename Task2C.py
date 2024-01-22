"""

This file represents a demonstration program for the task 2C.
We are testing that the function #stations_highest_rel_level
works properly by showing the first N (in this case, 10) stations
with the highest relative water level.

"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run() -> None:
    # Initialize station list and amount we want to get.
    stations: list[MonitoringStation] = build_station_list()
    N: int = 10

    # Retrieve latest real-time data.
    update_water_levels(stations)

    # Build the list of highest relative level stations.
    highest_level: list[MonitoringStation] = stations_highest_rel_level(
        stations,
        N
    )

    # Print output.
    for station in highest_level:
        print(f"{station.name}: {station.relative_water_level()}")

if __name__ == "__main__":
    run()