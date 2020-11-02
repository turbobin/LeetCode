# -*- coding: utf-8 -*-
"""
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例：
    输入: n = 12
    输出: 3 
    解释: 12 = 4 + 4 + 4.
"""
class Solution(object):
    def numSquares(self, n):
        # 以 n 为根节点构造一颗树，不断减去完全平方数数组中的值，直到叶子节点第一次出现完全平方数
        # 可以转换成广度优先搜索，搜索的层数即是求解的个数
        nums = [i ** 2 for i in range(n) if i ** 2 <= n]
        visited = set()
        visited.add(n)
        q = [n]
        cnt = 1
        while q:
            for _ in range(len(q)):
                num = q.pop(0)
                if num in nums:
                    return cnt
                for square in nums:
                    mod = num - square
                    if mod in visited or mod < 0:
                        continue
                    q.append(mod)

            cnt += 1


if __name__ == '__main__':
    n = 13
    result = Solution().numSquares(n)
    print(result)



