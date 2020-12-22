import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

from collections import deque
def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    s_x, s_y = s[0], s[1]
    e_x, e_y = e[0], e[1]
    queue = deque([[s_x, s_y, [(s_x, s_y)]]])
    
    while queue:    
        x, y, path = queue.popleft()
        if x == e_x and y == e_y:
            return path
        if maze[x][y] == 1:
            continue
        maze[x][y] = 1
        
        for new_x, new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= new_x <= len(maze)-1 and 0 <= new_y <= len(maze[0])-1 and maze[new_x][new_y] == 0:
                queue.append([new_x, new_y, path + [Coordinate(x = new_x, y = new_y)]])
    return []


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
