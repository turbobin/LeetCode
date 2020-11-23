# -*- coding: utf-8 -*-
"""
417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
（链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow）

示例：
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋
返回:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        # 设置两个矩阵记录能到达边界的点
        P = [[False] * m for _ in range(n)]
        A = [[False] * m for _ in range(n)]

        def dfs(i, j, R):
            R[i][j] = True
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                # 如果边界点大于邻接的点，则无法流通
                if matrix[i][j] > matrix[x][y]:
                    continue
                if R[x][y]:
                    continue
                dfs(x, y, R)

        for i in range(n):
            dfs(i, 0, P)    # can reach Pacifix
            dfs(i, m-1, A)  # can reach Atlantic

        for j in range(m):
            dfs(0, j, P)    # can reach Pacifix
            dfs(n-1, j, A)  # can reach Atlantic

        result = []
        # 找出两边都能流通的坐标点
        for i in range(n):
            for j in range(m):
                if P[i][j] is True and A[i][j] is True:
                    result.append([i, j])
        return result


if __name__ == '__main__':
    matrix = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    result = Solution().pacificAtlantic(matrix)
    print(result)