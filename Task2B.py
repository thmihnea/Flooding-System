"""

This file represents a demonstration program for the task
2B, where we have to show stations about a current tolerance level.

"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def run() -> None:
    # Initialize station list and tolerance.
    stations: list[MonitoringStation] = build_station_list()
    tolerance: float = 0.8

    # Update the water levels to retrieve current data.
    update_water_levels(stations)

    # Obtain the list of entries over accepted tolerance.
    over_tolerance: list[tuple[MonitoringStation, float]] = stations_level_over_threshold(
        stations,
        tolerance
    )

    # Print required output.
    for entry in over_tolerance:
        print(f"{entry[0].name}: {entry[1]}")

if __name__ == "__main__":
    run()