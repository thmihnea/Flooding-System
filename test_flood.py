from floodsystem.flood import flood_characterisation
from floodsystem.station import MonitoringStation

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

    #assign latest_level value for low risk
    s.latest_level = 2.0
    assert flood_characterisation(s) == 'low risk'


