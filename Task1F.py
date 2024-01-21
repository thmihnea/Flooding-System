'''

This file represents a demonstration program for the task 1F.
This tests the method typical_range_consistent which provides a True/False
depending on whether the typical range is a valid input
This also tests the function inconsistent_typical_range_stations
which provides a list of all stations with inconsistent data regarding 
their typical range.
'''

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    '''
    
    This function demonstrates the functionality of this task.
    
    '''
    #builds station list
    stations: list[MonitoringStation] = build_station_list()

    #executes test function
    inconsistent_station_list = inconsistent_typical_range_stations(stations)

    #prints output
    print("The list of inconsistent stations is:", sorted(inconsistent_station_list))

if __name__ == "__main__":
    run()