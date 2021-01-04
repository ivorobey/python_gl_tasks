# There is some small building (6 floors) with a single elevator (what a shame!). It was working fine in the morning - but at noon it just stopped at the ground floor. You are to calculate few things:

# On what floor the max number of ppl left - and how many?
# Total number of ppl in the building.
# You are given with ordered list of elevator records. Each record is mapping with floor and the number of ppl that were transferred to that floor.

# For example, the very first entry is:

# {2: 3, 4: 5, 5: 2, 6: 5}
# This means:

# 1st and 3rd - nobody arrived yet!
# 2nd floor - 3 ppl
# 4th floor - 5 ppl
# 5th floor - 2 ppl
# 6nd floor - 5 ppl
# This was simple.

# The next record is this:

# {1: 5, 2: -1, 4: -2, 5: 1, 6: -3}
# This means that 5 ppl went to the first floor, 1 left from the second (now 2nd floor has only 2 ppl as before it was 3, now -1). 2 ppl went out from 4th, +1 to 5th 3 left from sixth.

# What is left is to process ordered sequence of such records and determine needed answers.

# The function will access predefined variable elevator_records which is the list of dict shown before. The function should return return a tuple with 3 int numbers:

# The floor with max ppl left
# Number of ppl on the floor with max ppl left
# Total number of ppl left in the building

elevator_records = [
    {2: 3, 4: 5, 5: 2, 6: 5},
    {1: 5, 2: -1, 4: -2, 5: 1, 6: -3},
    {1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 6: 2},
    {1: -1, 2: -1, 3: 1, 4: 1, 5: 1, 6: 3},
    {1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 6: 1},
    {1: -2, 2: 3, 3: 1, 4: 1, 5: 1, 6: -1},
]


def elevator(elevator_records):
    status = {}
    for rec in elevator_records:
        for floor, ppl in rec.items():
            status[floor] = status.setdefault(floor, 0)+ppl

    max_ppl = max(status.values())
    total_ppl = sum(status.values())
    for k, v, in status.items():
        if v == max_ppl:
            max_ppl_floor = k
        break
    return (max_ppl_floor, max_ppl, total_ppl)


print(elevator(elevator_records))
