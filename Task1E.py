'''

description

'''

from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    '''
    
    This function demonstrates the functionality of this task.
    
    '''

    N = 9
    stations: list[MonitoringStation] = build_station_list()
    first_N_rivers = rivers_by_station_number(stations, N)
    

    print("test1")
    print("These are the" + (len(first_N_rivers)+1) + "rivers with the most number of stations:" + first_N_rivers  )

if __name__ == "__main__":
    run()
    print('test3')

run()
print('test2')