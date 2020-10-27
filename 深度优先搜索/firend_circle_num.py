# -*- coding: utf-8 -*-


class Solution(object):
    def findCircleNum(self, grid):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        nums = 0
        self.N = len(grid)
        for i in range(self.N):
            friends = self.dfs(grid, i)
            nums = nums + 1 if friends else nums
        return nums

    def dfs(self, grid, i):
        visited = set()
        self._recur_dfs(grid, i, visited)
        return visited

    def _recur_dfs(self, grid, i, visited):
        for j in range(self.N):
            if grid[i][j] == 0:
                continue
            item = (i, j)
            visited.add(item)
            grid[i][j] = 0      # 标记为0，不再访问
            self._recur_dfs(grid, j, visited)


import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        grid = [
         [1,0,0,1],
         [0,1,1,0],
         [0,1,1,1],
         [1,0,1,1]
        ]
        result = self.solution.findCircleNum(grid)
        output = 1
        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()
