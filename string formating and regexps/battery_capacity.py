# Task is to return the value of left battery capacity parsed from given string (let's assume it is some shell command's result).

# Current level should be calculated as CurrentCapacity / MaxCapacity in percents. The resulting value should be like the following example:

# 61.41%

# There are two ways:

# Parse from LegacyBatteryInfo block - this is super easy. If you are beginner - try to get needed info from this line.
# Parse from MaxCapacity/CurrentCapacity attributes - more complex task for more experienced programmers. If you want challenge - try to get information without using data from LegacyBatteryInfo block.
# The result of the function should be in the form of the string: "XX.YY%" where XX.YY is the float number of percents with 2 digits after dot.

import re
data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''

def get_battery_level(data):
    max_cap=re.search(r"\bMaxCapacity\D+(\d+)",data).group(1)
    cur_cap=re.search(r"\bCurrentCapacity\D+(\d+)",data).group(1)
    return "{:.2%}".format(int(cur_cap)/int(max_cap))

print(get_battery_level(data))
