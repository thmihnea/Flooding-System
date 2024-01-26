from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import is_invalid_data
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
    dt = datetime.timedelta(days = dt)

    # Sets up the degree of the polynomial.
    valid_stations: list[MonitoringStation] = []
    invalid_stations: list[MonitoringStation] = []

    fetch_more: bool = True
    M: int = N

    # Fetch the first N stations that have valid data
    # and are of highest relative level.
    while fetch_more is True:
        fetch_more = False
        N_stations: list[MonitoringStation] = stations_highest_rel_level(stations, M)

        for station in N_stations:
            if station not in valid_stations and station not in invalid_stations:
                dates, levels = fetch_measure_levels(station.measure_id, dt)
                if is_invalid_data(dates, levels):
                    invalid_stations.append(station)
                    fetch_more = True
                else:
                    valid_stations.append(station)

        M = N + len(invalid_stations)
                
    P: int = 4

    # Plot everything.
    for station in valid_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        
        plot_water_level_with_fit(station, dates, levels, P)

if __name__ == "__main__":
    run()