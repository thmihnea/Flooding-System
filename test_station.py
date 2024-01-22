# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_consistent() -> None:
    
    # Construct fictitious data.
    a = MonitoringStation(
        "a", "a", "a", (0, 0), (0.0, 1.0), "x", "a"
    )
    b = MonitoringStation(
        "a", "a", "a", (0, 0), (1.0, 0.0), "x", "a"
    )

    # Assertion statements.
    assert a.typical_range_consistent() == True and b.typical_range_consistent() == False
    assert inconsistent_typical_range_stations([a, b]) == [b]
