# -*- coding: utf-8 -*-

class Solution:
    def binarySearch(self, nums, key):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < key:
                low = mid + 1
            elif nums[mid] > key:
                high = mid - 1
            else:
                return mid
        return None

if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 8, 9]
    index = Solution().binarySearch(nums, 7)
    print(index)