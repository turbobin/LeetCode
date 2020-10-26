# -*- coding: utf-8 -*-
"""
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

示例：
    输入: "abca"
    输出: True
    解释: 你可以删除c字符。
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.check_is_palindrome(s[i:j]) or self.check_is_palindrome(s[i+1: j+1])
            i += 1
            j -= 1
        return True

    def check_is_palindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


import unittest
class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "acbcea"
        result = self.solution.validPalindrome(s)
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()


