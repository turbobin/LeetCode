# -*- coding: utf-8 -*-
"""
77.组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例：
    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        arr = []

        def back_track(start=1):
            if len(arr) == k:
                result.append(arr[:])

            for num in range(start, n+1):
                arr.append(num)
                back_track(num + 1)
                arr.pop()

        back_track()
        return result


if __name__ == '__main__':
    n, k = 4, 3
    result = Solution().combine(n, k)
    print(result)
