# -*- coding: utf-8 -*-
"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
（链接：https://leetcode-cn.com/problems/surrounded-regions）
示例：
    X X X X
    X O O X
    X X O X
    X O X X
运行后变成:
    X X X X
    X X X X
    X X X X
    X O X X
"""
class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return board
        n = len(board)
        m = len(board[0])
        visited = set()
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return
            if board[x][y] != "O":
                return
            board[x][y] = "V"   # 打上标记
            visited.add((x, y))
            for dx, dy in direction:
                i = x + dx
                j = y + dy
                item = (i, j)
                if item in visited:
                    continue
                dfs(i, j)

        # 分别从四个边界出发进行dfs，对所有可访问到的‘O’都打上标记
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        # 遍历矩阵，对 O 用 X 覆盖，对 V 用 X 还原
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "V":
                    board[i][j] = "O"
        return board


if __name__ == '__main__':
    board = [
        ["X","X","X","X"],
        ["X","O","X","X"],
        ["X","X","O","X"],
        ["X","O","O","X"]
    ]
    result = Solution().solve(board)
    print(result)


