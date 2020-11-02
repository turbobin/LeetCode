# -*- coding: utf-8 -*-
"""
540. 有序数组中的单一元素
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例：
    输入: [1,1,2,3,3,4,4,8,8]
    输出: 2

    输入: [3,3,7,7,10,11,11]
    输出: 10
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                low = mid + 2   # 因为前面mid=mid-1, 注意这里要+2，否则会导致死循环
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    nums = [1,1,2,3,3,4,4,8,8]
    result = Solution().singleNonDuplicate(nums)
    print(result)