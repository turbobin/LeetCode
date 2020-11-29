# -*- coding: utf-8 -*-
"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""

class Solution:
    def permute(self, nums):
        result = []
        arr = []
        visited = set()

        def full_array(k):
            if k == len(nums):
                result.append(arr[:])
                return
            for num in nums:
                if num in visited:
                    continue
                arr.append(num)
                visited.add(num)
                full_array(k+1)
                visited.remove(num)
                arr.pop()

        full_array(0)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)