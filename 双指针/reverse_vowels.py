# -*- coding: utf-8 -*-
"""
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例：
    输入："hello"
    输出："holle"

    输入："leetcode"
    输出："leotcede"
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        i = 0
        j = len(s) - 1
        # 先把字符串转成数组
        s = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                # 交换元素，双指针同时移动
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
        return ''.join(s)


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        result = self.solution.reverseVowels("hello")
        self.assertEqual("holle", result)


if __name__ == '__main__':
    unittest.main()