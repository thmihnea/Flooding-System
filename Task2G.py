from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import retrieve_risky_stations, RiskLevel

def run() -> None:

    # Builds list of stations.
    stations: list[MonitoringStation] = build_station_list()

    # Updates water levels.
    update_water_levels(stations)

    # Create data container.
    table: dict[RiskLevel, list[str]] = retrieve_risky_stations(stations)

    # Print data.
    for entry in table:
        print(f"{entry.value[0]}: {table[entry]}")

if __name__ == "__main__":
    run()