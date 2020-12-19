# -*- coding: utf-8 -*-
"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。(链接：https://leetcode-cn.com/problems/3sum)
"""

class Solution:
    def three_sum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n):
            # 避免重复元素
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            # 转化为求两数之和
            target = -1 * a
            two_nums = self.two_sums(nums[i+1:], target)
            for two_num in two_nums:
                b, c = two_num
                result.append([a, b, c])
        return result

    def two_sums(self, nums, target):
        i, j = 0, len(nums) - 1
        arr = set()     # 用set结构，避免元素重复
        while i < j:
            if nums[i] + nums[j] == target:
                item = (nums[i], nums[j])
                arr.add(item)
                i += 1
                j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return arr


if __name__ == '__main__':
    nums = [-1, -1, -1, 2]
    result = Solution().three_sum(nums)
    print(result)