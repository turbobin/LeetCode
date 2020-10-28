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
        # 使用广度优先搜索
        if not matrix:
            return (-1, -1)
        n = len(matrix)
        m = len(matrix[0])
        start = (0, 0)
        visited = {start}
        queue = [start]
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.pop(0)
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                if matrix[x][y] == target:
                    return (x, y)
                item = (x, y)
                if item in visited:
                    continue
                queue.append(item)
                visited.add(item)
        return (-1, -1)


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
