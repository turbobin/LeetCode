# -*- coding: utf-8 -*-
"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。
(链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array)

示例：
    输入: [3,4,5,1,2]
    输出: 1
"""
class Solution(object):
    def findMin(self, nums):
        # 使用二分法来查找
        low = 0
        high = len(nums) - 1
        # 判断是否有旋转
        if nums[high] > nums[low]:
            return nums[low]
        while low <= high:
            mid = low + (high - low) // 2
            # 和元素头或者元素尾比较大小
            if nums[mid] > nums[low]:
                low = mid + 1
            else:
                high = mid - 1
            # 找到最小值有两种情况
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]


if __name__ == '__main__':
    nums = [4, 5, 6, 0, 1, 3]
    result = Solution().findMin(nums)
    print(result)