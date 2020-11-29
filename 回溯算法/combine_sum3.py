# -*- coding: utf-8 -*-
"""
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。
组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
    - 所有数字都是正整数。
    - 解集不能包含重复的组合。

示例：
    输入: k = 3, n = 7
    输出: [[1,2,4]]
"""

class Solution:
    def combinationSum3(self, k, n):
        result = []
        arr = []

        def dfs(target, start=1):
            if target < 0:
                return
            if target == 0 and len(arr) == k:
                result.append(arr[:])
                return
            # 数字 1-9
            for i in range(start, 10):
                arr.append(i)
                num = target - i
                dfs(num, i + 1)
                arr.pop()

        dfs(n)
        return result


if __name__ == '__main__':
    k = 3
    n = 9
    result = Solution().combinationSum3(k, n)
    print(result)