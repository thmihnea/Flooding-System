""" 

This file contains a series of unit tests designed specifically
for the geo module within this project.

"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_distance():
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
