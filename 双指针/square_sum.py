# -*- coding: utf-8 -*-
"""
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
示例1：
    输入：c = 5
    输出：true
    解释：1 * 1 + 2 * 2 = 5

示例2：
    输入：c = 1
    输出：true

示例3：
    输入：c = 3
    输出：false
"""
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        # 为了避免超时，需要缩短指针的范围，可以取c的根号方
        # b = c
        b = int(c ** 0.5)
        while a <= b:
            if a*a + b*b > c:
                b -= 1
            elif a*a + b*b < c:
                a += 1
            else:
                return True
        return False


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        result = self.solution.judgeSquareSum(1000000000)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()