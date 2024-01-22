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
        if not isinstance(self.typical_range, tuple):
            return False
        if not isinstance(self.typical_range[0], float) or not isinstance(self.typical_range[1], float):
            return False
        return len(self.typical_range) == 2 and self.typical_range[0] < self.typical_range[1]
    
    def relative_water_level(self) -> float:
        if not self.typical_range_consistent() or self.latest_level is None:
            return None
        
        typical_low: float = self.typical_range[0]
        typical_high: float = self.typical_range[1]
        current_level: float = self.latest_level

        return (current_level - typical_low) / (typical_high - typical_low)

def inconsistent_typical_range_stations(stations: list[MonitoringStation]):
    return [station for station in stations if not station.typical_range_consistent() or station.typical_range is None]

        