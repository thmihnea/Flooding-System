"""

This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """ 
    This class represents a river level monitoring station.
    """

    def __init__(self, station_id: str, measure_id: str, label: str, coord: tuple[float], 
                 typical_range: tuple[float], river: str, town: str):
        """ Create a monitoring station """

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        check = 0
        if type(self.typical_range) == tuple:
            if len(self.typical_range) == 2:   
                if self.typical_range[0] < self.typical_range[1]:
                    check = 1
                    return True
        if check == 0:
            return False

from .stationdata import build_station_list

def inconsistent_typical_range_stations(stations):
    inconsistent_stations = []
    stations: list[MonitoringStation] = build_station_list()
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_stations.append(station.name)
    return inconsistent_stations
        