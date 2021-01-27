from typing import List

from test_framework import generic_test
# This solution works
# def get_max_trapped_water(heights: List[int]) -> int:
#     best = 0
#     highest = 0
#     left, right = 0, len(heights) - 1
#     while left < right:
#         # if left is less than or equal to highest
#         if heights[left] <= highest:
#             left += 1
#         # if right is less than or equal to highest
#         elif heights[right] <= highest:
#             right -= 1
#         # if both left and right are greater than highest
#         else:
#             highest = min(heights[left], heights[right])
#             best = max(best, highest * (right-left))
#     return best

# This solution works - just move the side whose height is lower
# your height has to be always increasing! (because your width is always decreasing)
def get_max_trapped_water(heights: List[int]) -> int:
    left = 0 
    right = len(heights)-1
    best = 0
    best_height = 0
    while left < right:
        best = max(best, (right - left) * min(heights[right], heights[left]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best


# This approach does not work
# def get_max_trapped_water(heights: List[int]) -> int:
#     #                       |
#     #                    |  |
#     #              |  |  |  |                          |
#     #           |  |  |  |  |        |     |           |
#     #     |     |  |  |  |  |  |     |     |  |     |  |
#     #  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#     # [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
#     #             this                                this
#     #  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
#     # 48 = 12 * 4
    
#     left = 0 
#     right = len(heights)-1
#     best = 0
#     best_height = 0
#     while left < right:
#         # print('tests', right - left, min(heights[right], heights[left]), (right - left + 1) * min(heights[right], heights[left]))
#         best = max(best, (right - left) * min(heights[right], heights[left]))
#         if (heights[left+1] - heights[left]) > (heights[right-1] - heights[right]):
#             left += 1
#         else:
#             right -= 1
#     return best

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
