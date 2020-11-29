# -*- coding: utf-8 -*-
"""
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例：
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
"""

class Solution:
    def subsetsWithDup(self, nums):
        result = [[]]
        arr = []
        visited = set()
        # 先排序
        nums = sorted(nums)
        n = len(nums)

        def back_track(k, start=0):
            if len(arr) == k:
                result.append(arr[:])
                return

            for i in range(start, n):
                item = (i, nums[i])
                if item in visited:
                    continue
                # 剪枝，如果当前元素与前一个元素相同，且前一个元素没有访问过，则跳过
                last_item = (i-1, nums[i-1])
                if i > 0 and nums[i] == nums[i-1] and last_item not in visited:
                    continue
                arr.append(nums[i])
                visited.add(item)
                back_track(k, i + 1)
                visited.remove(item)
                arr.pop()

        for k in range(1, n+1):
            back_track(k)

        return result


if __name__ == '__main__':
    nums = [1, 2, 2, 1]
    result = Solution().subsetsWithDup(nums)
    print(result)