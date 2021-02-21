from typing import List

from test_framework import generic_test


#    [1,  4,  2,  5,  6]
#                     .
#                 .   .
#         .       .   .
#         .       .   .
#         .   .   .   .
#     .   .   .   .   .
#    1x5 4x1 2x4 5x2 6x1
def calculate_largest_rectangle(heights: List[int]) -> int:
    if not heights:
        return 0
    # A "skyline" is the rectangle section drawn using a subset of adjacent buildings.
    # the ith skyline represents the skyline with height heights[i] and includes the ith building.
    skylines = [height for height in heights]
    
    # For each skyline, calculate the left side of the skyline.
    monoq = []
    for i, height in enumerate(heights):
        # best_prev keeps track of the best previous index that is at least `height` tall.
        best_prev = i
        # pop off previous buildings that are taller than or equal to `height`, and update best_prev.
        while monoq and monoq[-1][0] >= height:
            _, best_prev = monoq.pop()
        # append the current `height` and best_prev
        monoq.append((height, best_prev))
        # add the rectangle between the current i and best_prev
        skylines[i] += height * (i-best_prev)

    # For each skyline, calculate the right side of the skyline.
    # This can be done by just reversing heights and skylines and repeating the same procedure.
    monoq = []
    skylines.reverse()
    for i, height in enumerate(reversed(heights)):
        best_prev = i
        while monoq and monoq[-1][0] >= height:
            _, best_prev = monoq.pop()
        monoq.append((height, best_prev))
        skylines[i] += height * (i-best_prev)

    return max(skylines)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
