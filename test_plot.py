from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

#test to test plot_water_levels function
def test_plot():

    #generates list of stations
    stations: list[MonitoringStation] = build_station_list()
    test_station = 'Bourton Dickler'
    n = 0
    for station in stations:
        if test_station == station.name:
            plot_water_levels(station, 0, 0)
            n = 1
    assert n == 1