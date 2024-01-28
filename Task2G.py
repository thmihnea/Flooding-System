from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import flood_characterisation

def run() -> None:

    # Builds list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # Updates water levels.
    update_water_levels(stations)

    # Creates empty lists of towns.
    low_risk_towns = []   
    medium_risk_towns = []
    high_risk_towns = []
    severe_risk_towns = []

    # Organises station's town into a category based on their risk characteristic.
    for station in stations:
        risk = flood_characterisation(station)
        if risk == 'low risk' and station.town not in low_risk_towns:
            low_risk_towns.append(station.town)
        if risk == 'medium risk' and station.town not in medium_risk_towns:
            medium_risk_towns.append(station.town)
        if risk == 'high risk' and station.town not in high_risk_towns:
            high_risk_towns.append(station.town)
        if risk == 'severe risk' and station.town not in severe_risk_towns:
            severe_risk_towns.append(station.town)

    # Prints the result. 
    print("Towns at severe risk are:", severe_risk_towns)
    print("Towns at high risk are:", high_risk_towns)
    print("Towns at medium risk are:", medium_risk_towns)
    print("Towns at low risk are:", low_risk_towns)



if __name__ == "__main__":
    run()