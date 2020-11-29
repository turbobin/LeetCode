# -*- coding: utf-8 -*-
"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。(链接：https://leetcode-cn.com/problems/word-search)
示例：
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    给定 word = "ABCCED", 返回 true
    给定 word = "SEE", 返回 true
    给定 word = "ABCB", 返回 false
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, k=0):
            # 匹配到结尾了
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            item = (i, j)
            if item in visited:
                return False
            visited.add(item)
            for dx, dy in directions:
                x, y = i+dx, j+dy
                ret = dfs(x, y, k+1)
                if ret:
                    return True
            visited.remove(item)

        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True
        return False


if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCEE"
    result = Solution().exist(board, word)
    print(result)