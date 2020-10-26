# -*- coding: utf-8 -*-
"""
75. 颜色分类(荷兰国旗问题)
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例：
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]

    输入: [1,1,2]
    输出: [1,1,2]
"""
class Solution(object):
    def sortColors(self, nums):
        """
        思路1：最简单可以使用冒泡排序或快速排序解决，时间复杂度较高
        思路2：可以使用计数排序，时间复杂度为O(n)，但不是原地排序算法
        思路3：排序数据比较特别，只有0,1,2；可使用双指针操作，比较巧妙
        """
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1
        return nums


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2,0,2,1,1,0]
        output = [0,0,1,1,2,2]
        result = self.solution.sortColors(nums)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()