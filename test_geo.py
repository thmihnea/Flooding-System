""" 

This file contains a series of unit tests designed specifically
for the geo.py module within this project.

"""

from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation

def test_distance() -> None:
    """
    This function asserts that the distance between a
    list of stations is calculated correctly.
    """

    # Construct fictitious stations.
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "a", "a"
    )
    b = MonitoringStation(
        "b", "b", "b", (1, 0), (0, 0), "b", "b"
    )
    c = MonitoringStation(
        "c", "c", "c", (2, 0), (0, 0), "c", "c"
    )

    # This is the actual distance to the point (2, 0) as
    # calculated using the haversine formula.
    distance_actual = [
        (c, 0.0),
        (b, 111.1950802335329),
        (a, 222.3901604670658)
    ]

    # This is the distance computed using our function.
    distance_function = stations_by_distance([a, b, c], (2, 0))

    # Assertion statement.
    assert distance_actual == distance_function

def test_within_radius() -> None:
    """
    This function asserts that a fictive set of
    MonitoringStation objects are within a certain radius
    from a point.
    """

    # Construct fictitious data.
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "a", "a"
    )
    b = MonitoringStation(
        "b", "b", "b", (1, 0), (0, 0), "b", "b"
    )
    point = (1.5, 0.0)

    # Setup actual result and result from function.
    within_radius_actual = [b]
    within_radius = stations_within_radius([a, b], point, 100.0)

    # Assertion statement.
    assert within_radius_actual == within_radius

def test_rivers_with_station() -> None:
    """
    This function tests whether or not the geo.py #rivers_with_station
    function works normally.
    """

    # Construct fictitious data.
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "x", "a"
    )
    b = MonitoringStation(
        "b", "b", "b", (1, 0), (0, 0), "x", "b"
    )
    c = MonitoringStation(
        "c", "c", "c", (1, 1), (0, 0), "y", "c"
    )

    # Attribute real data with function-calculated data.
    different_rivers: set[str] = set(["x", "y"])
    different_rivers_actual: set[str] = rivers_with_station([a, b, c])

    # Assertion statement.
    assert different_rivers == different_rivers_actual

def test_stations_by_river() -> None:
    """
    This function tests whether or not the #stations_by_river
    function from the geo.py module functions normally.
    """

    # Construct fictitious data.
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "x", "a"
    )
    b = MonitoringStation(
        "b", "b", "b", (1, 0), (0, 0), "x", "b"
    )
    c = MonitoringStation(
        "c", "c", "c", (1, 1), (0, 0), "y", "c"
    )

    # Construct both hashtables.
    table: dict[str, list[MonitoringStation]] = {
        "x": [a, b],
        "y": [c]
    }
    actual_table: dict[str, list[MonitoringStation]] = stations_by_river([a, b, c])

    # Assertion statement.
    assert table == actual_table

def test_rivers_by_station_number() -> None:
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "x", "a"
    )
    b = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "x", "a"
    )
    c = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "y", "a"
    )
    d = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "z", "a"
    )
    e = MonitoringStation(
        "a", "a", "a", (0, 0), (0, 0), "y", "a"
    )

    first_result = rivers_by_station_number([a, b, c, d], 2)
    assert first_result == [("x", 2), ("y", 1), ("z", 1)]

    second_result = rivers_by_station_number([a, b, c, d, e], 2)
    assert second_result == [("x", 2), ("y", 2), ("z", 1)]

    third_result = rivers_by_station_number([a, b], 3)
    assert third_result == [("x", 2)]

    fourth_result = rivers_by_station_number([a, b, c], 4)
    assert fourth_result == [("x", 2), ("y", 1)]

if __name__ == "__main__":
    test_rivers_by_station_number()