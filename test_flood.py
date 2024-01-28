from floodsystem.flood import retrieve_risky_stations, RiskLevel
from floodsystem.station import MonitoringStation

def test_create_monitoring_station():

    a: MonitoringStation = MonitoringStation(
        "a", "a", "a", (0, 0), (0.0, 1.0), "a", "a"
    )
    a.latest_level = 1.5

    b: MonitoringStation = MonitoringStation(
        "b", "b", "b", (0, 0), (0.0, 1.0), "b", "b"
    )
    b.latest_level = 3.5

    result: dict[RiskLevel, list[str]] = retrieve_risky_stations([a, b])
    
    assert result[RiskLevel.SEVERE_RISK] == ["b"]
    assert result[RiskLevel.LOW_RISK] == ["a"]

