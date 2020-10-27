# -*- coding: utf-8 -*-
"""
695. 岛屿的最大面积
一个岛屿是由一些相邻的1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
"""
import unittest


class Solution(object):
    def maxAreaOfIsland(self, grid):
        area = {0}
        self.N = len(grid)
        for i in range(self.N):
            self.M = len(grid[i])
            for j in range(self.M):
                if grid[i][j] == 0:
                    continue
                visited = self.dfs(grid, i, j)
                area.add(visited)
        return max(area)

    def dfs(self, grid, i, j):
        visited = set()
        self._recur_dfs(grid, i, j, visited)
        return len(visited)

    def _recur_dfs(self, grid, i, j, visited):
        visited.add((i, j))
        grid[i][j] = 0      # 标记为0，不再访问
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= self.N or y >= self.M:
                continue
            if grid[x][y] == 0:
                continue
            item = (x, y)
            if item in visited:
                continue
            self._recur_dfs(grid, x, y, visited)


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        result = self.solution.maxAreaOfIsland(grid)
        output = 6
        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()

