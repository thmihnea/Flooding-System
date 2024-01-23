


from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime


def run() -> None:
    """
    This function demonstrates the functionality of this task.
    """

    stations: list[MonitoringStation] = build_station_list()

    N: int = 5

    update_water_levels(stations)
    dt: int = 10
    dt=datetime.timedelta(days=dt)

    N_stations = stations_highest_rel_level(stations, N)
    for station in N_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    run()