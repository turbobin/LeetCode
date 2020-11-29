# -*- coding: utf-8 -*-
"""
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
（链接：https://leetcode-cn.com/problems/subsets）

示例：
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums):
        result = [[]]
        arr = []
        n = len(nums)

        def back_track(k, start=0):
            if len(arr) == k:
                result.append(arr[:])
                return

            for i in range(start, n):
                arr.append(nums[i])
                back_track(k, i + 1)
                arr.pop()

        for k in range(1, n+1):
            back_track(k)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    print(result)