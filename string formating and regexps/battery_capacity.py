# import re

# data = '''
#             "SuperMaxCapacity" =0
#            "MaxCapacity" = 4540
#            "CurrentCapacity" = 2897
#            "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
#            "DesignCapacity" = 6700
# '''
# def get_battery_level(data): 

#        max = int(re.search('"MaxCapacity" = (\d+)', data).group(1))
#        cur = int(re.search('"CurrentCapacity" = (\d+)', data).group(1))
#        result = float(float(cur) * 100 / float(max))
#        return "{:.2f}%".format(result)

# print(get_battery_level(data))

import re
data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''

def get_battery_level(data):
    regm=r'\bMaxCapacity....[0-9]+'
    # regc=0
    maxcap=re.findall(regm,data)
    for i in maxcap:
        print(i.split(','))
    # curcap=re.findall(regc, data)

print(get_battery_level(data))
