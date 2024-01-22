"""

This file represents a demonstration for the 
Task 1C - it utilizes the #stations_within_radius
function from the geo.py module and builds a list
within 10km from Cambridge City Centre.

"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import extract_station_names

def run() -> None:
    """
    This function demonstrates the functionality of this task.
    """

    # Build the station list cache and setup the
    # Cambridge City Centre geolocation.
    stations: list[MonitoringStation] = build_station_list()
    point: tuple[float] = (
        52.2053,
        0.1218
    )

    # Extract all stations within the given radius.
    within_radius: list[MonitoringStation] = stations_within_radius(
        stations,
        point,
        10.0
    )

    # Print the output and require that it is equal to the test case.
    required_output: list[str] = ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
                       'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
                       'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    extracted_data: list[str] = extract_station_names(within_radius)
    assert extracted_data == required_output
    print(extracted_data)

if __name__ == "__main__":
    run()

    