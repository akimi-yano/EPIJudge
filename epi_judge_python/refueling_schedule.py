import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.

        #  A    B    C    D    E    F    G
        # [50,  20,  5,   30,  25,  10,  10] - gas - gallon
        # [900, 600, 200, 400, 600, 200, 100] - distance - miles
        
        #  10+50 15+20 5+5 0+30 10+25 5+10 5+10
        #  60    35    10 ok30   35    15   15 
        
            # 20x = 400
            # x = 20
            # 20x = 600
            # x = 30
            # 20x = 200
            # x = 10
            # 20x = 100
            # x = 5
            # 20x = 900
            # 2x = 90
            # x = 45
            # 20x = 600
            # x = 30
            # 20x = 200
            # x = 10
# * 20 miles per gallon *

# This solution works - need more optimization
# def find_ample_city(gallons: List[int], distances: List[int]) -> int:
#     for start in range(len(gallons)):
#         cur = 0
#         cur += gallons[start]
#         needed = distances[start]//20
#         if needed > cur:
#             continue
#         else:
#             idx = (start+1)%len(gallons)
#             cur -= needed
#             while idx != start:
#                 cur += gallons[idx]
#                 needed = distances[idx]//20
#                 if needed > cur:
#                     break
#                 else:
#                     idx = (idx+1)%len(gallons)
#                     cur -= needed
#             else:
#                 return start

# This solution works
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    arr = []
    cur = 0
    best = (float('inf'), -1)
    for i in range(len(gallons)):
        best = min(best, (cur, i))
        cur += gallons[i]
        cur -= distances[i]//20
    return best[1]

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
