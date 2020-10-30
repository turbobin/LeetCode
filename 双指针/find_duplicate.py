# -*- coding: utf-8 -*-
"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
(链接：https://leetcode-cn.com/problems/find-the-duplicate-number)

示例：
    输入: [1,3,4,2,2]
    输出: 2

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化，一前一后两个指针(必须一前一后，不能在同一个位置)
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            # slow 走一步，fast 走两步
            slow =  nums[slow]
            next_ = nums[fast]
            fast = nums[next_]

        # slow 放到起点，这时候 slow 和 fast 每次都走一步，直到两个再次相遇
        slow = 0
        while slow != fast:
            # 两个点再次相遇时，即是环的入口
            slow = nums[slow]
            fast = nums[fast]
            
        return slow



if __name__ == '__main__':
    nums = [3,1,3,4,2]
    result = Solution().findDuplicate(nums)
    print(result)