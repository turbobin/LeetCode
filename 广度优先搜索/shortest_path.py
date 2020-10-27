# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n
        # 一个坐标点的 8 个方向
        directions = [(-1, -1), (1, 0), (0, 1), (-1, 0),
                      (0, -1), (1, 1), (1, -1), (-1, 1)]
        queue = deque()
        start = (0, 0)
        queue.append(start)
        path = 1
        while queue:
            for _ in range(len(queue)):
                print(path, queue)
                i, j = queue.popleft()
                for dx, dy in directions:
                    x, y = i+dx, j+dy
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if grid[x][y] == 1:
                        continue
                    if x == n - 1 and y == n - 1:
                        return path + 1
                    item = (x, y)
                    queue.append(item)
                    grid[x][y] = 1      # 标记为已访问
            path += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    path = s.shortestPathBinaryMatrix(grid)
    print("path:", path)
