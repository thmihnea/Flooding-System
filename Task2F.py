from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run() -> None:
    
    # Builds list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # Determines number of graphs generated.
    N: int = 5

    # Updates water levels.
    update_water_levels(stations)

    # Sets up time.
    dt: int = 2
    dt = datetime.timedelta(days=dt)

    # Sets up the degree of the polynomial.
    valid_stations = []
    invalid_stations = []
    n = 1
    M = N
    while n == 1:
        n = 0
        N_stations: list[MonitoringStation] = stations_highest_rel_level(stations, M)
        for station in N_stations:
            if station not in valid_stations and station not in invalid_stations:
                dates, levels = fetch_measure_levels(station.measure_id, dt)
                if dates == []:
                    invalid_stations.append(station)
                    n = 1
                else:
                    valid_stations.append(station)
        M = N + len(invalid_stations)
                
    P = 4

    for station in valid_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        
        plot_water_level_with_fit(station, dates, levels, P)




if __name__ == "__main__":
    run()