
from floodsystem.plot import recent_flow_increase
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_just_levels
from floodsystem.flood import flood_characterisation

def run() -> None:

    # Builds list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # Updates water levels.
    update_water_levels(stations)

    # Sets up the degree of the polynomial.
    P = 4

    low_risk = []
    medium_risk = []
    high_risk = []
    severe_risk = []    
    for station in stations:
        risk = flood_characterisation(station)
        if risk == 'low risk':
            low_risk.append(station)
        if risk == 'medium risk':
                    medium_risk.append(station)
        if risk == 'high risk':
                    high_risk.append(station)
        if risk == 'severe risk':
                    severe_risk.append(station)
    print(severe_risk)

if __name__ == "__main__":
    run()