# -*- coding: utf-8 -*-
"""
200. 岛屿数量
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
(链接：https://leetcode-cn.com/problems/number-of-islands)
"""


import unittest


class Solution(object):
    def numIslands(self, grid):
        nums = 0
        self.N = len(grid)
        for i in range(self.N):
            self.M = len(grid[i])
            for j in range(self.M):
                if grid[i][j] == "0":
                    continue
                visited = self.dfs(grid, i, j)
                print(visited)
                nums += 1 if visited else nums
        return nums

    def dfs(self, grid, i, j):
        visited = set()
        self._recur_dfs(grid, i, j, visited)
        return visited

    def _recur_dfs(self, grid, i, j, visited):
        visited.add((i, j))
        grid[i][j] = "0"      # 标记为0，不再访问
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= self.N or y >= self.M:
                continue
            if grid[x][y] == "0":
                continue
            item = (x, y)
            if item in visited:
                continue
            self._recur_dfs(grid, x, y, visited)


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        result = self.solution.numIslands(grid)
        output = 3
        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()
