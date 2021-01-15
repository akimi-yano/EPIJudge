from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    def helper(row, col, prev_color):
        if not (0 <= row <= len(image)-1) or not (0 <= col <= len(image[0])-1) or image[row][col] != prev_color:
            return 
        image[row][col] = image[row][col] ^ 1
        helper(row, col+1, prev_color)
        helper(row, col-1, prev_color)
        helper(row+1, col, prev_color)
        helper(row-1, col, prev_color)
    
    helper(x,  y, image[x][y])

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
