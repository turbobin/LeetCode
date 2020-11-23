# -*- coding: utf-8 -*-
"""
503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
(链接：https://leetcode-cn.com/problems/next-greater-element-ii)
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        # 为了方便从头循环搜索一遍元素，把数组组合成一个2n的数组
        n = len(nums)
        nums = nums + nums
        arr = [-1] * n
        stack = []
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                prev = stack.pop(-1)
                arr[prev] = num
            if i < n:
                stack.append(i)
        return arr


if __name__ == '__main__':
    nums = [1, 2, 1]
    result = Solution().nextGreaterElements(nums)
    print(result)



