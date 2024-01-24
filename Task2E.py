"""

This file represents a demonstration program for the task 2E.
We are testing that the function #plot_water_levels
works properly by showing the first N (in this case, 5) stations
with the highest relative water level plotted onto graphs showing their 
water level over the specific time period (in this case 10 days).

"""


from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime


def run() -> None:

    # Builds list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # Determines number of graphs generated.
    N: int = 5

    # Updates water levels.
    update_water_levels(stations)

    # Sets up time.
    dt: int = 10
    dt = datetime.timedelta(days=dt)

    # Determines N stations with the highest relative water level.
    N_stations: list[MonitoringStation] = stations_highest_rel_level(stations, N)

    # Plots the N stations water level over the given time period.
    for station in N_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    run()