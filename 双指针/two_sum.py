# -*- coding: utf-8 -*-
"""
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
例如：
    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 1
        index2 = len(numbers)
        while index1 <= index2:
            if numbers[index1-1] + numbers[index2-1] > target:
                index2 -= 1
            elif numbers[index1-1] + numbers[index2-1] < target:
                index1 += 1
            else:
                return index1, index2
        return None, None


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        numbers = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(numbers, target)
        self.assertEqual((1,2), result)


if __name__ == '__main__':
    unittest.main()