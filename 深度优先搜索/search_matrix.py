# -*- coding: utf-8 -*-
"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
(链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii)
"""


class Solution:
    def searchMatrix(self, matrix, target):
        # 使用深度优先搜索
        if not matrix:
            return (-1, -1)
        n = len(matrix)
        m = len(matrix[0])
        visited = set()
        pos = []

        def dfs(x, y):
            if pos:
                return
            if x < 0 or y < 0 or x >= n or y >= m:
                return
            item = (x, y)
            if item in visited:
                return
            if matrix[x][y] == target:
                pos.append(item)
                return
            visited.add(item)
            if matrix[x][y] < target:
                dfs(x+1, y)
                dfs(x, y+1)
                dfs(x+1, y+1)
            if matrix[x][y] > target:
                dfs(x-1, y)
                dfs(x, y-1)
                dfs(x-1, y-1)

        # 为加快效率，从中间位置开始搜索
        dfs(n>>1, m>>1)
        return pos[0] if pos else (-1, -1)


if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    result = Solution().searchMatrix(matrix, 26)
    print(result)
