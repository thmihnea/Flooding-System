"""

This file represents a demonstration program for
the Task 1D - this tests the geo.py functions that
interact with the stations by extracting river-related
data.

"""

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

if __name__ == "__main__":
    
    # Obtain the list of all available stations and
    # prepare all data.
    stations: list[MonitoringStation] = build_station_list()
    river_table: dict[str, list[MonitoringStation]] = stations_by_river(stations)
    rivers: list[str] = rivers_with_station(stations)
    
    # Retrieve all valid rivers.
    valid_rivers = list(rivers)
    valid_rivers.sort()

    # Print required output.
    print(f"There are {len(valid_rivers)} rivers that have at least one station. The first ten are: {valid_rivers[:10]}.\n")

    rivers = ["River Aire", "River Cam", "River Thames"]
    for river in rivers:
        station_list: list[str] = [station.name for station in river_table[river]]
        station_list.sort()
        print(f"Stations located on {river} are: {station_list}.\n")



    